from django.contrib import admin
from . import models


class testAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')


admin.site.register(models.test, testAdmin)

# Register your models here.
