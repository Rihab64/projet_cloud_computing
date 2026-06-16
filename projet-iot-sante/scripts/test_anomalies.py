import paho.mqtt.client as mqtt
import json
import time

BROKER = "localhost"
PORT = 1883

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Anomalies à tester
anomalies = [
    {
        "patient_id": "patient1",
        "heart_rate": 140,        # BPM > 120 ⚠️
        "temperature": 37.0,
        "spo2": 98,
        "blood_pressure": 120
    },
    {
        "patient_id": "patient2",
        "heart_rate": 75,
        "temperature": 39.0,      # Température > 38.5 ⚠️
        "spo2": 98,
        "blood_pressure": 110
    },
    {
        "patient_id": "patient3",
        "heart_rate": 80,
        "temperature": 37.0,
        "spo2": 88,               # SpO2 < 92 ⚠️
        "blood_pressure": 115
    },
    {
        "patient_id": "patient4",
        "heart_rate": 40,         # BPM < 50 ⚠️
        "temperature": 37.0,
        "spo2": 96,
        "blood_pressure": 100
    }
]

print("Envoi des anomalies...")

for anomalie in anomalies:
    topic = f"hospital/{anomalie['patient_id']}"
    client.publish(topic, json.dumps(anomalie))
    print(f"✅ Envoi anomalie → {topic} : {anomalie}")
    time.sleep(2)
