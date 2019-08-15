from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions


class employee_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'url', 'id', 'username')


class login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        if username and password:
            user = authenticate(username, password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    message = 'account is disabled'
                    raise exceptions.ValidationError(message)
            else:
                message = 'invalid username or password'
                raise exceptions.ValidationError(message)
        else:
            message = 'must provide both username and password'
            raise exceptions.ValidationError(message)
        return data
