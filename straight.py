from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
leftm = LargeMotor(OUTPUT_B)
rightm = LargeMotor(OUTPUT_C)


m = MoveTank(OUTPUT_B, OUTPUT_C)
s = MoveSteering(OUTPUT_B, OUTPUT_C)
gs = GyroSensor("in2")



def straight(rot, maxspeed, dir, speedup, slowdown, p, minspeed):
    if(maxspeed < 0):   
        minspeed = minspeed * -1
    print(rotations())
    ##if(maxspeed < 0):
        ##speedup *= -1
        ##slowdown *= -1
    while abs(rotations()) <= rot:
        if(abs(rotations()) < speedup):
            print("speeding up")
            spd = (abs(rotations()) / speedup * (maxspeed - minspeed)) + minspeed
        elif(abs(rotations()) > slowdown):
            print("slowing down")
            spd = maxspeed - ((abs(rotations()) - (rot - slowdown)) / slowdown * maxspeed) + minspeed
        else:
            print("going normal speed")
            spd = maxspeed
        if spd > 100:
            spd = 100
        angle = (dir - (gs.angle * -1)) * p
        if(maxspeed < 0):
            angle = angle * -1
        if(angle > 100):
            angle = 100
        elif(angle < - 100):
            angle = -100
        print(spd)
        s.on(angle, spd)
    m.stop()
def rotations():
    return leftm.rotations + rightm.rotations / 2
print(rotations())
gs.reset()
print(gs.angle)
#straight(3, 75, int(gs.angle), 2, 2, 2, 20)
leftm.reset()
rightm.reset()
print("aaaaaaaaaaaaaaa")
straight(3, -75, int(gs.angle), 1, 1.5, 2, 20)
