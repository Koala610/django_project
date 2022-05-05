from rest_framework import serializers
from django.contrib.auth import authenticate
from message.serializers import MessageSerializer
from .models import Category, Post




class PostSerializer(MessageSerializer):
	reciever_id = serializers.IntegerField()
	sender_id = serializers.IntegerField()
	body = serializers.CharField()
	rating = serializers.IntegerField()

	def create(self, data):
		return Post.objects.create(**data)

	def update(self, instance, data):
		instance.body = data.get('body', instance.body)
		instance.rating = data.get('rating', instance.rating)
		instance.sender_id = data.get('sender_id', instance.sender_id)
		instance.reciever_id = data.get('reciever_id', instance.reciever_id)
		instance.save()
		return instance


class CategorySerializer(serializers.ModelSerializer):
	posts = PostSerializer(many=True)
	class Meta:
		model = Category
		fields = ('id', 'cover', 'name', 'posts')


