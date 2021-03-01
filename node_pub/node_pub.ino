#include<arduino.h>
#include<ESP8266WiFi.h>
#include<PubSubClient.h>
#include"config.h"
#include<DHT.h>

//constants
//In Config file

//globals
WiFiClient wificlient;
PubSubClient client(wificlient);
DHT dht(DHTPIN,DHT11);


int soilMoist=100; // dummy 
int temp=0; //dummy

//Wifi connection Function
void wifi_connect()
{
    WiFi.disconnect();
    Serial.printf("Connecting to %s\n",ssid);
    WiFi.begin(ssid,pass);
    while(WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(500);
    }
    Serial.print("\nConnected to ");
    Serial.println(WiFi.localIP());
}
//establishing a recconect and initial
void MQTT_connect()
{
    while(!client.connected())
    {
        Serial.println("Attempting MQTT connection...");
        String clientID="IoTLAB-";
        clientID+=String(random(0xffff),HEX);
        Serial.println(clientID.c_str());
        if(client.connect(clientID.c_str()))
        {
            Serial.println("Connected");
        }
        else
        {
            Serial.print("Failed, rc = ");
            Serial.println(client.state());
            delay(5000);
        }
    }
}
void setup()
{
    Serial.begin(9600);
    wifi_connect();
    client.setServer(mqtt_broker,port);
}
void loop()
{
    if(!client.connected())
        MQTT_connect();
    client.loop();


    //add the code for soil moisture sensor, DHT data acquisation
    //here
    //client.publish("node1/soilMoisture",cstr);
    //client.publish("node1/temp",cstr);


    //dummy code for debug
    char cstr[100];
    itoa(soilMoist,cstr,10);
    client.publish("node1/soilMoisture",cstr);
    itoa(temp,cstr,10);
    client.publish("node1/temp",cstr);
    soilMoist++;
    temp++;

    //optional delay 
    delay(2000);
    
    
}