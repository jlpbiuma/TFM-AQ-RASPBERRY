import paho.mqtt.client as mqtt
import random
import time
import os

# MQTT broker details
BROKER_ADDRESS = os.environ["BROKER_ADDRES"]
PORT = int(os.environ["BROKER_MQTT_PORT"])
TOPIC_TEMPLATE = os.environ["TOPIC_TEMPLATE"]
TIME_REFRESH = int(os.environ["DATA_FREQUENCY"])

# Connect to the MQTT broker
client = mqtt.Client()
client.connect(BROKER_ADDRESS, PORT)

# Function to generate random data for different topics
def generate_data(index):
    if index == 1:
        # Generate temperature data with mean 25 and std 2.5
        value = random.normalvariate(25, 0.5)
    elif index == 2:
        # Generate humidity data with mean 50 and std 20
        value = random.normalvariate(50, 1)
        # Add persistence to humidity data
    elif index == 3:
        # Generate CO ppm data with mean 25 and std 1
        value = random.normalvariate(25, 0.01)
    else:
        # Invalid topic
        return None
    return value

# Publish data over different topics continuously
while True:
    for i in range(1, 4):
        topic = TOPIC_TEMPLATE + str(i)
        data = generate_data(i)
        if data is not None:
            client.publish(topic, payload=str(data))
            print(f"Published data {data} to topic {topic}")
    time.sleep(TIME_REFRESH)  # Wait for 1 minute before publishing again
