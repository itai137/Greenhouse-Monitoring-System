import tkinter as tk
import subprocess  # Add this line to import subprocess
from manager import Manager
from gui import Gui

def main():
    # Replace '3.77.251.252' with the actual IP address of your MQTT broker
    broker_ip = '3.77.251.252'

    # Create a Manager instance with the broker IP
    greenhouse_manager = Manager(broker_ip)

    # Start the DHT emulator using subprocess
    emulator_process = subprocess.Popen(["python", "DHT_emulator.py"])

    # Create a Tkinter root window
    root = tk.Tk()
    root.title("Greenhouse Monitoring System")

    # Create the GUI and pass the manager instance
    app = Gui(root, greenhouse_manager)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
