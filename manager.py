import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime
from init import comm_topic  # Add this import statement


# Define the MQTT broker IP and port
broker_ip = "3.77.251.252"  # Change this to your MQTT broker IP
port = 1883  # Change this to your MQTT broker port

class Manager:
    def __init__(self, broker_ip):
        self.broker_ip = broker_ip  # Store the broker IP
        self.conn_time = 0
        self.manag_time = 0
        self.client = self.client_init("Manager-", self.broker_ip)

    def on_log(self, client, userdata, level, buf):
        print("log: " + buf)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully")
        else:
            print("Bad connection. Returned code =", rc)

    def on_disconnect(self, client, userdata, flags, rc=0):
        print("Disconnected. Result code " + str(rc))

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        m_decode = str(msg.payload.decode("utf-8", "ignore"))
        print("Message from:", topic, m_decode)

    def send_msg(self, topic, message):
        print("Sending message:", message)
        self.client.publish(topic, message)

    def client_init(self, client_id, broker_ip):
        r = random.randrange(1, 10000000)
        ID = str(client_id + str(r + 21))
        client = mqtt.Client(ID, clean_session=True)

        # Define callback functions
        client.on_connect = self.on_connect
        client.on_disconnect = self.on_disconnect
        client.on_log = self.on_log
        client.on_message = self.on_message

        print("Connecting to broker", broker_ip)
        client.connect(broker_ip, int(port))

        return client

    def start_monitoring(self):
        # Implement the logic to start monitoring here
        pass  # Add your logic here

    def stop_monitoring(self):
        # Implement the logic to stop monitoring here
        pass  # Add your logic here

    def main(self):
        # Main monitoring loop
        self.client.loop_start()
        self.client.subscribe(comm_topic + '#')

        try:
            while self.conn_time == 0:
                # Replace this with your logic for monitoring and managing data
                print("Monitoring...")
                time.sleep(self.conn_time + self.manag_time)
                # Replace this with your logic for checking data and sending alerts
                print("Checking data...")
                time.sleep(3)

            print("Connection time ending")

        except KeyboardInterrupt:
            self.client.disconnect()
            print("Interrupted by keyboard")

        self.client.loop_stop()
        self.client.disconnect()
        print("End manager run script")

if __name__ == "__main__":
    broker_ip = '3.77.251.252'  # Replace with your broker IP
    manager = Manager(broker_ip)
    manager.main()
