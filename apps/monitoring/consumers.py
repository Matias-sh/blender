from channels.generic.websocket import AsyncWebsocketConsumer
import paho.mqtt.client as mqtt

class MQTTConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Conectar al broker MQTT
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect("mqtt.example.com", 1883)

        # Suscribirse a un tema MQTT
        self.mqtt_client.subscribe("my_topic")

        # Establecer la función de callback para recibir mensajes MQTT
        self.mqtt_client.on_message = self.handle_mqtt_message

        # Conectar el websocket de Channels
        await self.accept()

    def handle_mqtt_message(self, client, userdata, msg):
        # Enviar el mensaje recibido a través del websocket
        self.send(msg.payload.decode("utf-8"))

    async def disconnect(self, close_code):
        # Desconectar el cliente MQTT
        self.mqtt_client.disconnect()

    async def receive(self, text_data):
        # Enviar el mensaje recibido a través del cliente MQTT
        self.mqtt_client.publish("my_topic", text_data)