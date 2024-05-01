import paho.mqtt.client as mqtt

def initialize_mqtt(topics):
    # Configuración del cliente MQTT
    mqtt_client = mqtt.Client()
    # Conexión al broker Mosquitto
    mqtt_client.connect("mosquitto", 1883, 60)
    mqtt_client.loop_start()
    mqtt_client = subscribe_topics(mqtt_client, topics)
    return mqtt_client

def subscribe_topics(mqtt_client, topics):
    # Suscripción a los tópicos deseados
    for topic in topics:        
        mqtt_client.subscribe(topic)
    return mqtt_client
