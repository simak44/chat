"""
ASGI config for jsonconsumer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""


import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter, ProtocolTypeRouter
import  myapp.routing 
from channels.auth import AuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jsonconsumer.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(
        myapp.routing.websocket_urlpatterns
        )),
})