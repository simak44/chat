from django.shortcuts import render
from .models import GroupModel, ChatModel
# Create your views here.
def MyView(request, groupnamee):
    groupnamev = GroupModel.objects.filter(groupname=groupnamee)
    chats = [ ]
    if groupnamev:
        chats = ChatModel.objects.filter(groupnamec__in = groupnamev)
        print(chats)
        
    else:
        group= GroupModel(groupname=groupnamee)
        group.save()

    print(groupnamee)
    return render(request, 'myapp/index.html', {'groupname':groupnamee, 'chats':chats})