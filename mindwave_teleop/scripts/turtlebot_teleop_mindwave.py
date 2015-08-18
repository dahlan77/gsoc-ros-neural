#!/usr/bin/env python

import rospy
import roslib

from geometry_msgs.msg import Twist
from mindwave_msgs.msg import Mindwave

M_PI = 3.1415116

class Turtlebot:
    def __init__(self):

        rospy.init_node('turtle_teleop_mindwave', anonymous=True)
        
        self.speed = 0.1 # 0.1 m/s
        self.turn = 1
        self.meditation_threshold = 60
        self.attention_threshold = 25

        self.loop_rate = rospy.Rate(10) # T = 1/10
        
        self.lastvel = Twist()        
        self.sub = rospy.Subscriber('/mindwave', Mindwave, self.mindwaveCallback, queue_size=100)
        self.pub = rospy.Publisher('~cmd_vel', Twist, queue_size=10)    

    def mindwaveCallback(self, msg):
    
        twist = Twist()

        # Go fordward
        if msg.attention >= self.attention_threshold:
            twist.linear.x = self.speed + 1.0/msg.attention # m/s
        else:
            twist.linear.x = 0 

        twist.linear.y = 0 
        twist.linear.z = 0

        # Turn
        if msg.meditation >= self.meditation_threshold:
            twist.angular.z = self.turn + M_PI/msg.meditation
        else:
            twist.angular.z = 0  # no rotation    
        
        self.lastvel = twist

    def run(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.lastvel)
            self.loop_rate.sleep()

if __name__=="__main__":
    try:
        turtle = Turtlebot()
        turtle.run()
        rospy.spin()        
    except rospy.ROSInterruptException, e:
        print str(e)
        pass
