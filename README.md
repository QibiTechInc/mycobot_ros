# mycobot_ros 

Modified mycobot_ros pkg for mycobot_pi

This is a forked project of [the official repository](https://github.com/elephantrobotics/mycobot_ros)

Clone the pkg into the rpi's local workspace:
```bash
git clone -b mycobot-pi https://github.com/QibiTechInc/mycobot_ros.git
```
Launch the following to test the system, you should be able to see myCobot in Rviz with a visual interface that by changing the joints value the robot's actual joint state would change
```bash 
roslaunch mycobot_280 simple_gui.launch 
```
