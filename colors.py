from ev3dev2.motor import *
from ev3dev2.sensor.lego import GyroSensor, ColorSensor 
from time import sleep
import math

gs = GyroSensor()
cs = ColorSensor()

gs.reset()

cs = ColorSensor()
m1 = LargeMotor("outA")
m2 = LargeMotor("outD")
tank = MoveTank("outA", "outD")
tanki = MoveSteering("outA", "outD")
karle = MediumMotor("outB")
karjx = MediumMotor("outC")

print("Kész vagyok")
while True:
    if(cs.color == "5" or cs.color == 5):
        tank.on_for_rotations(75, 75, 1)
    elif(cs.color == "3" or cs.color == 3):
        
