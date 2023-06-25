from rest_framework import serializers
from . import models
from django.contrib.auth.models import User, Group


class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.test
        fields = ('title', 'url')


class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class groupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

