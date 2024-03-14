# Hands-on LAB: IoT Practice part 1

## Study Case

**Scenario:** A company is planning to transmit IoT data, such as temperature, humidity, and other sensor readings, via MQTT (Message Queuing Telemetry Transport) with a public broker. The objective is to ensure reliable transmission of IoT data from IoT devices deployed in various locations to a centralized system for analysis and monitoring,

The idea is to set up a Raspberry PI to send this data but the company also want privacy for some cases so they want also to deploy their own MQTT server in Azure.

**Tasks:**

**PART 1:** **Public MQTT**

1. Set up the raspberry to recerive and send telemetry data via MQTT.

2. Use a public MQTT broker as HIVEMQ.

3. Use MQTTX to send and receive data in the computer.

**PART 2: Private MQTT**

    1. Set up a Virtual Network.

    2. Launch a Virtual Machine.

    3. Install mosquitto broker.

    4. Modify the NSGs.

    5. Use MQTTX to send and receive data in the computer.

## PART 1: Public MQTT

### Set up the raspberry PI

1. Download the Pi Imager tool and plug the micro sd card to install a O.S.

<img title="" src="../img/rasp%20(2).png" alt="rasp (2).png" width="476">

2. After selecting the device and the O.S click on edit settings after clicking next.

<img title="" src="../img/rasp%20(3).png" alt="rasp (3).png" width="475">

3. Here some key parts, set a User and a Password and write it down, also configure the Wireless LAN configuration.

<img title="" src="../img/rasp%20(4).png" alt="rasp (4).png" width="375">

4. Allow SSH in services to remote access the raspberry PI and click save.

<img title="" src="../img/rasp%20(5).png" alt="rasp (5).png" width="374">

5. Click on YES and wait to finish.

<img title="" src="../img/rasp%20(6).png" alt="rasp (6).png" width="472">

6. Identify yout IP address and SSH into the Raspberry PI

<img src="../img/rasp%20(7).png" title="" alt="rasp (7).png" width="565">



<img title="" src="../img/mqttx.png" alt="mqttx.png" width="699">
