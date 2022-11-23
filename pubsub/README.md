# Create new msg definition

For creating a new msg definition, we use primitive data types. Consult http://wiki.ros.org/msg

1. Create a package only for messages and service definitions, with `$ catkin_create_pkg my_robot_msgs roscpp rospy std_msgs`
2. Remove "include" folder with `$ rm -rf include/`
3. Remove "src" folder with `$ rm -rf src/`
We only need `CMakeLists.txt` and `package.xml`

4. Add in `package.xml`:

```
<build_depend>message_generation</build_depend>
...
<exec_depend>message_runtime</exec_depend>
```

5. Add in `CMakeLists.txt`:

```
find_package(
...
message_generation
)
```


```
generate_messages(
...
std_msgs
)
```


```
catkin_package(
...
CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
)
```

6. Make a folder for msg definitions `$ mkdir msg`, containing a file, for example `$ touch HardwareStatus.msg`:

```
int64 temperature

bool are_motors_up

string message
```


7. Add this new file into the `CMakeLists.txt`:

```
add_message_files)
  FILES

  HardwareStatus.msg
)
```

8. Compile everything with `$ catkin_make`

# Common Practices to write _Publisher_ in ROS

Step 1. Determine a name for the topic to publish.

Step 2. Determine the type of the messages that the topic will publish.

Step 3. Determine the frequency of topic publication (how many messages per second).

Step 4. Create a Publisher object with parameters chosen.

Step 5. Keep publishing the topic message at the selected frequency.

# Common Practices to write _Subscriber_ in ROS

Step 1. Identify the name for the topic to listen to.

Step 2. Identify the type of the message to be received.

Step 3. Define a _callback_ function that will automatically execute when a new message is received on the topic.

Step 4. Start listening for the topic messages.

Step 5. Spin to listen forever (in C++ and Python).
