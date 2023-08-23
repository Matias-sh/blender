import paho.mqtt.client as mqtt
from channels.generic.http import AsyncHttpConsumer
from django.http import HttpResponse

class MQTTConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        self.mqtt_client = mqtt.Client()

        def on_connect(client, userdata, flags, rc):
            self.mqtt_client.subscribe("mqtt_topic")  # Reemplaza con el tema MQTT que quieras suscribirte

        def on_message(client, userdata, msg):
            payload = msg.payload.decode("utf-8")
            # Haz lo que necesites con los datos recibidos, como guardarlos en la base de datos
            print("Mensaje recibido:", payload)

        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message

        self.mqtt_client.connect("mqtt_broker_address", 1883, 60)  # Reemplaza con la dirección de tu broker MQTT
        self.mqtt_client.loop_forever()
