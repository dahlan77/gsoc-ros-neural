# gsoc-ros-neural
Repository for the GSOC 2015 Neural Interfaces for ROS project, sponsored by OSRF.

### Student Info ###
* Student Name: Steve Ataucuri Cruz
* Organization: Open Source Robotics Foundation
* Mentor's name: Jackie Kay, Esteve Fernandez
* Project title: Neural Interfaces for ROS/Gazebo project
* Project link: http://www.google-melange.com/gsoc/project/details/google/gsoc2015/stonescenter/5878405773918208
* Additional information: stonescenter.wordpress.com
* Wiki page: You can see additional info at [Wiki](https://github.com/jacquelinekay/gsoc-ros-neural/wiki/GSoC-2015-Steve-Ataucuri)

### What is this repository for? ###
  
The main goal of this project is create a ros package, driver plugin library and virtual sensors to be used into Gazebo context which will be able to communicate with The Mindwave device to ROS 

#### Dependencies ####
In order to be able to run the nodes, it is necessary, at first, clone or install some packages:
* apt-get install libbluetooth-dev
* pip install pyserial
* pip install pybluez
* If you use python 2.7 install : pip install enum34

#### Summary of set up ####


### What contain folders? ###

* **mindwave_driver:** driver of Mindwave and files of the node
* **mindwave_teleop:** package to start teleop the turtlebot robot into Gazebo
* **mindwave_msgs:** a share ros message to nodes

### Contacts ###

Steve Ataucuri: lord.ataucuri@ucsp.edu.pe
