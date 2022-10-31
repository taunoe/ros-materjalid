#!/usr/bin/env python3
"""
Robot keerab kahe AR markeri vahel
Moodul 5
"""
import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers
from geometry_msgs.msg import Twist

new_marker_id = 1


def ar_message_handler(data):
   global new_marker_id
   
   if len(data.markers) > 0:
      for marker in data.markers:
         rospy.loginfo("Detected marker with ID " + str(marker.id))
         new_marker_id = marker.id
         
         #rospy.loginfo("position x " + str(marker.pose.pose.position.x))
   else:
      rospy.loginfo("No AR markers detected.")


def main():
    global new_marker_id
    
    rospy.init_node("tauno_ar")
    rospy.Subscriber("ar_pose_marker", AlvarMarkers, ar_message_handler)
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0)
    rospy.sleep(2)
    
    loop_rate = rospy.Rate(10)
    starting_time = rospy.get_time()
    
    old_marker_id = 0
    
    z = 0.3

    while (not rospy.is_shutdown()):
       robot_vel = Twist()
       robot_vel.linear.x = 0
       robot_vel.linear.y = 0
       robot_vel.linear.z = 0
       robot_vel.angular.x = 0
       robot_vel.angular.y = 0
       robot_vel.angular.z = z
       
       if (new_marker_id != old_marker_id):
           rospy.loginfo("new ID")
           z = -(z)
           #if (new_marker_id > old_marker_id):
           #    robot_vel.angular.z = -0.3
           #else:
           #    robot_vel.angular.z = 0.3
           old_marker_id = new_marker_id
       
       velocity_pub.publish(robot_vel)
       
       loop_rate.sleep()


if __name__ == '__main__':
   try:
        main()
   except rospy.ROSInterruptException:
        print('error')

