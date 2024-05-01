import os
from influxdb import InfluxDBClient
import time

# Configuración de InfluxDB
influxdb_host = os.environ.get('INFLUXDB_HOST', 'influxdb')
influxdb_port = int(os.environ.get('INFLUXDB_PORT', 8086))
influxdb_user = os.environ.get('INFLUXDB_USER', 'user')
influxdb_password = os.environ.get('INFLUXDB_PASSWORD', 'password')
influxdb_database = os.environ.get('INFLUXDB_DATABASE', 'mydb')

# Función para conectar a InfluxDB con reintentos
def connect_to_influxdb():
    while True:
        try:
            influxdb_client = InfluxDBClient(host=influxdb_host, port=influxdb_port, username=influxdb_user, password=influxdb_password, database=influxdb_database)
            return influxdb_client
        except Exception as e:
            print("Error connecting to InfluxDB:", e)
            print("Retrying in 5 seconds...")
            time.sleep(5)