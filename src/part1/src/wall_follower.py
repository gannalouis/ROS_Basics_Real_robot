#! /usr/bin/env python



import rospy                                                    # Importing rospy    
from sensor_msgs.msg import LaserScan                           # Importing LaserScan from sensor_msgs message to use for subscribing 
from geometry_msgs.msg import Twist                             # Importing Twist message to publish messages to the topic /cmd_vel


def callback(msg):     
    print("I am in the call back funciton")
                                         # Messages are received, callback is invoked with the message as the first argument. 
    list = msg.ranges                                           # Creating an list from the selectd portion of the array 
    directions.angular.z = 1
    directions.linear.x = 1
    

    pub.publish(directions)                                     # Using the publisher, values are assigned to the Twist message and then published 
    print("I have sucessfullt published the new values ")
    '''
    if list[360] > 1:                                           # Cases /// need to make sure that robot position is reset after each case     
        print("robot is moving forward - no wall detected ")
        directions.angular.z = 0
        directions.linear.x = 0.25
    if list[360] < 1:
        print("wall detected! - will turn left")
        directions.linear.x = 0
        directions.angular.z = 0.25
    if list[719] < 1:
        print("robot will turn left")
        directions.linear.x = 0
        directions.angular.z = -0.25
    if list[0] < 1:
        print("robot will turn right")
        directions.linear.x = 0
        directions.angular.z = 0.25
    '''


while not rospy.is_shutdown():                                  # Create a loop that will go until someone stops the program execution
    print("I am at the beg of the code")
    rospy.init_node('cmd_vel_publisher')  
    print("I have initalized the robot_move code")
                             # Create node called 'move_robot'
    directions = Twist()                                            # Creating an instance of Twist to tinker with and use as a subsciber 
                         
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
    print("I am publishing to the cmd_vel topic")
    rate = rospy.Rate(2)
    #directions.angular.z = 1
    #directions.linear.x = 1
    directions.angular.z = 0
    directions.linear.x = 1
    

    pub.publish(directions) 
    print("I have sucessfully printed a message")

    #pub.publish(directions)  
     # Create a publisher oobject that is publishing a twist message to cmd_vel       
    #rospy.init_node('robot_move')                               # Initiate a Node called 'odometry_subscriber'
    #rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
    #print("I am subscribed to the lazer topic")
 # Create a Subscriber that will listen to the 
    rospy.spin()                                                # simply keeps python from exiting until this node is stopped

'''
 ***solution** 
#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist
def callback(msg): 
  print(msg.ranges[360]) #We print the distance to an obstacle in front of the robot
#If the distance to an obstacle in front of the robot is bigger than 1 meter, the robot will move forward
  if msg.ranges[360] > 1:
      move.linear.x = 0.1
      move.angular.z = 0.0
#If the distance to an obstacle in front of the robot is smaller than 1 meter, the robot will turn left
  if msg.ranges[360] < 1: 
      move.linear.x = 0.0
      move.angular.z = 0.2
        
#If the distance to an obstacle at the left side of the robot is smaller than 0.3 meters, the robot will turn right
  if msg.ranges[719] < 0.3:
      move.linear.x = 0.0
      move.angular.z = -0.2
        
#If the distance to an obstacle at the right side of the robot is smaller than 0.3 meters, the robot will turn left
  if msg.ranges[0] < 0.3:
      move.linear.x = 0.0
      move.angular.z = 0.2
      
  pub.publish(move)
rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()
rospy.spin() '''