import paho.mqtt.client as mqtt
import time
import random

# MQTT Broker Configuration
broker_address = "3.77.251.252"  # Change this to your MQTT broker
topic = "greenhouse/button"

# Simulated Button Emulator
def simulate_button():
    client = mqtt.Client()
    client.connect(broker_address)

    while True:
        # Simulate button press (True) and release (False)
        is_pressed = random.choice([True, False])

        # Send button state to the MQTT broker
        client.publish(topic, str(is_pressed))

        print(f"Button State: {'Pressed' if is_pressed else 'Released'}")
        time.sleep(3)  # Simulate button state change every 3 seconds

if __name__ == "__main__":
    try:
        simulate_button()
    except KeyboardInterrupt:
        print("Emulator stopped.")
