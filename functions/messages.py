import requests
import os

BACKEND_URL = os.environ["BACKEND_URL"]  # Use os.environ.get() instead of os.environ()
TOPIC_1 = os.environ["TOPIC_1"]

def on_message(client, userdata, msg):
    print(client, userdata, msg)
    print("Hello world!")
    # Construct JSON payload
    payload = {
        "topic": TOPIC_1,
        "message": msg.payload.decode("utf-8")  # Convert bytes to string
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
