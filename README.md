# ROS-Templates

## Templates Collection for ROS Nodes

Collection of templates for writing ROS Nodes with properties of publihser, subscriber, service server, service client, action server, action client in C++ and Python.

Content includes general info about using OpenCV in ROS, and connecting hardware such as Arduino or Mbed supported boards with ROS via serial communication.

# Executables

## Executable node for Python nodes
1. Go to the directory conatining the `*.py` script, and type in terminal:
```
$ chmod +x <nodeFilename>.py
```

## Executable for C++ nodes
1. Open CMakeLists.txt file where the `scr/<nodeFilename>.cpp` scr node is located.
2. Add the following lines:
```
add_executable(<node_name> src/<nodeFilename>.cpp)   ## assign nodename to the src file
target_link_libraries(<node_name> ${catkin_LIBRARIES})  # use the assigned nodename
```
3. Compile with `$ catkin_make`.

Repository is updated periodcally!
