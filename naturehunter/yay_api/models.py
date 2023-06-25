from django.db import models


class test(models.Model):
    title = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)

# Create your models here.
