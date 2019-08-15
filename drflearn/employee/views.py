from django.shortcuts import render
from rest_framework import viewsets,
from django.contrib.auth.models import User
from .serializers import employee_serializer, login_serializer
from rest_framework.views import APIView


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = employee_serializer


class login_view(APIView):
    def post(self, request):
        data = request.data
        serializer = login_serializer(data)
