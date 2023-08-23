from django.urls import path, include
from apps.monitoring.views import index
from apps.monitoring import routing

urlpatterns = [
    path('', index, name='index'),
    path('ws/', include(routing.websocket_urlpatterns)),
]