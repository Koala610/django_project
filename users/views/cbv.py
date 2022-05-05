from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.serializers import UserRegistrSerializer, UserSerializer
from users.forms import ImageUploadModelForm
class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class ImageUploadView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'avatar']
    template_name = 'profile.html'
    success_url = '/profile'