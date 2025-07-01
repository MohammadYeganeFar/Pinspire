from django.shortcuts import render
from rest_framework import viewsets
from account.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from account.models import CustomUser

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
