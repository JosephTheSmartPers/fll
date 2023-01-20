from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *

leftMotorOutput = "outC"
rightMotorOutput = "outA"

leftm = LargeMotor(leftMotorOutput)
rightm = LargeMotor(rightMotorOutput)
import math

m = MoveTank(leftMotorOutput, rightMotorOutput)
s = MoveSteering(leftMotorOutput, rightMotorOutput)
"""gs = GyroSensor(INPUT_2)
rs = ColorSensor("in3")
bs = ColorSensor("in4")"""

gs = GyroSensor("in2")
rs = ColorSensor("in4")
bs = ColorSensor("in1")

def rotations():
    return leftm.rotations + rightm.rotations / 2


def stop():
    m.stop
    leftm.stop()
    rightm.stop()

def raall(sensi, maxs, maxspd, minlight):
    now = time.time()
    print(time.time)
    
    seconds = time.time() - now
    while True:
        seconds = time.time() - now

        leftSpd = (minlight - bs.reflected_light_intensity) * sensi * (2 - seconds)
        rightSpd = (minlight - rs.reflected_light_intensity) * sensi * (2 - seconds)
        if(abs(leftSpd) > maxspd):
            leftSpd = maxspd * (leftSpd / abs(leftSpd))
        if(abs(rightSpd) > maxspd):
            rightSpd = maxspd * (rightSpd / abs(rightSpd))
        leftm.on(leftSpd)
        rightm.on(rightSpd)

        if(seconds >= maxs):
            stop()
            break
        if(leftSpd == 0 and rightSpd == 0):
            stop()
            break

def straight(rot, maxspeed, dir, p, minspeed, stopOnLine = False, coorigate = False):
    speedup = rot * 0.5
    slowdown = rot * 0.6
    onPoint = 0
    totalTimes = 0

    startRotations = rotations()
    deltaTime = time.time()

    if(maxspeed < 0):   
        minspeed = minspeed * -1

    while abs(rotations() - startRotations) <= rot:
        if(stopOnLine == True):
            if(bs.reflected_light_intensity <= 8 or rs.reflected_light_intensity <= 8):
                if(coorigate == True):
                    raall(1.75, 0.7, 15, 6)
                m.stop()
                break

        if(abs(rotations() - startRotations) < speedup):
            spd = (abs(rotations() - startRotations) / speedup * (maxspeed - minspeed)) + minspeed
        elif(abs(rotations() - startRotations) > slowdown):
            spd = maxspeed - ((abs(rotations() - startRotations) - (rot - slowdown)) / slowdown * maxspeed) + minspeed
        else:
            spd = maxspeed

        if(abs(spd) > maxspeed): spd = (abs(spd) / spd) * abs(maxspeed)
        angle = ((dir * -1) - (gs.angle * -1)) * p
        if(maxspeed < 0):
            angle = angle * -1
        if(abs(angle) > 100): angle = (abs(angle) / angle) * 100

        if(gs.angle == dir):
            onPoint += 1
        totalTimes += 1
        s.on(angle, spd)
    m.stop()
    time.sleep(0.2)
    print("Kész az egyenesen menés "+ str(time.time() - deltaTime) +" mp alatt"+", pontosság: " + str((onPoint/totalTimes) * 100) + "%")
straight(1, 60, int(gs.angle), 1.5, 20)
straight(1, -60, int(gs.angle), 1.5, 20)
