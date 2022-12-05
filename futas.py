from ev3dev2.sensor.lego import * 
from ev3dev2.sensor import *
from ev3dev2.motor import *
from straight import *
leftm = LargeMotor(OUTPUT_B)
rightm = LargeMotor(OUTPUT_C)
hand = MediumMotor(OUTPUT_A)

m = MoveTank(OUTPUT_B, OUTPUT_C)
s = MoveSteering(OUTPUT_B, OUTPUT_C)
gs = GyroSensor(INPUT_2)
rs = ColorSensor("in3")
ls = ColorSensor("in4")

ls.MODE_COL_REFLECT = "COL-REFLECT"
rs.MODE_COL_REFLECT = "COL-REFLECT"
gs.MODE_GYRO_ANG = 'GYRO-ANG'

#Turning
########################################################################################################
def turn(degree, speed, acceleration, time):
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
            print(spd)
    m.stop()
    normal = gs.angle
  

#Line following
########################################################################################################
def getRotations():
    return (leftm.rotations + rightm.rotations) / 2
    
def calcDegree(lightIntensity, goodLight, sensitivity, maxSpeed):
        spd = (goodLight-lightIntensity) * -sensitivity

        if(abs(spd) > maxSpeed):
            spd = maxSpeed * (spd / abs(spd))

        return(spd)

def followLine(sensitivity, distance, maxSpeed, goodLight, sensor = False, straight = False):
        m.on(20,20)
        straight = True
        while straight == True:
            if(ls.reflected_light_intensity < 60):
                straight = False
                startRotation = getRotations()
                while startRotation + distance > getRotations():
                    if(sensor != False):
                        s.on(calcDegree(sensor.reflected_light_intensity, goodLight, sensitivity, maxSpeed), maxSpeed)
                    else:
                        leftm.on(maxSpeed-calcDegree(ls.reflected_light_intensity, goodLight, sensitivity, maxSpeed))
                        rightm.on(maxSpeed-calcDegree(rs.reflected_light_intensity, goodLight, sensitivity, maxSpeed))
                m.stop() 
########################################################################################################

gs.reset()
hand.on_for_rotations(50, 1)
straight(2.8, 45, int(gs.angle) + 1.73, 2, 20)
hand.on_for_rotations(30, -1)
straight(2.8, 45, int(gs.angle), 2, 20)