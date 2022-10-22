#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def init_node():
	rospy.init_node("velocity_publisher")
	velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0)
	rospy.sleep(2)
	return velocity_pub
	

def example(velocity_pub):
	loop_rate = rospy.Rate(10)
	starting_time = rospy.get_time()

	while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < 5):
		robot_vel = Twist()
		robot_vel.linear.x = 0.1
		robot_vel.linear.y = 0.0
		robot_vel.linear.z = 0.0
		robot_vel.angular.x = 0.0
		robot_vel.angular.y = 0.0
		robot_vel.angular.z = 0.0
	
		velocity_pub.publish(robot_vel)
		
		loop_rate.sleep()

def ruut1(velocity_pub):
	'''
	Ühte suunda hoidev ruut - holonoomiline
	Liikumine päripäeva
	'''
	loop_rate = rospy.Rate(10)
	robot_vel = Twist()
	
	starting_time = rospy.get_time()
	aeg = 2
	kiirus = 0.1
	
	while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < aeg):
		robot_vel.linear.x = kiirus
		robot_vel.linear.y = 0.0
		robot_vel.linear.z = 0.0
		robot_vel.angular.x = 0.0
		robot_vel.angular.y = 0.0
		robot_vel.angular.z = 0.0
		
		velocity_pub.publish(robot_vel)
		loop_rate.sleep()
	
	while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < aeg*2):
		robot_vel.linear.x = 0.0
		robot_vel.linear.y = -kiirus
		robot_vel.linear.z = 0.0
		robot_vel.angular.x = 0.0
		robot_vel.angular.y = 0.0
		robot_vel.angular.z = 0.0
		
		velocity_pub.publish(robot_vel)
		loop_rate.sleep()
		
	while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < aeg*3):
		robot_vel.linear.x = -kiirus
		robot_vel.linear.y = 0.0
		robot_vel.linear.z = 0.0
		robot_vel.angular.x = 0.0
		robot_vel.angular.y = 0.0
		robot_vel.angular.z = 0.0
		
		velocity_pub.publish(robot_vel)
		loop_rate.sleep()
	
	while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < aeg*4):
		robot_vel.linear.x = 0.0
		robot_vel.linear.y = kiirus
		robot_vel.linear.z = 0.0
		robot_vel.angular.x = 0.0
		robot_vel.angular.y = 0.0
		robot_vel.angular.z = 0.0
		
		velocity_pub.publish(robot_vel)
		loop_rate.sleep()
	
	
def ruut2(velocity_pub):
	'''
	Pööramisega ruut - mitteholonoomiline
	Liikumine vastupäeva
	'''
	loop_rate = rospy.Rate(10)
	robot_vel = Twist()
	
	
	aeg = 1.0
	kiirus = 0.1
	p66re = 1.48
	
	while (not rospy.is_shutdown()):
		for i in range(4):
			starting_time = rospy.get_time()
			# põõre
			while (rospy.get_time() - starting_time < aeg):
				robot_vel.linear.x = 0.0
				robot_vel.linear.y = 0.0
				robot_vel.linear.z = 0.0
				robot_vel.angular.x = 0.0
				robot_vel.angular.y = 0.0
				robot_vel.angular.z = -p66re
		
				velocity_pub.publish(robot_vel)
				loop_rate.sleep()
			#otse	
			while (rospy.get_time() - starting_time < aeg*4):
				robot_vel.linear.x = kiirus
				robot_vel.linear.y = 0.0
				robot_vel.linear.z = 0.0
				robot_vel.angular.x = 0.0
				robot_vel.angular.y = 0.0
				robot_vel.angular.z = 0.0
		
				velocity_pub.publish(robot_vel)
				loop_rate.sleep()
		break


def ring(velocity_pub):
	loop_rate = rospy.Rate(10)
	robot_vel = Twist()
	
	while (not rospy.is_shutdown()):
		starting_time = rospy.get_time()
		while (rospy.get_time() - starting_time < 30):
				robot_vel.linear.x = 0.1
				robot_vel.linear.y = 0.0
				robot_vel.linear.z = 0.0
				robot_vel.angular.x = 0.0
				robot_vel.angular.y = 0.0
				robot_vel.angular.z = 0.4
		
				velocity_pub.publish(robot_vel)
				loop_rate.sleep()
		break


def kaheksa(velocity_pub):
	loop_rate = rospy.Rate(10)
	robot_vel = Twist()
	
	while (not rospy.is_shutdown()):
		starting_time = rospy.get_time()
		#poolring
		while (rospy.get_time() - starting_time < 6):
				robot_vel.linear.x = 0.1
				robot_vel.linear.y = 0.0
				robot_vel.linear.z = 0.0
				robot_vel.angular.x = 0.0
				robot_vel.angular.y = 0.0
				robot_vel.angular.z = 0.7
		
				velocity_pub.publish(robot_vel)
				loop_rate.sleep()
		#otse
		while (rospy.get_time() - starting_time < 12):
				robot_vel.linear.x = 0.1
				robot_vel.linear.y = 0.0
				robot_vel.linear.z = 0.0
				robot_vel.angular.x = 0.0
				robot_vel.angular.y = 0.0
				robot_vel.angular.z = 0.0
		
				velocity_pub.publish(robot_vel)
				loop_rate.sleep()
		#poolring
		while (rospy.get_time() - starting_time < 18):
				robot_vel.linear.x = 0.1
				robot_vel.linear.y = 0.0
				robot_vel.linear.z = 0.0
				robot_vel.angular.x = 0.0
				robot_vel.angular.y = 0.0
				robot_vel.angular.z = -0.7
		
				velocity_pub.publish(robot_vel)
				loop_rate.sleep()
		#otse
		while (rospy.get_time() - starting_time < 24):
				robot_vel.linear.x = 0.1
				robot_vel.linear.y = 0.0
				robot_vel.linear.z = 0.0
				robot_vel.angular.x = 0.0
				robot_vel.angular.y = 0.0
				robot_vel.angular.z = 0.0
		
				velocity_pub.publish(robot_vel)
				loop_rate.sleep()
		
		break


def main():
	pub = init_node()
	#example(pub)
	for i in range(2):
		ruut1(pub)
	for i in range(2):
		ruut2(pub)
	ring(pub)
	for i in range(3):
		kaheksa(pub)


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		print('error')