from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
leftm = LargeMotor(OUTPUT_B)
rightm = LargeMotor(OUTPUT_C)


m = MoveTank(OUTPUT_B, OUTPUT_C)
s = MoveSteering(OUTPUT_B, OUTPUT_C)
gs = GyroSensor(INPUT_2)
rs = ColorSensor("in3")
ls = ColorSensor("in4")

ls.MODE_COL_REFLECT = "COL-REFLECT"
rs.MODE_COL_REFLECT = "COL-REFLECT"

go = True

def sign(number):
    if(number == 0):
        number = 1
    value = number / abs(number)
    return value

def stop():
    m.stop
    leftm.stop()
    rightm.stop()
    perfect = True  

def raall(sensi, maxs, maxspd, minlight, margin = 2):
    now = 9999999999999999999
    maxms = float(maxs)
    print(time.time)
    leftPrev = 100
    rightPrev = 100
    perfect = False


    
    seconds = time.time() - now
    while perfect != True:
        

        seconds = time.time() - now

        leftSpd = (minlight - ls.reflected_light_intensity) * sensi
        rightSpd = (minlight - rs.reflected_light_intensity) * sensi
        
        if(abs(leftSpd) > maxspd):
            leftSpd = maxspd * sign(leftSpd)
        if(abs(rightSpd) > maxspd):
            rightSpd = maxspd * sign(rightSpd)
        leftm.on(leftSpd)
        rightm.on(rightSpd)

        if((minlight - margin <= ls.reflected_light_intensity <= minlight + margin) and (minlight - margin <= rs.reflected_light_intensity <= minlight + margin)):
            if(now > time.time()):
                now = time.time()


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
            if(ls.reflected_light_intensity <= 10 or rs.reflected_light_intensity <= 10):
                if(coorigate == True):
                    raall(1.2, 1, 15, 9)
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
def rotations():
    return leftm.rotations + rightm.rotations / 2
print(rotations())
gs.reset()
print(gs.angle)
#straight(3, 75, int(gs.angle), 2, 2, 2, 20)
leftm.reset()
rightm.reset()
##straight(10, 45, int(gs.angle), 2, 20, True, True)


