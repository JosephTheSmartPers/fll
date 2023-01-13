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

gs.reset()

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

    if(maxspeed  < 0):
        rot = rot * -1

    rot = rot + rotations()
    if(maxspeed < 0):
        minspeed = minspeed * -1
    stopNow = False
    speedup = rot * 0.5

    slowdown = rot * 0.6

    while rotations() < rot and stopNow == False:
        if(stopOnLine == True):
            if(bs.reflected_light_intensity <= 8 or rs.reflected_light_intensity <= 8):
                if(coorigate == True):
                    raall(2, 1, 15, 6)
                m.stop()
                stopNow = True
                return

        if(rotations() < speedup):
            print("speeding up")
            spd = (rotations() / speedup * (maxspeed - minspeed)) + minspeed
            print(rotations())
        elif(rotations() > slowdown):
            print("slowing down")
            print(rotations())
            spd = maxspeed - rotations() - ((rot - slowdown) / slowdown * maxspeed) + minspeed
        else:
            print("going normal speed")
            spd = maxspeed
            
        if(abs(spd) > maxspeed): spd = (abs(spd) / spd) * maxspeed
        angle = (dir - (gs.angle * -1)) * p
        if(abs(angle) > maxspeed): angle = (abs(angle) / angle) * maxspeed
        if(maxspeed < -1):
            angle *= -1
        s.on(angle, spd)
    m.stop()
##straight(3, 60, int(gs.angle), 1.5, 20)

