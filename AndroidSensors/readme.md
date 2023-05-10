# Description

Android device will publish via TCP/IP the sensor reading of android phone to a web server.

# Requirements

1. Download the Android App "Sensor Stream" from https://play.google.com/store/apps/details?id=com.sensorsensei&hl=en_US . developed by Priyankar Kumar.
2. Pip install the following python packages:
- `pip install asyncio`
- `pip install Wave`
- `pip install websockets`
3. Sample code is provided in `server.py`. Do NOT run in Jupyter Notebook or Lab, recommended to run in Visual Studio Code.

## To use the APP

1. Make sure both your phone and the laptop/raspi/other device are on same network.
2. Find the internal ip address of the raspi/laptop. The server should be showing you the same.
3. Simply type the ip address:5000. Example: `192.168.1.24:5000` in the app's input bar.
*NOTE: click on your Start Menu and type `cmd` in the search box and press enter. A black and white window will open where you will type `ipconfig /all` and press enter. Your ip address will be the IPv4 address.*
4. Switch on whatever sensor's data you want to stream.

## Cheat Sheet for sensor data
- Accelerometer: x,y,z
- Gyroscope: x,y,z
- Magnetometer: x,y,z
- Orientation: azimuth,pitch,roll
- Step Counter: steps
- Thermometer: temperature
- Light Sensor: light
- Proximity: isNear, value, maxRange
- Link: https://github.com/kprimice/react-native-sensor-manager
- Camera and Audio: base64 encoded strings

## Covnert JSON string into Python Dictionary
Data from phone is a strring of the form:

`{"SensorName":"Accelerometer","Timestamp":1683713060748,"x":"-0.4546051025390625","y":"3.2190704345703125","z":"9.168655395507812","payload":""}`

In order to transform this string into an usable dictionary object for python, the following example is given:

```
# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json
 
# initializing string
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
 
# printing original string
print("The original string : " + str(test_string))
 
# using json.loads()
# convert dictionary string to dictionary
res = json.loads(test_string)
 
# print result
print("The converted dictionary : " + str(res))
```

# References

`https://github.com/priyankark/SensorStreamServer`

