from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
leftm = LargeMotor(OUTPUT_A)
rightm = LargeMotor(OUTPUT_D)
#sensor2 = UltrasonicSensor(INPUT_2)

mm1 = MediumMotor(OUTPUT_C)
mm2 = MediumMotor(OUTPUT_B)

m = MoveTank(OUTPUT_A, OUTPUT_D)
s = MoveSteering(OUTPUT_A, OUTPUT_D)
gs = GyroSensor(INPUT_1)

gs.reset()
print(gs.angle)

#(rotations, maxspeed, angle, acceleration, deceleration, sensitivity, minspeed)
def straight(rot, maxspeed, dir, speedup, slowdown, p, minspeed):

    while rotations() <= rot:
        if(rotations() < speedup):
            #linear speeding up
            spd = (rotations() / speedup * (maxspeed - minspeed)) + minspeed
        elif(rotations() > slowdown):
            #linear slowing down
            spd = maxspeed - ((rotations() - (rot - slowdown)) / slowdown * maxspeed) + minspeed
        else:
            print("going normal speed")
            spd = maxspeed
        if spd > 100:
            spd = 100
        angle = (dir - (gs.angle * -1)) * p
        if(angle > 100):
            angle = 100
        elif(angle < - 100):
            angle = -100
        s.on(angle, spd)
    m.stop()

#Returns the motors rotations, is here to make the program a little cleaner.
def rotations():
    return leftm.rotations + rightm.rotations / 2

#(angle, maxspeed, acceleration)
def turn(degree, speed, acceleration):
    global normal
    rldegree = degree * -1
    rotation = gs.angle
    while gs.angle != rotation - rldegree:
            spd = (rotation - rldegree - gs.angle) * acceleration
            if(spd > speed):
                spd = speed
            if(spd < speed * -1):
                spd = speed * -1
            m.on(spd * -1, spd)
           ##print(spd)
    m.stop()
    normal = gs.angle
m.on(75, 75)
#(rotations, maxspeed, angle, acceleration, deceleration, sensitivity, minspeed)
def number1():
    mm2.on_for_seconds(75, 1)
    mm2.reset()
    straight(6.8, 50, int(gs.angle - 20), 2, 3, 2, 20)
    mm2.on_for_seconds(-75, 1)
    mm2.reset()
    m.on_for_rotations(-75, -75, 3.6)
def number2():
    mm1.on_for_seconds(75, 1)
    mm1.reset()
    straight(5, 50, int(gs.angle), 2, 3, 1, 20)
    m.on_for_rotations(-75, -75, 0.8)
    mm1.on_for_seconds(-75, 1)
    mm1.reset()
    leftm.reset()
    rightm.reset()
    straight(1, 50, int(gs.angle), 2, 3, 1, 20)
    mm1.on_for_seconds(75, 1)
    mm1.reset()
number1()

