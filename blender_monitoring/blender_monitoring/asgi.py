import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from medical_data.routing import websocket_urlpatterns  # Importar las rutas WebSocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blender_monitoring.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Manejo de solicitudes HTTP
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Rutas WebSocket
        )
    ),
})
