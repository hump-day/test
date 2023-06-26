from django.db import models
from django.contrib.auth.models import User


class test(models.Model):
    title = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)


class transect(models.Model):
    name = models.CharField(blank=True, max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transects')
    date = models.DateTimeField()
    # observations: observations foreign key
    # nodes: transect_nodes foreign key


class observation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    species = models.CharField(null=True, max_length=20)
    # CheckListBank Taxon ID (max length is arbitrary idk what it is)

    transect = models.ForeignKey(transect, on_delete=models.CASCADE, related_name='observations')
    date_offset = models.DurationField()
    # images: obvs_image foreign key


class obvs_image(models.Model):
    url = models.URLField()
    observation = models.ForeignKey(observation, on_delete=models.CASCADE, related_name='images')


class transect_node(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    index = models.IntegerField()
    transect = models.ForeignKey(transect, on_delete=models.CASCADE, related_name='nodes')

    class Meta:
        unique_together = ['transect', 'index']
        ordering = ['index']

    # sort the nodes by index to recreate the path
