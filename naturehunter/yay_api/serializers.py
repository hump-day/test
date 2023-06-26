from typing import Mapping

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
        fields = ['url', 'username', 'email', 'groups', 'transects']


class groupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class obvs_imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.obvs_image
        fields = ['url']


class observationSerializer(serializers.ModelSerializer):
    images = obvs_imageSerializer(many=True)

    class Meta:
        model = models.observation
        fields = ['latitude', 'longitude', 'species', 'date_offset', 'transect', 'images']

    def create(self, validated_data: dict):

        images = validated_data.pop('images')
        temp = super().create(validated_data)
        for image in images:
            temp.images.create(**image)

        print(validated_data)
        # super().create(validated_data)
        return temp

    def update(self, instance, validated_data):
        images = validated_data.pop('images')
        temp = super().update(instance, validated_data)

        for image in images:
            temp.images.create(**image)
        return temp


class transect_nodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.transect_node
        fields = ['latitude', 'longitude', 'index']


class transectSerializer(serializers.ModelSerializer):
    nodes = transect_nodeSerializer(many=True)
    observations = observationSerializer(many=True)

    # observations = serializers.HyperlinkedRelatedField(
    #    many=True,
    #    view_name='observation-detail',
    #    read_only=True,
    # )

    class Meta:
        model = models.transect
        fields = ['name', 'user', 'date', 'nodes', 'observations']

    def create(self, validated_data):
        nodes = validated_data.pop('nodes')
        observations = validated_data.pop('observations')

        temp = models.transect.objects.create(**validated_data)

        for node in nodes:
            temp.nodes.create(**node)

        for observation in observations:
            temp.observations.create(**observation)

        return temp

    def update(self, instance, validated_data):
        nodes = validated_data.pop('nodes')
        observations = validated_data.pop('observations')

        temp = super().update(instance, validated_data)

        for node in nodes:
            temp.nodes.create(**node)

        for observation in observations:
            temp.observations.create(**observation)

        return temp


"""{
    "latitude": 0,
    "longitude": 0,
    "species": null,
    "date_offset": 0,
    "images": []
}
"""
