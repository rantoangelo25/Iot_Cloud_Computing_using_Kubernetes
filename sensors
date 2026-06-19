import json
import random
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = "<MQTT_BROKER_IP>"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensors"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Sensor simulator started...")

while True:
    data = {
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "distance": round(random.uniform(5, 200), 2),
        "voltage": round(random.uniform(3.0, 5.0), 2)
    }

    client.publish(MQTT_TOPIC, json.dumps(data))
    print("SENT:", data)

    time.sleep(2)
