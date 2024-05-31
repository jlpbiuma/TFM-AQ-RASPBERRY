import requests
import os
from datetime import datetime
import time

BACKEND_URL = os.environ["BACKEND_URL"]  # Use os.environ.get() instead of os.environ()
PUBLIC_IP_URL = os.environ["PUBLIC_IP_URL"].replace("ID_ESTACION", os.environ["ID_ESTACION"])

def on_message(client, userdata, msg):
    # Construct JSON payload
    payload = {
        "topic": msg.topic,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Format the timestamp
        "valor": msg.payload.decode("utf-8")  # Convert bytes to string
    }
    try:
        # Send POST request to the backend
        response = requests.post(BACKEND_URL, json=payload)
        # Check if the request was successful
        if response.status_code == 200:
            print("Message sent to backend successfully")
        else:
            print("Failed to send message to backend. Status code:", response.status_code)
    except Exception as e:
        print("Error:", e)
    return 0

# Function to get the public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            return response.json().get('ip')
    except Exception as e:
        print(f"Error getting public IP: {e}")
    return None

# Function to send the public IP address to the backend
def send_public_ip():
    while True:
        public_ip = get_public_ip()
        if public_ip:
            payload = {
                "public_ip": public_ip,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            try:
                response = requests.put(PUBLIC_IP_URL, json=payload)
                if response.status_code == 200:
                    print("Public IP sent to backend successfully")
                else:
                    print("Failed to send public IP to backend. Status code:", response.status_code)
            except Exception as e:
                print(f"Error sending public IP: {e}")
        # Wait for a defined interval before sending the IP again
        time.sleep(3600)  # Send every hour