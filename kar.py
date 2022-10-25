from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
import time
m = MoveTank(OUTPUT_A, OUTPUT_D)
mm1 = MediumMotor(OUTPUT_C)
mm2 = MediumMotor(OUTPUT_B)
mm1.reset()
mm2.reset()
def xhand(rot, spd):
    mm1.on_for_seconds(rot, spd)
    time.sleep(spd)
    mm1.reset()
def yhand(rot, spd):
    mm2.on_for_seconds(rot, spd)
    time.sleep(spd)
    mm2.reset()
def repulo():
    xhand(-100, 1.9)
    yhand(-100, 1.9)
    xhand(100, 1.9)
    time.sleep(1)
    yhand(100, 1.9)
def lepulo():
    yhand(-100, 1.9,)
def bridge():
    xhand(100, 1.9)
    yhand(-100, 1.5)
    m.on_for_rotations(75, 75, 1)
def kakas():
    yhand(-75, 0.3)
    xhand(75, 1)
kakas()