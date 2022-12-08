from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
leftm = LargeMotor(OUTPUT_B)
rightm = LargeMotor(OUTPUT_C)
hand = MediumMotor(OUTPUT_A)

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


followLine(0.8, 3, 20 , 40, ls, True)
hand.on_for_rotations(70, 0.4, False, False)
m.on_for_rotations(-20, -20, 0.6)
hand.on_for_rotations(-70, 0.4, False, False)
m.on_for_rotations(-20, -20, 0.2)
turn(90, 45, 0.4, 1)




