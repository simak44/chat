from django.urls import path
from myapp import consumers
websocket_urlpatterns=[
    # path('ws/sc/pakistan/', consumers.MyJsonConsumer.as_asgi()),
    path('ws/sc/<str:groupName>/', consumers.MyJsonConsumer.as_asgi()),

]