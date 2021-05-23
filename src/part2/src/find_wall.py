#! /usr/bin/env python


import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from sensor_msgs.msg import LaserScan                           # Importing LaserScan from sensor_msgs message to use for subscribing 
from geometry_msgs.msg import Twist  


def my_callback(msg):
    rospy.loginfo("I am in the callback")
    #Empty = EmptyResponse
    move = Twist()
    laserScanMin = msg.range_min
    #rospy.loginfo(laserScanMin)
    turnTill = True 
    
    while turnTill:
        laserScan = msg.ranges
        rospy.loginfo("I am in the loop")
        move.angular.z = 0.2
        pub.publish(move)
        rospy.loginfo(laserScanMin)
        rospy.loginfo(laserScan[0])
        if(laserScan[0] == 0.11999999731779099):
            turnTill = False
            

    rospy.loginfo("I am out the loop")
    move.angular.z = 0
    pub.publish(move)
    

    #move = Twist()
    #rospy.loginfo("My_callback has been called")
    #move.angular.z = 1
    #pub.publish(move)
    #rospy.sleep(2.3)
 

    #Empty.success = True
    #return Empty    # the service Response class, in this case EmptyResponse


rospy.init_node('Wall_Finder') 
rospy.loginfo("I have just initalized node")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size =1)

sub = rospy.Subscriber('/scan', LaserScan, my_callback) #We subscribe to the laser's topic

#rospy.loginfo("I have just started publishing to the cmnd_vel topic")
#my_service = rospy.Service('/wallFinder', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.