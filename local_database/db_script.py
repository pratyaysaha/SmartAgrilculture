import paho.mqtt.client as mqtt
import pymongo as mongo

broker_address="192.168.0.58"
port=1882
username="pratyay"
password="26324926"
connection_string="mongodb://192.168.0.58:1990/"

dbclient=mongo.MongoClient(connection_string)
db=dbclient["AgrilData"]
col=db["allData"]



def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    client.subscribe("node1/soilMoisture")
    client.subscribe("node1/temp")

def on_message(client,userdata,msg):
    print("Message ["+msg.topic+"] : "+str(msg.payload))
    new_dict={"sensor": msg.topic , "data" : msg.payload}
    col.insert_one(new_dict)

client=mqtt.Client("IOT-LAB_PI_DB")
client.connect(broker_address,port)
client.on_connect=on_connect
client.on_message=on_message
client.loop_forever()

