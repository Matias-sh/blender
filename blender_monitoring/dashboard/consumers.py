import paho.mqtt.client as mqtt
from channels.generic.http import AsyncHttpConsumer
from .models import MonitoringData, AlarmLog
import json

class MQTTConsumer(AsyncHttpConsumer):
    print("nashe")
    async def handle(self, body):
        self.mqtt_client = mqtt.Client()

        async def on_connect(client, userdata, flags, rc):
            print("Conectado al broker MQTT")
            client.subscribe("polo/blender_dashboard")  # Suscripción al tema deseado

        async def on_message(client, userdata, msg):
            payload = msg.payload.decode("utf-8")
            data = json.loads(payload)

            monitoring_data = MonitoringData(
                oxygen=data['oxygen'],
                pressure=data['pressure'],
                flow=data['flow'],
                co2=data['co2'],
                spo2=data['spo2']
            )
            monitoring_data.save()

            if data.get('alarm', False):
                alarm_message = "¡Alarma! Problema detectado en el dispositivo."
                alarm_log = AlarmLog(message=alarm_message)
                alarm_log.save()

        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message

        self.mqtt_client.connect("localhost", 1883, 60)  # Conexión al broker MQTT en localhost

        # Iniciar el bucle en segundo plano
        self.mqtt_client.loop_start()

        # Mantener el consumidor activo mientras la conexión MQTT esté activa
        while True:
            await asyncio.sleep(1)
