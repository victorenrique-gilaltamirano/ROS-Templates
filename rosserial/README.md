# What is _rosserial_?

Protocol designed to communicate between ROS and Hardware. There are different knd of Hardware available, Arduino, STM32, Raspberry Pi, etc. It allows the new electronic hardware to directly talk to ROS system. Without need to develop custom drivers and comm protocols.

_rosserial_ is a protocol for wrapping standard ROS serialized messages and multiplexing multiple topics and services over a serial port or network socket.

- **rosserial_client** is the generic client-side _rosserial_ implementation. It is designed for microcontrollers and it can run on any processor having an ANSI C++ compiler and a serial port connection to a computer running ROS. Other client libraries are:
- **rosserial_arduino**
- **rosserial_mbed**
- rosserial_embeddedlinux
- rosserial_windows
- rosserial_tivac
- rosserial_stm32
- rosserial_teensy
- etc.

On the ROS-side it is recommended to have the following interfaces:
- **rosserial_python**: a Python-based implementation.
- **rosserial_server**: a C++ implementation, with some more limitations than _rosserial_python_ but recommended for high-performance applications.

While connecting hardware, we need to ALWAYS be running a node (**rosserial_python** or rosserial_server) to make the interface between microcontroller and ROS ecosystem.

Microcontroller can behave as publisher, subscriber, etc.

# Using Arduino with ROS

Step 1. Download/Install Arduino IDE.

Step 2. Install rosserial for arduino by typing in a new terminal (Kinetic, for example):
```
$ sudo apt-get install ros-kinetic-rosserial-arduino
$ sudo apt-get install ros-kinetic-rosserial
```
with the installations above, now we have access to **rosserial_python** node.

Step 3. Considering that You are programming with Arduino IDE in Linux Ubuntu, go to Arduino sketchbook folder (arduino-1.8.6, for example) as:
```
$  cd arduino-1.8.6/libraries
$  rm -rf ros_lib
$  rosrun rosserial_arduino make_libraries.py
```

NOTE: If programming Arduino in Windows, open Arduino IDE - Manage Libraries - search for `Rosserial Arduino Library` by Michael Ferguson, and install.

Now examples for ROS should appear in the examples section.

Check for Templates of ROS Nodes written in Arduino in the following repository [link](https://github.com/victorenrique-gilaltamirano/ROS-Templates/tree/main/rosserial/arduino).

Application logic should be inside the `void loop()` method

# Using Mbed board with ROS

For the ONLINE Compiler, simply import the rosserial_mbed library to your online compiler account using the following link:
```
$ https://developer.mbed.org/users/garyservin/code/ros_lib_noetic/
```

NOTE:
In order to use the rosserial libraries in your own code, you must first put
```
#include <ros.h>
```
prior to including any other header files, e.g.
```
#include <std_msgs/String.h>
```
