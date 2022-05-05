from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from publication.models import Category, Post
from publication.serializers import CategorySerializer, PostSerializer
from publication.log_module import logger
# Create your views here.


class CategoryView(APIView):
	def get(self, request):
		categories = Category.objects.all()
		serializer = CategorySerializer(categories, many=True)
		logger.info(f'{request.user.id} user got all categories')
		return Response({'categories': serializer.data})


class PostView(APIView):
	def get(self, request):
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response({'posts': serializer.data})
	def post(self, request):
		post = request.data.get('post')
		serializer = PostSerializer(data=post)
		res = None
		if serializer.is_valid(raise_exception=True):
			res = serializer.save(sender_id=post.get('sender_id'))
		if res is not None:
			return  Response({"success":"Done"})
		else:
			logger.info(f'{request.user.id} user send wrong request')
			return  Response({"error":"Wrong"})
	def put(self, request, id):
		post = Post.objects.get(id=id)
		data = request.data.get('post')
		serializer = PostSerializer(instance=post, data=data, partial=True)
		res = None
		if serializer.is_valid(raise_exception=True):
			res = serializer.save()
		if res is not None:
			ogger.info(f'{request.user.id} user updated {id} id post')
			return  Response({"success":"Done"})
		else:
			return  Response({"error":"Wrong"})