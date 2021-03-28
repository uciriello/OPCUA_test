from opcua import Server
from random import randint
import datetime
import time

server = Server()

url = "opc.tcp://localhost:4840"
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node  = server.get_objects_node()

Param = node.add_object(addspace, "parametres")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
CurentTime = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
CurentTime.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    Temperature = randint(10,50)
    Pressure = randint(200,999)
    NOW = datetime.datetime.now()

    print(Temperature, Pressure, NOW)
    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    CurentTime.set_value(NOW)

    time.sleep(0.1)