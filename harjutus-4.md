# Roboto liikumine

Rubriigis `cmd_vel` infot selle kohta, kuidas me soovime robotit liigutada.

Rubriigi `cmd_vel` sõnumitel on kindel struktuur ehk tüüp nimega **Twist**. Twist kuulub kategooriasse `geometry_msgs` ja sisaldab kaht vektorit, millest kummaski on kolm reaalarvu.

- vektor _linear_ ja kirjeldab **lineaarset liikumist** kolmemõõtmelise ruumi kolmes suunas. Kiiruseid (ühikuks m/s) kolmes teljes (x,y,z).
- vektori _angular_ ja kirjeldavad roboti **pöördliikumist** ümber nendesamade kolme telje. **Nurkkiirused** vastavate telgede ümber: x-telg, y-telg ja z-telg (ühikuks radiaan sekundis ehk rad/s).

ROSis on roboti liikumise koordinaatsüsteemi 

- **x-telg** suunatud ettepoole
- **y-telg** vasakule
- **z-telg** üles.

## Kimbu loomine

- Nimi: `geometric_shapes`.
- Sõltub kimpudest: `rospy`, `geometry_msgs`

```bash
cd ~/catkin_ws/src
catkin create pkg geometric_shapes --catkin-deps rospy geometry_msgs
cd geometric_shapes
mkdir scripts
gedit simple_velocity_publisher.py
```

```python
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def main():
  # Init sõlm
  rospy.init_node("velocity_publisher")
  # Kuulutaja (rubriigi nimi, sõnumitüüp, järjekorra suurus) 0=ei oota järjekorras
  velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0)
  rospy.sleep(2)

  # sõnumi loomine
  robot_vel = Twist()
  robot_vel.linear.x = 0.1 # m/s
  robot_vel.linear.y = 0.0
  robot_vel.linear.z = 0.0
  robot_vel.angular.x = 0.0
  robot_vel.angular.y = 0.0
  robot_vel.angular.z = 0.0

  # Sõnumi kuulutamine
  velocity_pub.publish(robot_vel)

if __name__ == '__main__':
  try:
    main()
  except rospy.ROSInterruptException:
    pass
```

Anname failile käivitamisõigused:

```bash
chmod u+x simple_velocity_publisher.py
```

Kompileerime ja laadime:

```bash
cd ../..
catkin build
source devel/setup.bash
```

Pythoni koodi ei pea iga kord catkini tööruumi uuesti kompileerima - C++ koodi kirjutades peaksime seda tegema.

Käivitame roscore:

```bash
roscore
```

Kuulame sõnumeid:

```bash
rostopic echo cmd_vel
```

Käivitame uue sõlme ja vaatame kas näeme sõnumit:

```bash
rosrun geometric_shapes simple_velocity_publisher.py
```

Käivitame visualiseerimise ja vaatame kas robot liigub:

```bash
roslaunch robotont_driver fake_driver.launch
```

### Koodi näide 2

Liigume järjest 5 sekundit.

```bash
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node("velocity_publisher")
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=0)
    rospy.sleep(2)

    loop_rate = rospy.Rate(10) # kood jooksma kiirusega 10 Hz

    # alustame ajamõõtmist
    starting_time = rospy.get_time()

    # jooksutame koodi 5 sek
    while (not rospy.is_shutdown()) and (rospy.get_time() - starting_time < 5):
        robot_vel = Twist()
        robot_vel.linear.x = 0.1
        robot_vel.linear.y = 0.0
        robot_vel.linear.z = 0.0
        robot_vel.angular.x = 0.0
        robot_vel.angular.y = 0.0
        robot_vel.angular.z = 0.0

        velocity_pub.publish(robot_vel)

        loop_rate.sleep() # ootame, et kood ei jookseks ettenähtust kiiremini

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
```

## Geomeetrilised kujundid

### Ühte suunda hoidev ruut (holonoomiline)

### Pööramisega ruut (mitteholonoomiline)

### Ring

### Kaheksa-sümbol

## Lingid

- [Noodul 4](https://sisu.ut.ee/rosak/moodul-4)
- [Muutujad (Python)](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTIIMuutujad)
- [Valiklaused](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTIIIValikulause1)
- [Tsüklid](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTVTsykkel1)
- [Funktsioonid](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTVIIFunktsioon1)
