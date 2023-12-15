import json
import random
import time
from websocket_server import WebsocketServer

# Función llamada cuando un cliente se conecta
def new_client(client, server):
    print(f"Nuevo cliente conectado y fue dado id {client['id']}")

# Función llamada cuando un cliente envía un mensaje
def message_received(client, server, message):
    print(f"Cliente({client['id']}) dijo: {message}")

# Función para enviar datos aleatorios
def send_random_data():
    while True:
        data = {
            "oxygen": random.randint(90, 100),
            "pressure": random.randint(120, 130),
            "flow": random.randint(50, 60),
            "co2": random.randint(35, 45),
            "spo2": random.randint(95, 100),
            "alarm": random.choice([True, False])
        }
        server.send_message_to_all(json.dumps(data))
        time.sleep(5)

# Crear un servidor WebSocket en el puerto 8000
server = WebsocketServer(8000, host='192.168.216.108')
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)

# Iniciar el servidor en un hilo separado
import threading
thread = threading.Thread(target=send_random_data)
thread.start()

# Ejecutar el servidor indefinidamente
server.run_forever()
