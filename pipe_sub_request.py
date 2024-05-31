import threading
from functions import initialize_mqtt, send_public_ip, on_message

mqtt_client = initialize_mqtt()

# Suscripción a mensajes
mqtt_client.on_message = on_message

# Start the thread to send public IP regularly
public_ip_thread = threading.Thread(target=send_public_ip)
public_ip_thread.daemon = True  # This ensures the thread will close when the main program exits
public_ip_thread.start()

# Mantener el script en ejecución
while True:
    pass