#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
mgstosend=0

#def callback():
#    global msgtosend
#    rospy.loginfo(msgtosend)

def talker():
    global mgstosend
    pub = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)
#    rospy.Subscriber('/robot/joint2_position_controller/goalpos', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.25) # 10hz
    temp=0.0
    while not rospy.is_shutdown():
	if temp==0:
	    msgtosend=1
	    temp=1
	    pub.publish(msgtosend)
	    rospy.loginfo(msgtosend)
	else:
	    msgtosend=0
	    temp=0
	    pub.publish(msgtosend)
	    rospy.loginfo(msgtosend)
#	rospy.Subscriber('/robot/joint2_position_controller/goalpos', Float64, callback)
	
	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
