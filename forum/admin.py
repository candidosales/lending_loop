from django.contrib import admin

# Register your models here.

from .models import Topic, Comment

admin.site.register(Topic)
admin.site.register(Comment)
