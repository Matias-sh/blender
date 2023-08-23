from django.urls import re_path
from apps.monitoring.consumers import MQTTConsumer

websocket_urlpatterns = [
    re_path(r'ws/mqtt/$', MQTTConsumer.as_asgi()),
]