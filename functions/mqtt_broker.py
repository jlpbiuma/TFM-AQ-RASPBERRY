import paho.mqtt.client as mqtt
import os

# Use os.environ.get() with a default value instead of direct access to os.environ
BACKEND_URL = os.environ.get("BACKEND_URL", "")
TOPIC_1 = os.environ.get("TOPIC_1", "")

print("BACKEND_URL:", BACKEND_URL)  # Print the environment variables to debug
print("TOPIC_1:", TOPIC_1)

def initialize_mqtt():
    # Configuración del cliente MQTT
    mqtt_client = mqtt.Client()
    # Conexión al broker Mosquitto
    mqtt_client.connect("mosquitto", 1883, 60)
    mqtt_client.loop_start()
    mqtt_client.subscribe(TOPIC_1)
    return mqtt_client
