# Harjutus 2

## Kirjeldus

Robotont otsib enda ümbruskonnas üles oranži porgandi ja sõidab selle juurde. Kui on porgandi juurte jõudud otsib järgmse porgandi ja sõidab selle juurde jne kuni program katkestatakse.

On kolm sõlme (_node_):

- Sõlm, mis võtab kaamerast pildi ja kuulutab saadud pilti mõnes rubriigis.
- Sõlm, mis kuulab rubriiki, kus on kaamera pildid, ja leiab neilt oranžid porgandid.
- Sõlm, mis võtab tuvastatud porgandite asukohad ja paneb roboti nende järgi sõitma.

Rubriike näeme käsuga:

`rostopic list`

Meie ülesandeks sobib rubriik `/camera/color/image_raw_throttled`.

### _blob detector_

Porgandid on taustast selgesti eristatava värviga - oranžid. Ja vaateväljas muid oranže objekte ei ole.

Laigutuvastaja (_blob detector_) kasutamiseks kimp nimega **opencv_apps**.

#### Laigutuvastaja paigaldamine

```bash
cd ~/catkin_ws/src
git clone https://github.com/ut-ims-robotics/opencv_apps.git
cd opencv_apps
git checkout blob_detection_nodelet
```

### Porgandi jällitaja paigaldamine

On Pythoni script.

```bash
cd ..
git clone https://github.com/unitartu-edu/carrot_follower.git
```

### Kompileerime ja laadime

```bash
catkin build
source devel/setup.bash
```

#### Laigutuvastaja kasutamine

Muuta seadistuste failis `opencv_apps/config/blob_detection_config.yaml` parameetreid, et leiaks piisava suurusega oranzid objektid. Värvid on HSV värviruumis.

```yaml
hue_lower_limit: 5
hue_upper_limit: 20
...
min_area: 20
...
sat_lower_limit: 160
...
val_lower_limit: 100
```

### Katsetame

OpenCV käivitamine:

```bash
roslaunch opencv_apps blob_detection.launch debug_mode:=deploy image:=/camera/color/image_raw_throttled
```

Liikumise käivitamine

```bash
rosrun carrot_follower carrot_follower.py
```

## Otsi viga

Kõiki aktiivseid sõlmi näeb käsuga:

`rosnode list`

Kas on tekkinud rubriik `/blob_detection/blobs`? Kuhu kuulutab sõlm nimega `blob_detection`?

```bash
rostopic list
rostopic info /blob_detection/blobs
```

Mis rubriiki tellib `carrot_follower`? Kas see on õige? Peata ja käivita uuesti nii, et telliks õiget rubriiki.

```bash
rosrun carrot_follower carrot_follower.py xxxx:=/blob_detection/blobs
```

Kuula pealt sõnumeid:

```bash
rostopic echo /blob_detection/blobs
```

## Mida robot näeb?

`rviz -d ~/catkin_ws/src/carrot_follower/config/watch_carrots.rviz`

## Lingid

- [github.com/ut-ims-robotics/opencv_apps/](https://github.com/ut-ims-robotics/opencv_apps/)
- [github.com/unitartu-edu/carrot_follower](https://github.com/unitartu-edu/carrot_follower)