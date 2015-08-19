#!/usr/bin/env python

import rospy
import roslib
import time

from mindwave_driver.bluetooth_headset import BluetoothHeadset
from mindwave_driver.common import *

from mindwave_msgs.msg import Mindwave

class MindwaveNode:
    """the Ros node for Mindwave message"""

    def __init__(self):
        
        rospy.init_node('mindwave_node', anonymous=True)     
        
        self.addr = rospy.get_param("~addr", None)
        
        if self.addr is not None:
            self.headset = BluetoothHeadset(self.addr)
        else:
            self.headset = BluetoothHeadset()
            self.addr = self.headset.addr

        self.pub = rospy.Publisher('mindwave', Mindwave, queue_size=10)
        
        self.loop_rate = rospy.Rate(10)

        rospy.loginfo("Publishing the ros message for mindwave at addr %s ...", self.addr)

    def update(self):
        """This method publishes the Mindwave ros message

        It publishes the Attention and Meditation values, these are
        the main messages to control robots.
        """

        msg = Mindwave()
        while not rospy.is_shutdown():
           
            if self.headset.status != Status.CONNECTED:
                rospy.loginfo('trying connecting')
                self.headset.connect(headset.addr)
                rospy.sleep(1)             
            else:
                pass
            
            msg.status = self.headset.status
            msg.signal = self.headset.signal
            msg.attention = self.headset.attention
            msg.meditation = self.headset.meditation
      
            #rospy.loginfo(msg)
            self.pub.publish(msg)
            #self.loop_rate.sleep()
            rospy.sleep(0.1)

        self.headset.close()

if __name__ == '__main__':
    try:
        node = MindwaveNode()
        node.update() 
        rospy.spin()
    except rospy.ROSInterruptException, e:
        rospy.logerr(str(e))
        pass