import tkinter as tk
import paho.mqtt.client as mqtt
import json

class Gui:
    def __init__(self, master, greenhouse_manager):
        self.master = master
        self.master.title("Greenhouse Monitoring GUI")
        self.master.geometry("800x600")
        self.greenhouse_manager = greenhouse_manager

        # Create your GUI elements and widgets here
        self.label = tk.Label(self.master, text="Greenhouse Monitoring System")
        self.label.pack(pady=20)

        self.status_label = tk.Label(self.master, text="Status: Ready")
        self.status_label.pack(pady=10)

        self.temperature_label = tk.Label(self.master, text="Temperature: N/A")
        self.temperature_label.pack(pady=10)

        self.humidity_label = tk.Label(self.master, text="Humidity: N/A")
        self.humidity_label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop Monitoring", command=self.stop_monitoring, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        # Subscribe to MQTT topics
        self.greenhouse_manager.client.subscribe("greenhouse/dht")  # Adjust the MQTT topic as needed

        # Set up the MQTT message callback
        self.greenhouse_manager.client.on_message = self.on_message

    def on_message(self, client, userdata, msg):
        # This method will be called when an MQTT message is received
        if msg.topic == "greenhouse/dht":
            data = json.loads(msg.payload.decode("utf-8"))
            temperature = data.get("temperature")
            humidity = data.get("humidity")

            # Update the data labels with the received values
            self.temperature_label.config(text=f"Temperature: {temperature}°C")
            self.humidity_label.config(text=f"Humidity: {humidity}%")

    def start_monitoring(self):
        # Implement the logic to start monitoring here
        self.greenhouse_manager.start_monitoring()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Monitoring")

    def stop_monitoring(self):
        # Implement the logic to stop monitoring here
        self.greenhouse_manager.stop_monitoring()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Ready")

if __name__ == "__main__":
    root = tk.Tk()
    greenhouse_manager = Manager()  # Create a Manager instance
    gui = Gui(root, greenhouse_manager)
    root.mainloop()
