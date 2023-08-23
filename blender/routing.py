from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from myapp import consumers  # Asegúrate de reemplazar 'myapp' con el nombre de tu aplicación

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/some_path/", consumers.SomeConsumer.as_asgi()),
    ]),
})
