from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import RegisterSerializer
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()
    def create(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)
        print(username, password)
        return Response({'success': 'User created successfully',
                         'user_id': user.id,
                         'refresh': str(refresh),
                        'access': str(refresh.access_token)
                        })
    





    