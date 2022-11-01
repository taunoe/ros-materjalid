# Harjutus 6

## Keskkonna kaardistamine

Kimbu loomine

```bash
cd catkin_ws/src/
catkin create pkg uue_kimbu_nimi
```

Ainult simulatoris kasutamisel: `roslaunch robotont_gazebo world_minimaze.launch model:=robotont_gazebo_lidar`

**SLAMi sõlm** kasutame algoritmi gmapping. gmapping tugineb lidari andmetele. Robotondil pole lidarit - on sügavuskaamera. ROSi kimpu nimega `depthimage_to_laserscan`, kus on sõlm, mis teeskleb sügavuskaamera info põhjal, et ta robot saab andmeid lidari käest. Sisuliselt teeskleb see, et meil on lidari andmed, kuigi tegelikult ei ole. 

```bash
roslaunch robotont_demos gmapping.launch
```

Kaardi kuvamine

```bash
roslaunch robotont_demos 2d_slam_display.launch
```

Roboti Manuaalne juhtimine

```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

Kaardi salvestamine (sõlm `map_saver` kimbust `map_server`)

```bash
cd katkin_ws/src/kaardistaja
mkdir maps
cd maps
rosrun map_server map_saver -f ruumi-kaart
```

## Autonoomne navigeerimine

**Kaardi** laadimine

```bash
cd katkin_ws/src/kaardistaja/maps/
rosrun map_server map_server ruumi-kaart.yaml
```

**Lokaliseerimine** kasutades meetodit nimega "adaptiivne Monte Carlo lokaliseerimine". Sõlme `amcl` kimbust `amcl`.

```bash
rosrun amcl amcl
```

**Planeerimine** ja navigeerimine. Kimp nimega `move_base`. Sellest kimbust sõlme käivitamiseks õigete parameetritega on käivitusfail kimbus `robotont_navigation`.

```bash
roslaunch robotont_navigation move_base.launch
```

RViz `roslaunch robotont_demos 2d_slam_display.launch`

## Links

- https://sisu.ut.ee/rosak/praktika-moodul-6
- https://openslam-org.github.io/gmapping.html
