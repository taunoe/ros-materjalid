#!/usr/bin/env python3
import tf

# Kvaternioni teisendamine Euleri nurkadeks
def callback(data):
    for marker in data.markers:
        marker_ori = (
            marker.pose.pose.orientation.x,
            marker.pose.pose.orientation.y,
            marker.pose.pose.orientation.z,
            marker.pose.pose.orientation.w)

        # sisendiks on kvaternion ja väljundiks on järjend Euleri nurkadega
        euler = tf.transformations.euler_from_quaternion(marker_ori)
        roll = euler[0]
        yaw = euler[1]
        pitch = euler[2]
