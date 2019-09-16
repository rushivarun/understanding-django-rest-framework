from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import employee_serializer, login_serializer
from rest_framework.views import APIView
from django.contrib.auth import login as auth_login, logout as auth_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = employee_serializer


class login_view(APIView):
    def post(self, request):
        data = request.data
        serializer = login_serializer(data=data)
        print(data)
        serializer.is_valid()
        user = serializer.validated_data["user"]
        auth_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)


class logout_view(APIView):

    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        auth_logout(request)
        return Response(status=204)
