from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *

def reset(motor):
    motor.on_for_rotations(40, motor.rotations * -0.8 )
    motor.reset()