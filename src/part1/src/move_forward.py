#! /usr/bin/env python

import rospy                                                    # Importing rospy    
from sensor_msgs.msg import LaserScan                           # Importing LaserScan from sensor_msgs message to use for subscribing 
from geometry_msgs.msg import Twist  

    
    
    #print(list[0], " this is what the tobot sees on its backwards [0] ")
    #print(list[90], " this is what the tobot sees on its right side [90] ")
    #print(list[180], " this is what the robot sees front [180]")
    #print(list[270],  " this is what the robot sees to its left [270]")
    

def callback(msg):       
    print("I am at the beining of the loop")
    move = Twist()
    list = msg.ranges 
    
    print(list[90], " this is what the tobot sees on its right side [90] ")
    print(list[180], " this is what the robot sees front [180]")
    
        
    if(list[90] > 0.3):
        rospy.loginfo("the robot is too far away from the wall turning right")
        move.linear.x = 0.1
        move.angular.z = 0.1

    if(list[90] < 0.2):
        rospy.loginfo("the robot is too close from the wall turning left")
        move.linear.x = 0.1
        move.angular.z = -0.1

    if(list[90] < 0.3 and list[90] > 0.2 ):
        rospy.loginfo("the robot is moving straight")
        move.linear.x = 0.1
        move.angular.z = 0

    if(list[180] < 0.4):
        rospy.loginfo("wall detected turning ")
        move.linear.x = 0
        move.angular.z = 0.5

   
    pub.publish(move)

    


rospy.init_node("topic_publisher")
rate = rospy.Rate(1)



while not rospy.is_shutdown():
    sub = rospy.Subscriber('/scan', LaserScan, callback) #We subscribe to the laser's topic
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size =1)
    rate.sleep()