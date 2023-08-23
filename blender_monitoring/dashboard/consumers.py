import paho.mqtt.client as mqtt
from channels.generic.http import AsyncHttpConsumer
import json
from .models import MonitoringData, AlarmLog

class MQTTConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        print("entro handle")
        self.mqtt_client = mqtt.Client()

        def on_connect(client, userdata, flags, rc):
            print("nashe")
            self.mqtt_client.subscribe("polo/blender_dashboard")  # Reemplaza con el tema MQTT que quieras suscribirte

        def on_message(client, userdata, msg):
            
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

        self.mqtt_client.connect("127.0.0.1", 1883, 60)  # Reemplaza con la dirección de tu broker MQTT
        self.mqtt_client.loop_forever()
