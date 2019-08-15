from rest_framework import serializers
from django.contrib.auth.models import User


class employee_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'url', 'id', 'username')
