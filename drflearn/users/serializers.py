from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate


class login_serializer(serializers.Serializer):
    user = User

    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
