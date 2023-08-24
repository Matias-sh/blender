from django.urls import re_path
from .consumers import MQTTConsumer

websocket_urlpatterns = [
    re_path(r'ws/mqtt_consumer/$', MQTTConsumer.as_asgi()),
]
