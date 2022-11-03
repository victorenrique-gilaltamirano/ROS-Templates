# Create new action definition

For creating a new srv definition, we use primitive data types. Consult http://wiki.ros.org/msg

1. (skip if already done for msg) Create a package only for messages and service definitions, with `$ catkin_create_pkg my_robot_msgs roscpp rospy std_msgs`
2. (skip if already done for msg) Remove "include" folder with `$ rm -rf include/`
3. (skip if already done for msg) Remove "src" folder with `$ rm -rf src/`
We only need `CMakeLists.txt` and `package.xml`

4. Add in `package.xml`:
```
<build_depend>message_generation</build_depend>

<exec_depend>message_runtime</exec_depend>

<depend>action_lib</depend>
```

5. Add in `CMakeLists.txt`:
```
find_package(
...
message_generation
actionlib_msgs
)
```

```
generate_messages(
...
std_msgs
actionlib_msgs
)
```

```
catkin_package(
...
CATKIN_DEPENDS roscpp rospy std_msgs message_runtime actionlib_msgs
)
```

6. Make a folder for srv definitions `$ mkdir action`, containing a file, for example `$ touch CountUntil.action`:


```
#goal
int64 max_number
float64 wait_duration
---
int64 count
---
float64 percentage
```


7. Add this new file into the `CMakeLists.txt`:

```
add_action_files(
  FILES
  CountUntil.action
)
```

8. Compile everything with `$ catkin_make`
