#! /usr/bin/env python


import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist  


def my_callback(request):
    Empty = EmptyResponse 
    rospy.loginfo("I am in the callback")
    move = Twist()
    rospy.loginfo("My_callback has been called")
    move.angular.z = 1
    pub.publish(move)
    rospy.sleep(2.3)
    rospy.loginfo("the robot is spining ")
    move.angular.z = 0
    rospy.loginfo("the robot is stopping  ")
    pub.publish(move)

    move.linear.x = 0.2
    pub.publish(move)
    rospy.sleep(3)
    move.linear.x = 0
    pub.publish(move)
    Empty.success = True
    return Empty    # the service Response class, in this case EmptyResponse


rospy.init_node('service_server') 
rospy.loginfo("I have just initalized node")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size =1)
rospy.loginfo("I have just started publishing to the cmnd_vel topic")
my_service = rospy.Service('/my_service', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.