from django.contrib import admin

from twitter import models

admin.site.register(models.Tweet)
admin.site.register(models.Comment)
admin.site.register(models.Message)

