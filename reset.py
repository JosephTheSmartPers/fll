from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *

def reset(motor, maxRot):
    motorRotations = motor.rotations
    if(abs(motorRotations) > maxRot):
        motorRotations = (abs(motorRotations) / motorRotations) * maxRot
        
    motor.on_for_rotations(90, motorRotations * -0.99 )
    motor.reset()