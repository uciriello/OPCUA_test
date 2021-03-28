from opcua import Client
import time

url = "opc.tcp://localhost:4840"

client = Client(url)

client.connect()
print("Client Connected")

while True:
    TempNode = client.get_node("ns=2;i=2")
    Temperature = TempNode.get_value()
    print(Temperature)

    PressNode = client.get_node("ns=2;i=3")
    Pressure = PressNode.get_value()
    print(Pressure)

    TimeNode = client.get_node("ns=2;i=4")
    CurrentTime = TimeNode.get_value()
    print(CurrentTime)

    time.sleep(0.1)