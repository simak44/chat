from channels.consumer import  AsyncConsumer, SyncConsumer
from channels.generic.websocket import JsonWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from myapp.models import GroupModel, ChatModel

class MyJsonConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()
        print('WebSocket Consumer Accepted!!!')
        self.groupname = self.scope['url_route']['kwargs']['groupName']
        print(self.groupname)
        async_to_sync(self.channel_layer.group_add)(self.groupname, self.channel_name)
    
    def receive_json(self, content):
        print('Message from Client!!!', content)
        # self.send_json({'msg':'hello from server to client'})
        group = GroupModel.objects.get(groupname=self.groupname)
        if self.scope['user'].is_authenticated:
            chat = ChatModel(
                content= content['msg'],
                groupnamec = group
            )
            chat.save()
            async_to_sync(self.channel_layer.group_send)(
                self.groupname,
                {
                'type': 'chat.message',
                'message':content['msg']
                })
        else:
             self.send_json({
                  'message':'Login required to send message'
             })
    def chat_message(self, event):
            print(event)
            self.send_json({
             'message':event['message']
            })


    def disconnect(self, close_code):
        print('Websocket Disconnected!!!', close_code)
