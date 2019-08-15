from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import employee_serializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = employee_serializer
