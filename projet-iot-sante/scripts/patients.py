import paho.mqtt.client as mqtt
import random
import time
import json

# Broker MQTT (Docker local)
BROKER = "localhost"
PORT = 1883

# Création client MQTT
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Fonction de génération de données réalistes
def generate_data(patient_id):
    return {
        "patient_id": patient_id,
        "bpm": random.randint(60, 120),
        "temperature": round(random.uniform(36.0, 39.0), 1),
        "spo2": random.randint(92, 100),
        "tension": f"{random.randint(11, 14)}/{random.randint(7, 9)}"
    }

patients = [
    "patient1",
    "patient2",
    "patient3",
    "patient4",
    "patient5"
]

print("🚑 Simulation des patients démarrée...")

while True:
    for p in patients:
        topic = f"hospital/{p}"
        data = generate_data(p)

        payload = json.dumps(data)

        client.publish(topic, payload)

        print(f"📤 {topic} -> {payload}")

        time.sleep(2)