"""
Disaster Alert Publisher
------------------------
Sends random disaster alerts to MQTT broker.
"""

import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "disaster/alert"
CLIENT_ID = f"publisher_{random.randint(0, 1000)}"

def connect_mqtt():
    client = mqtt.Client(CLIENT_ID)
    client.connect(BROKER, PORT)
    print(f"[Publisher] Connected to broker {BROKER}")
    return client

def publish_alerts(client):
    disasters = ["Earthquake", "Flood", "Cyclone", "Wildfire", "Tsunami"]
    severities = ["Low", "Medium", "High", "Severe"]
    locations = ["Chennai", "Mumbai", "Delhi", "Kolkata", "Hyderabad"]

    while True:
        alert = {
            "type": random.choice(disasters),
            "severity": random.choice(severities),
            "location": random.choice(locations),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        message = json.dumps(alert)
        result = client.publish(TOPIC, message)
        status = result[0]
        if status == 0:
            print(f"[Publisher] Sent `{message}` to topic `{TOPIC}`")
        else:
            print(f"[Publisher] Failed to send message to topic {TOPIC}")
        time.sleep(random.randint(3, 6))

def run():
    client = connect_mqtt()
    publish_alerts(client)

if __name__ == "__main__":
    run()
