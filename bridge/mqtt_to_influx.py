import json
import requests
import paho.mqtt.client as mqtt

MQTT_BROKER = "<MQTT_BROKER_IP>"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensors"

INFLUX_URL = "http://<INFLUXDB_IP>:8086/write?db=iot"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print("Connection failed:", rc)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        temperature = float(data.get("temperature", 0))
        humidity = float(data.get("humidity", 0))
        distance = float(data.get("distance", 0))
        voltage = float(data.get("voltage", 0))

        line = f"sensors temperature={temperature},humidity={humidity},distance={distance},voltage={voltage}"

        response = requests.post(INFLUX_URL, data=line)

        if response.status_code == 204:
            print("Saved to InfluxDB")
        else:
            print("InfluxDB error:", response.text)

    except Exception as e:
        print("Error:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Bridge started...")

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
