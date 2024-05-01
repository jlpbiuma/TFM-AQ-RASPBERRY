
def on_message(client, userdata, msg):
    print(client, userdata, msg)
    print("Hello world!")
    # Save into influxdb and mysql
    return 0
