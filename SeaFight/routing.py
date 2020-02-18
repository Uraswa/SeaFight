from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from SeaFight.consumers import GameConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
[path("ws/<str:id>/<str:is_host>/", GameConsumer)]
        )
    ),
})