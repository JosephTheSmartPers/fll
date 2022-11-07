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

m.on(75, 75)
go = True

def stop():
    m.stop
    perfect = True 
    leftm.stop()
    rightm.stop()  

def raall(sensi, maxs, maxspd, minlight):
    maxms = float(maxs)
    now = time.time()
    print(time.time)
    leftPrev = 100
    rightPrev = 100
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
        print(str(minlight - bs.reflected_light_intensity))
        print(time.time())
        if(seconds >= maxs):
            m.stop
            perfect = True 
            leftm.stop()
            rightm.stop()

while go == True:
    if(bs.reflected_light_intensity <= 10 or rs.reflected_light_intensity <= 10):
        m.stop()
        m.on(-10, -10)
        while go == True:
            if(bs.reflected_light_intensity <= 8 or rs.reflected_light_intensity <= 8):
                m.stop()
                go = False
                raall(2.45, 2, 15, 7)