import os
import MySQLdb
import time

# Configuración de MySQL
mysql_host = os.environ.get('MYSQL_HOST', 'mysql')
mysql_port = int(os.environ.get('MYSQL_PORT', 3306))
mysql_user = os.environ.get('MYSQL_USER', 'user')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'password')
mysql_database = os.environ.get('MYSQL_DATABASE', 'mydb')

def connect_to_mysql():
    while True:
        try:
            mysql_client = MySQLdb.connect(host=mysql_host, port=mysql_port, user=mysql_user, passwd=mysql_password, db=mysql_database)
            return mysql_client
        except Exception as e:
            print("Error connecting to MySQL:", e)
            print("Retrying in 5 seconds...")
            time.sleep(5)