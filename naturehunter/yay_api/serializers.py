from rest_framework import serializers
from . import models


class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.test
        fields = ('title', 'url')
