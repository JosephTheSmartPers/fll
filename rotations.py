from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
yhand = MediumMotor(OUTPUT_A)
xhand = MediumMotor(OUTPUT_D)
yhand.reset()
yhand.on_for_rotations(90, )