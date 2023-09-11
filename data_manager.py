import paho.mqtt.client as mqtt
import sqlite3
import json
from datetime import datetime

# MQTT Broker Configuration
broker_address = "3.77.251.252"  # Change this to your MQTT broker
topic_prefix = "greenhouse/"

# Database Configuration
db_name = 'data/homedata_05_2.db'

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_data(conn, data):
    sql = ''' INSERT INTO data(timestamp, name, value)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT broker")
        client.subscribe(topic_prefix + "#")
    else:
        print(f"Bad connection. Returned code = {rc}")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")

    print(f"Received message from {topic}: {payload}")

    # Process the received message (modify this part based on your project's requirements)
    try:
        data = json.loads(payload)
        name = data.get("name", "")
        value = data.get("value", "")
        if name and value:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            conn = create_connection(db_name)
            if conn is not None:
                insert_data(conn, (timestamp, name, value))
                conn.close()
    except json.JSONDecodeError:
        print("Received non-JSON message. Ignoring...")
    except Exception as e:
        print(f"Error processing message: {e}")



if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    print(f"Connecting to MQTT broker: {broker_address}")
    client.connect(broker_address)

    print(f"Using local database: {db_name}")
    create_table(create_connection(db_name), '''
        CREATE TABLE IF NOT EXISTS data (
            id integer PRIMARY KEY AUTOINCREMENT,
            timestamp text NOT NULL,
            name text NOT NULL,
            value real NOT NULL
        );''')

    client.loop_forever()
