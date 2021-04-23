from opcua import Client
import paho.mqtt.client as mqtt
import time
import json

url = "opc.tcp://192.168.1.17:4840"
client = Client(url)
client.connect()
print("OPC UA Client connected")

iot_hub = "demo.thingsboard.io"
port = 1883
username = "whohDlx7wkEXXuoWim6Y"  
password = ""
topic = "v1/devices/me/telemetry"

iot_hub_client = mqtt.Client()
iot_hub_client.username_pw_set(username, password)
iot_hub_client.connect(iot_hub, port)
print("Connected to IOT hub")

data = dict()
while True:
    try:
        temp = client.get_node("ns=2;i=2")
        press = client.get_node("ns=2;i=3")
        temperature = temp.get_value()
        pressure = press.get_value()
        print(temperature, pressure)

        data["temperature"] = int(temperature)
        data["pressure"] = int(pressure)
        data_out = json.dumps(data)
        iot_hub_client.publish(topic, data_out, 0)

        time.sleep(2)
    except Exception as e:
        print(e)