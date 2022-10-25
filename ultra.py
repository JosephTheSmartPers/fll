from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
import time

usb=UltrasonicSensor(INPUT_3)

while True:
    time.sleep(1)
    print(usb.distance_centimeters)