import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blender_monitoring.settings")
django.setup()

import paho.mqtt.client as mqtt
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MonitoringData, AlarmLog
import json

import json
import paho.mqtt.client as mqtt
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MonitoringData

class MQTTConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect("localhost", 1883, 60)
        self.mqtt_client.subscribe("polo/blender_dashboard")
        self.mqtt_client.loop_start()

    async def disconnect(self, close_code):
        self.mqtt_client.loop_stop()

    def on_message(self, client, userdata, msg):
        try:
            payload = msg.payload.decode("utf-8")
            data = json.loads(payload)
            
            # Guardar en la base de datos
            monitoring_data = MonitoringData(
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
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
