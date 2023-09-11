import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker Configuration
broker_address = "3.77.251.252"  # Change this to your MQTT broker
topic = "greenhouse/dht"

# Simulated DHT Sensor
def simulate_dht_sensor():
    client = mqtt.Client()
    client.connect(broker_address)

    while True:
        temperature = random.uniform(20, 30)  # Simulate temperature (20-30°C)
        humidity = random.uniform(40, 60)     # Simulate humidity (40-60%)

        # Create a JSON payload with temperature and humidity
        payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'

        # Publish the data to the MQTT broker
        client.publish(topic, payload)

        print(f"Published: {payload}")
        time.sleep(5)  # Simulate data update every 5 seconds

if __name__ == "__main__":
    try:
        simulate_dht_sensor()
    except KeyboardInterrupt:
        print("Emulator stopped.")
