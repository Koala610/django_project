from rest_framework import serializers
from django.contrib.auth import authenticate
from users.serializers import UserSerializer


class MessageSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=200)
    sender = UserSerializer(source='outbox', read_only=True)
    reciever = UserSerializer(source='inbox', read_only=True)