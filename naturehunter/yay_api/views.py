from django.shortcuts import render
from rest_framework import generics
from . import serializers, models


class testList(generics.ListAPIView):
    serializer_class = serializers.testSerializer
    queryset = models.test.objects.all()

# Create your views here.
