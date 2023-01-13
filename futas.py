from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *

leftm = LargeMotor(OUTPUT_B)
rightm = LargeMotor(OUTPUT_C)
yhand = MediumMotor(OUTPUT_A)
xhand = MediumMotor(OUTPUT_D)

m = MoveTank(OUTPUT_B, OUTPUT_C)
s = MoveSteering(OUTPUT_B, OUTPUT_C)
gs = GyroSensor(INPUT_2)
rs = ColorSensor("in3")
ls = ColorSensor("in4")

ls.MODE_COL_REFLECT = "COL-REFLECT"
rs.MODE_COL_REFLECT = "COL-REFLECT"
gs.MODE_GYRO_ANG = 'GYRO-ANG'

from line import *
from turn import *
from straight import *
from reset import *

#Kiszámolja, hogy milyen

def startCalc(startDegree, plusDegree):
    return((startDegree - gs.angle) + plusDegree)

"""
#Visszaállítja a kezdeti pozicóba a karokat
reset(yhand, 2.5)
reset(xhand, 1.1)
"""

startDegree = gs.angle

straight(2.74, 30, int(gs.angle), 1.1, 20)
xhand.on_for_rotations(90, -1)
straight(1.8, -30, int(gs.angle), 1.1, 20)
yhand.on_for_rotations(90, 0.4)
straight(2.15, 30, int(gs.angle) + -1.4, 1.1, 20)
yhand.on_for_rotations(90, 0.9)
xhand.on_for_rotations(90, 0.7)


time.sleep(0.6) #Wait for cell to rool back

turn(startCalc(startDegree, 100), 27, 0.4, 0.5)
gs.reset()
straight(0.2, 25, int(gs.angle), 1, 20)#, True, True)
turn(startCalc(startDegree, -62), 20, 0.5, 0.3)
"""
xhand.on_for_rotations(-90, 0.7)
yhand.on_for_rotations(90, 0.2)
print(followLine(0.55, 2.2, 20, 40, ls))

#Innen
#straight(3.8, 60, int(gs.angle), 1, 20)

yhand.on_for_rotations(45, -1.2)
m.on_for_rotations(-15, -15, 0.2)
straight(1.5, -15, int(gs.angle), 1.5, 20)

raiseHeight = 1.1
raiseSpeed = 45

xhand.on_for_rotations(raiseSpeed, 0.35)
yhand.on_for_rotations(raiseSpeed, raiseHeight)
yhand.on_for_rotations(raiseSpeed, -raiseHeight)
yhand.on_for_rotations(raiseSpeed, raiseHeight)
yhand.on_for_rotations(raiseSpeed, -raiseHeight)
yhand.on_for_rotations(raiseSpeed, raiseHeight)
yhand.on_for_rotations(raiseSpeed, -(raiseHeight / 2))
xhand.on_for_rotations(raiseSpeed, -0.35)
straight(1, -30, int(gs.angle) + 60, 1.5, 20)
turn(30, 25, 0.7, 0.4)
yhand.on_for_rotations(-45, 0.1)
#xhand.on_for_rotations(90, 0.2)
straight(1.1, -45, int(gs.angle), 1.5, 20)

turn(45, 35, 0.5, 1)

straight(3, -37.5, int(gs.angle), 1.5, 20)


xhand.reset()
yhand.reset()"""
#HA KÉSZ VAN ÁRON MEGMUTAT FOTÓT