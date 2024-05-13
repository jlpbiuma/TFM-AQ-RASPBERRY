from functions import *

mqtt_client = initialize_mqtt()

# Suscripción a mensajes
mqtt_client.on_message = on_message

# Mantener el script en ejecución
while True:
    pass
