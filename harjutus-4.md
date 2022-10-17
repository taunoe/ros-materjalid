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



## Lingid

- [Noodul 4](https://sisu.ut.ee/rosak/moodul-4)
- [Muutujad (Python)](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTIIMuutujad)
- [Valiklaused](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTIIIValikulause1)
- [Tsüklid](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTVTsykkel1)
- [Funktsioonid](https://courses.cs.ut.ee/2022/progmaa/spring/Main/PARTVIIFunktsioon1)
