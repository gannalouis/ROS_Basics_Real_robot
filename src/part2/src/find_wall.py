#! /usr/bin/env python
import rospy
from part2.srv import findWall, findWallRequest
#import part2.srv
#from sensor_msgs.msg import LaserScan                           # Importing LaserScan from sensor_msgs message to use for subscribing 
#from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
#from geometry_msgs.msg import Twist  


#def my_callback(request):
#    Empty = findWallResponse 
#    rospy.loginfo("I am in the call back")
#    Empty.findWall = True
#    return Empty    # the service Response class, in this case EmptyResponse


rospy.init_node('find_wall_node') 
rospy.loginfo("I have just initalized node")
#pub = rospy.Publisher("/cmd_vel", Twist, queue_size =1)
#rospy.loginfo("I have just started publishing to the cmnd_vel topic")
my_service = rospy.Service('/findWall', findWall , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.