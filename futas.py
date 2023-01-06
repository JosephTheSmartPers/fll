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

reset(yhand)
reset(xhand)

straight(2.7, 60, int(gs.angle), 1.5, 20)
xhand.on_for_rotations(90, -1)
straight(1.8, -60, int(gs.angle), 1.5, 20)
yhand.on_for_rotations(90, 0.4)
straight(2.14, 60, int(gs.angle), 1.5, 20)
yhand.on_for_rotations(90, 0.8)
xhand.on_for_rotations(90, 0.7)


time.sleep(0.5) #Wait for cell to rool back
turn(60, 55, 0.4, 0.5)
xhand.on_for_rotations(-90, 0.6)

yhand.on(2)

print(followLine(0.4, 2.5, 25, 20, rs, True))
yhand.stop()
reset(yhand)

gs.reset()
straight(1.29, -30, int(gs.angle), 1.5, 20)

raiseHeight = 1.1

xhand.on_for_rotations(90, 0.35)
yhand.on_for_rotations(90, raiseHeight)
yhand.on_for_rotations(90, -raiseHeight)
yhand.on_for_rotations(90, raiseHeight)
yhand.on_for_rotations(90, -raiseHeight)
yhand.on_for_rotations(90, raiseHeight)
yhand.on_for_rotations(90, -(raiseHeight / 2))
xhand.on_for_rotations(90, -0.35)
straight(1, -60, int(gs.angle) + 60, 1.5, 20)
turn(30, 55, 0.7, 0.5)
yhand.on_for_rotations(-90, 0.1)
xhand.on_for_rotations(90, 0.7)
straight(6, -90, int(gs.angle), 1.5, 20)

"""
turn(34, 70, 0.5, 1)
turn(-45, 70, 0.5, 1)


straight(0.5, -30, int(gs.angle), 1.5, 20)

turn(45, 70, 0.5, 1)

xhand.reset()
yhand.reset()
"""

