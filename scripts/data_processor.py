from functions import *

# Conexión a InfluxDB
influxdb_client = connect_to_influxdb()

# Conexión a MySQL
mysql_client = connect_to_mysql()

# Conexión a Mosquitto
TOPICS = ["topic1", "topic2"]
mqtt_client = initialize_mqtt(TOPICS)

# Suscripción a mensajes
mqtt_client.on_message = on_message

# Mantener el script en ejecución
while True:
    pass
