from sense_hat import SenseHat
import json
import time
import paho.mqtt.client as mqtt
import argparse


parser = argparse.ArgumentParser(description='My script with options')

parser.add_argument('--broker', type=str, help='broker address')
parser.add_argument('--topic1', type=str, help='topic2publish')
parser.add_argument('--topic2', type=str, help='topic2subscribe')

args = parser.parse_args()

# Access the values using args.option1 and args.option2
broker_address = args.broker
publish_topic = args.topic1
subscribe_topic = args.topic2

# Sense HAT setup
sense = SenseHat()

# MQTT callback when a message is received
def on_message(client, userdata, msg):
    try:
        # Decode the received message payload
        payload = json.loads(msg.payload.decode('utf-8'))
        print("Received message: {}".format(payload))

        # Display received data on Sense HAT screen
        display_message(payload.get("msg", None))

    except Exception as e:
        print("Error decoding message: {}".format(e))

# Function to publish sensor data as JSON to the specified topic
def publish_sensor_data(client):
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    sensor_data = {
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    }

    # Publish sensor data to the MQTT topic
    client.publish(publish_topic, json.dumps(sensor_data))

# Function to display messages on the Sense HAT screen
def display_message(message):
    sense.show_message(str(message))

# Set up MQTT client and callbacks
client = mqtt.Client()
client.on_message = on_message

# Connect to the HiveMQ broker
client.connect(broker_address, 1883, 60)

# Subscribe to the specified topic for receiving messages
client.subscribe(subscribe_topic)

# Main loop

try:
    while True:
        # Publish sensor data to the MQTT topic
        publish_sensor_data(client)

        # Listen for incoming messages
        client.loop()

        # Wait for a few seconds before publishing again
        time.sleep(2)

except KeyboardInterrupt:
    print("Script terminated by user.")
    sense.clear()
    client.disconnect()
