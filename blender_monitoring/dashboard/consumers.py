import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blender_monitoring.settings")
django.setup()

import asyncio
import paho.mqtt.client as mqtt
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import MonitoringData, AlarmLog
from celery import shared_task
import json

class MQTTConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.username_pw_set(username="matias777", password="matiasdeb777")
        
        try:
            self.mqtt_client.connect("192.168.216.225", 1883, 60)
            self.mqtt_client.subscribe("polo/blender_monitoring")
            self.mqtt_client.loop_start()
        except Exception as e:
            print(f"Error connecting to MQTT: {e}")

    async def disconnect(self, close_code):
        try:
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()
        except Exception as e:
            print(f"Error disconnecting from MQTT: {e}")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker successfully!")
        else:
            print(f"Failed to connect to MQTT broker. Return code: {rc}")

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected from MQTT broker.")

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
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Error processing MQTT message: {e}")
