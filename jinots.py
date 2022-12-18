#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int64


def move():
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = 0
    distance = 0
    isForward = 0
    
    print("Let's move your robot")
    speed = int(input("Input your speed:"))
    distance = int(input("Type your distance:"))
    isForward = int(input("Foward?: "))
    
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():        
        t0 = rospy.Time.now().to_sec()
        current_distance = 0        
        while(current_distance < distance):            
            velocity_publisher.publish(vel_msg)            
            t1=rospy.Time.now().to_sec()           
            current_distance= speed*(t1-t0)
        
        vel_msg.linear.x = 0        
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:        
        move()
    except rospy.ROSInterruptException: 
        pass