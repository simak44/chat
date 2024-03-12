from django.contrib import admin
from .models import GroupModel, ChatModel
# Register your models here.
@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'groupname']

@admin.register(ChatModel)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'groupnamec', 'content']