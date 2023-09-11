# init.py

import socket

nb = 1  # Choose 0 for one broker, 1 for another
brokers = [str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com')),
           "18.194.176.210"]
ports = ['80', '1883', '1883']
usernames = ['', '', '']  # Modify for your MQTT broker
passwords = ['', '', '']  # Modify for your MQTT broker
broker_ip = brokers[nb]
port = ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0  # 0 stands for endless loop
msg_system = ['normal', 'issue', 'No issue']
wait_time = 5

# Common
conn_time = 0  # 0 stands for endless loop
comm_topic = 'pr/Smart/'
