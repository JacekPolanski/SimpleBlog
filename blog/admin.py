from django.contrib import admin

from .models import Topic, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(Topic)
