from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
leftm = LargeMotor(OUTPUT_B)
rightm = LargeMotor(OUTPUT_C)


m = MoveTank(OUTPUT_B, OUTPUT_C)
s = MoveSteering(OUTPUT_B, OUTPUT_C)
gs = GyroSensor(INPUT_2)
rs = ColorSensor("in3")
bs = ColorSensor("in4")

bs.MODE_COL_REFLECT = "COL-REFLECT"
rs.MODE_COL_REFLECT = "COL-REFLECT"

def rotations():
    return leftm.rotations + rightm.rotations / 2


def stop():
    m.stop
    leftm.stop()
    rightm.stop()
    perfect = True  

def raall(sensi, maxs, maxspd, minlight):
    now = time.time()
    print(time.time)
    perfect = False
    
    seconds = time.time() - now
    while perfect != True:
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
            perfect = True
        if(leftSpd == 0 and rightSpd == 0):
            stop()
            perfect = True

def straight(rot, maxspeed, dir, p, minspeed, stopOnLine = False, coorigate = False):
    speedup = rot * 0.2
    slowdown = rot * 0.8
    if(maxspeed < 0):   
        minspeed = minspeed * -1
    print(rotations())
    stopNow = False

    while abs(rotations()) <= rot and stopNow == False:
        if(stopOnLine == True):
            if(bs.reflected_light_intensity <= 10 or rs.reflected_light_intensity <= 10):
                if(coorigate == True):
                    raall(2.45, 1, 15, 6)
                m.stop()
                stopNow = True
                return

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

straight(10, -45, int(gs.angle), 2, 20)


