from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.serializers import UserRegistrSerializer, UserSerializer
from users.log_module import logger
from users.forms import ImageUploadModelForm
#logger.info(f'{from_user.username} tried to send friend request to himself')
@login_required
def send_friend_request(request, id):
    user = request.user
    if user.id == id:
        return JsonResponse({"error" : "Can not send to yourself"})
    target = User.objects.get(id=id)
    if str(user.id) in target.requests.split(','):
        return JsonResponse({"error" : "Already sent"})
    if str(user.id) in target.friends.split(','):
        return JsonResponse({"error" : "Already friends"})
    target.requests += f'{user.id},'
    target.save()
    logger.info(f'{user.username} send friend request to {target.username}')
    return JsonResponse({"status" : "Sent"})


@login_required
def accept_friend_request(request, id):
    user = request.user
    if user.id == id:
        return JsonResponse({"error" : "Can accept from yourself"})
    target = User.objects.get(id=id)
    if str(target.id) in user.friends.split(','):
        return JsonResponse({"error" : "Already friends"})
    if str(target.id) in user.requests.split(','):
        target.friends += f'{user.id},'
        user.friends += f'{target.id},'
        res_requests = user.requests.split(',')
        res_requests.remove(str(id))
        user.requests = ','.join(res_requests)
        target.save()
        user.save()
        logger.info(f'{user.username} added {target.username} to friends')
        return JsonResponse({"status" : "Accepted"})
    else:
        return JsonResponse({"error" : "No such request"})


@login_required
def delete_friend(request, id):
    user = request.user
    if user.id == id:
        return JsonResponse({"error" : "Can delete yourself"})
    target = User.objects.get(id=id)
    if str(target.id) in user.friends.split(','):
        res_requests = user.friends.split(',')
        res_requests.remove(str(id))
        user.friends = ','.join(res_requests)
        user.save()
        res_requests = target.friends.split(',')
        res_requests.remove(str(user.id))
        target.friends = ','.join(res_requests)
        target.save()
        return JsonResponse({"status" : "Deleted!"})
    else:
        return JsonResponse({"error" : "You are not friends"})


@login_required
def check_profile(request, id=None):
    user = request.user
    mine = False
    form = ImageUploadModelForm(request.POST or None, request.FILES or None, instance=request.user)
    friends = [User.objects.get(id=i) for i in user.friends.split(',') if i != '']
    requests = [User.objects.get(id=int(i)) for i in user.requests.split(',') if i != '']
    friends = None if len(friends) == 0 else friends
    requests = None if len(requests) == 0 else requests
    if id is None or request.user.id==id:
        id = request.user.id
        mine = True
    return render(request, 'profile.html', {
            'user': User.objects.get(id=id),
            'form': form,
            'mine': mine,
            'friends': friends,
            'requests': requests
            })
    