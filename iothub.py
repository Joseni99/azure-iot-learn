from azure.iot.device import IoTHubDeviceClient, Message
import json
import time
from sense_hat import SenseHat
import argparse

# Command-line argument parser
parser = argparse.ArgumentParser(description='Azure IoT Hub Client')
parser.add_argument('--connection-string', type=str, help='Azure IoT Hub connection string')
args = parser.parse_args()

# Access the connection string using args.connection_string
connection_string = args.connection_string

# Sense HAT setup
sense = SenseHat()

# Create an IoT Hub client instance
client = IoTHubDeviceClient.create_from_connection_string(connection_string)

# Function to display messages on the Sense HAT screen
def display_message(message):
    sense.show_message(str(message))

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

    # Publish sensor data to Azure IoT Hub
    client.send_message(json.dumps(sensor_data))

def on_c2d_message(message):
    try:
        payload = json.loads(message.data)
        print("Received C2D message: {}".format(payload))

        # Display received data on Sense HAT screen
        display_message(payload.get("msg", None))

    except Exception as e:
        print("Error handling C2D message: {}".format(e))

# Set the C2D message callback
client.on_message_received = on_c2d_message

# Connect to Azure IoT Hub
client.connect()

# Main loop
try:
    while True:
        # Publish sensor data to Azure IoT Hub
        publish_sensor_data(client)

        # Wait for a few seconds before publishing again
        time.sleep(10)

except KeyboardInterrupt:
    print("Script terminated by user.")
    sense.clear()
    client.disconnect()
