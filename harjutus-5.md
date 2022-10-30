# AR märgised

NB! Puudu kaamera kalibreerimine.

Kimbu `ar_track_alvar` paigaldamine:

```bash
cd ~/catkin_ws/src
git clone https://github.com/rios-ai/ar_track_alvar.git
cd ar_track_alvar
git checkout feature/rios_bug_fix
cd ../..
catkin build
source devel/setup.bash
```

## Tellija (_subscriber_)

Uus kimp, mis sõltub kimpudest: `ar_track_alvar_msgs`, `geometry_msgs`, `rospy` ja `tf`.

```bash
cd ~/catkin_ws/src
catkin create pkg tauno_ar_subscriber --catkin-deps ar_track_alvar_msgs rospy geometry_msgs tf
cd tauno_ar_subscriber
mkdir scripts
gedit tauno_ar_subscriber.py
```

```python
#!/usr/bin/env python3
import rospy
from ar_track_alvar_msgs.msg import AlvarMarkers

def ar_message_handler(data):
  if len(data.markers) > 0:
    for marker in data.markers:
      rospy.loginfo("Detected marker with ID " + str(marker.id))
      rospy.loginfo("position x " + str(marker.pose.pose.position.x))
  else:
    rospy.loginfo("No AR markers detected.")

def main():
   # Init sõlm
  rospy.init_node("tauno_ar_subscriber")

  # Tellija kuulab AlvarMarkers tüüpi sõnumeid rubriigis ar_pose_marker
  # Tagasikutsefunktsioon (callback function) ehk funktsioon, mis käivitub iga sõnumi saabumisel on ar_message_handler
  rospy.Subscriber("ar_pose_marker", AlvarMarkers, ar_message_handler)

  # spin() simply keeps python from
  # exiting until this node is stopped
  #rospy.spin()

  while (not rospy.is_shutdown()):
    pass

if __name__ == '__main__':
  try:
    main()
  except rospy.ROSInterruptException:
    pass
```

```bash
chmod +x tauno_ar_subscriber.py
rosrun tauno_ar_subscriber tauno_ar_subscriber.py
```

### Käivitusfail

```bash
cd ~catkin_ws/src/tauno_ar_subscriber/
mkdir launch
cd launch
gedit pr2_indiv_no_kinect.launch
```

- Robotil kasutades `camera/color/image_raw_throttled`
- Gazebos `camera/color/image_raw`
- Gazebo käivitamine `roslaunch robotont_gazebo world_minimaze_ar.launch`

```xml
<launch>
  <include file="$(find ar_track_alvar)/launch/pr2_indiv_no_kinect.launch">
    <arg name="cam_image_topic" value="camera/color/image_raw_throttled"/>
    <arg name="cam_info_topic" value="camera/color/camera_info"/>
    <arg name="output_frame" value="camera_link"/>
    <arg name="marker_size" value="10"/>
  </include>
</launch>
```

```bash
chmod +x pr2_indiv_no_kinect.launch
```

AR märgiste tuvastamise programmi käivitamine:

```bash
roslaunch tauno_ar pr2_indiv_no_kinect.launch
```

Sõnumite vaatamine:

```bash
rostopic echo /ar_pose_marker
```

Manuaalne juhtimine `rosrun teleop_twist_keyboard teleop_twist_keyboard.py`

Oma koodi käivitamine `rosrun tauno_ar_subscriber tauno_ar_subscriber.py`

## Lingid

- [sisu.ut.ee/rosak/moodul-5](https://sisu.ut.ee/rosak/moodul-5)
- [Writing the Subscriber Node](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
