from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
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


class transects(viewsets.ModelViewSet):
    queryset = models.transect.objects.all().order_by('date')
    serializer_class = serializers.transectSerializer


class observations(viewsets.ModelViewSet):
    queryset = models.observation.objects.all().order_by('transect')
    serializer_class = serializers.observationSerializer
