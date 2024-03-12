from django.db import models

# Create your models here.
class GroupModel(models.Model):
    groupname = models.CharField(max_length = 20)
    def __str__(self):
        return self.groupname

class ChatModel(models.Model):
    groupnamec = models.ForeignKey('GroupModel', on_delete = models.CASCADE)
    content = models.CharField(max_length = 1000)