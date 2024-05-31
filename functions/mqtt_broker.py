import paho.mqtt.client as mqtt

TOPIC_PATTERN = "estacion/+/magnitud/+"  # Adjust this pattern as needed

def initialize_mqtt():
    # Configuración del cliente MQTT
    mqtt_client = mqtt.Client()
    # Conexión al broker Mosquitto
    mqtt_client.connect("mosquitto", 1883, 60)
    mqtt_client.loop_start()
    mqtt_client.subscribe(TOPIC_PATTERN)
    return mqtt_client
