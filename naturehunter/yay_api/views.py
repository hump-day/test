from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import serializers, models
from django.contrib.auth.models import User, Group


class testList(viewsets.ModelViewSet):
    serializer_class = serializers.testSerializer
    queryset = models.test.objects.all()


class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.userSerializer
    permission_classes = [permissions.IsAuthenticated]


class groupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.groupSerializer
    permission_classes = [permissions.IsAuthenticated]
