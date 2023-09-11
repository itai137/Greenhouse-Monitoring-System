import paho.mqtt.client as mqtt
import time

# MQTT Broker Configuration
broker_address = "3.77.251.252"  # Change this to your MQTT broker
topic = "greenhouse/relay"

# Simulated Relay Emulator
def on_message(client, userdata, message):
    # Toggle the relay state when a message is received
    if message.payload.decode() == "toggle":
        # Implement your logic here to control a relay or digital output
        # For this example, we'll just print the state change
        print("Relay Toggled")

def simulate_relay():
    client = mqtt.Client()
    client.connect(broker_address)
    client.subscribe(topic)

    client.on_message = on_message

    while True:
        client.loop()
        time.sleep(1)  # Adjust the sleep interval as needed

if __name__ == "__main__":
    try:
        simulate_relay()
    except KeyboardInterrupt:
        print("Emulator stopped.")
