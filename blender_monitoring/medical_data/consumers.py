from decouple import config
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import paho.mqtt.client as mqtt
from .models import MonitoringData

class MQTTConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = self.on_message

        # Obtener credenciales desde variables de entorno
        mqtt_username = config('MQTT_USERNAME', default='default_user')
        mqtt_password = config('MQTT_PASSWORD', default='default_password')
        mqtt_host = config('MQTT_HOST', default='localhost')
        mqtt_port = config('MQTT_PORT', default=1883, cast=int)

        # Configurar MQTT
        self.mqtt_client.username_pw_set(username=mqtt_username, password=mqtt_password)
        self.mqtt_client.connect(mqtt_host, mqtt_port, 60)
        self.mqtt_client.subscribe("polo/blender_monitoring")
        self.mqtt_client.loop_start()

    async def disconnect(self, close_code):
        self.mqtt_client.loop_stop()

    def on_message(self, client, userdata, msg):
        try:
            payload = msg.payload.decode("utf-8")
            data = json.loads(payload)

            # Guardar datos en la base de datos
            monitoring_data = MonitoringData(
                patient_id=data['patient_id'],
                oxygen=data['oxygen'],
                pressure=data['pressure'],
                flow=data['flow'],
                co2=data['co2'],
                spo2=data['spo2'],
                alarm=data.get('alarm', False)
            )
            monitoring_data.save()

            # Enviar datos al cliente WebSocket
            self.send(text_data=json.dumps(data))
        except Exception as e:
            print(f"Error processing MQTT message: {e}")
