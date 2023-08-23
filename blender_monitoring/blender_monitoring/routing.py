from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from dashboard import consumers  # Importa los consumidores de tu aplicación

application = ProtocolTypeRouter({
    "websocket": URLRouter([]),  # Mantén solo el websocket si es necesario
})
