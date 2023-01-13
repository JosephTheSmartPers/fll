from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound
from ev3dev2.sensor import *
import time

gs = GyroSensor("in2")
spkr = Sound()
m = MoveTank(OUTPUT_B, OUTPUT_C)
gs.MODE_GYRO_ANG = 'GYRO-ANG'
gs.reset()

def turn(degree, speed, acceleration, maxTime, margin = 2, timeout = 3):
    print("turning")
    startTime = time.time()
    now = 999999999999
    global normal
    rldegree = degree * -1
    rotation = gs.angle
    seconds = time.time() - now
    go = True
    while gs.angle != rotation - rldegree and go == True:
        if(startTime + timeout <= time.time()):
            break
        seconds = time.time() - now

        if(((rotation - rldegree) - margin <= gs.angle <= (rotation - rldegree)  + margin)):
            if(now > time.time()):
                now = time.time()

        if(seconds >= maxTime):
            m.stop()
            go = False

        spd = (rotation - rldegree - gs.angle) * acceleration
        if(spd > speed):
            spd = speed
        if(spd < speed * -1):
            spd = speed * -1
        m.on(spd * -1, spd)
        print(spd)
    m.stop()
    normal = gs.angle
    gs.reset()
  
##turn(50, 70, 0.7, 2)