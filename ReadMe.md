# Smart Agriculture Project



## Abstract 

Agriculture contributes about 17% of India's GDP where the 70% rural population depends on it. With old farming practices, the natural resources like water upon which agriculture depends are used injudiciously. More and more use of fertilizers and pesticides has caused a decrease in the quality of food. Irregular rainfall and wind pattern and sudden change in climatic conditions affects the crop in a negative way. So this project aims at creating a decision system along with an early warning system to support agriculture in a more precision fashion. 

## Introduction

Smart Agriculture Project is an umbrella project that consists of a smart  irrigation system, crop health detection with existing Normalised Difference    Vegetation Index (NDVI), a pest infestation warning system. The field is to be    divided into grids. Each grid provides the information about crop health and soil   health. 

### Smart Irrigation System 
The loss of water in crops is mainly caused by evaporation from soil surface and transpiration loss from the leaf surface. These two losses together is called evapotranspiration loss. This loss of water can be met up by natural watering (rainfall) or by irrigation. Irrigation is providing water to crops artificially from sources like rivers, lakes, canals and underground water. Irrigation depends upon various factors like present weather conditions with temperature, rainfall, humidity,  the amount of sunlight falling on the soil and crop canopy cover. With existing framing practices, all the factors were impossible to be implemented due to lack of knowledge to the farmers. 
This project aims at creating a decision system incorporating the factors through various sensors.
### Crop Health Detection 
The crop health is an essential parameter to know what stages of growth the crop is and how is the health of the crop at that stage. Crop health is assessed with the use of hyperspectral imaging by several vegetation indices like NDVI and EVI . The images are processed into a number and that number states the crop health in accordance with the index. This project uses NDVI. It is a simple graphical tool that uses the Near Infrared and Red spectrum. The index is provided below. 

![Image of NDVI Values](https://phenospex.com/wp-content/uploads/2019/10/plants.png)

### Pest infestation warning and alert
-----To be Provided ----------
## Basic Concepts and Technology

### Smart Irrigation System 	
#### Sensors used : 
- `Capacitive soil moisture sensor` : It is an analog sensor that uses capacitors to store charges when in contact with moist substance. The amount of charging is proportional to the amount of water present in the soil. 
- `Photoresistors` : Commonly called Light Dependent Resistors (LDR) is an analog sensor. The analog value is proportional to the amount of light (luminance). 
- `DHT sensor` : A humidity and temperature sensor (DHT-11/22) is a digital sensor that provides information about the humidity and temperature of a surroundings. 

#### Integration :
All the sensors are connected to a ESP8266 development board called NodeMCU through wiring. 

#### Architecture used :
The data sensed by the sensors are transmitted to a Raspberry Pi (a local server and itself a development board) by a Wireless Network ( WiFi ) using [Message Queueing Telemetry Transport (MQTT)](https://mqtt.org/) from the NodeMCU. The MQTT broker used is a local broker called [Mosquitto](https://mosquitto.org/).The topics were created in the nomenclature of “_gridNumber_/_sensorName_”. 
For future study of the data and reference, the data collected in real time by the sensors are stored in a local NoSQL database using [MongoDB](https://www.mongodb.com/). A python script is daemoned into the Raspberry Pi for the purpose.

Data interpretation and decision making :

--------------------------  to be done  ------------------------------------
	

### Crop Health Detection 
	

