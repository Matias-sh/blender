from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from dashboard.consumers import MQTTConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([]),
    "http": URLRouter([
        path("mqtt_receiver/", MQTTConsumer.as_asgi()),
    ]),
})
