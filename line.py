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

def getRotations():
    return (leftm.rotations + rightm.rotations) / 2
    
def calcDegree(lightIntensity, goodLight, sensitivity, maxSpeed):
        spd = (goodLight-lightIntensity) * -sensitivity

        if(abs(spd) > maxSpeed):
            spd = maxSpeed * (spd / abs(spd))

        return(spd)
        

def followLine(sensitivity, distance, maxspeed, goodLight, sensor):
    startRotation = getRotations()
    while startRotation + distance > getRotations():
        s.on(calcDegree(ls.reflected_light_intensity, goodLight, sensitivity, maxspeed), maxspeed)
    m.stop()

m.on(20,20)
straight = True
while straight == True:
    if(ls.reflected_light_intensity < 60):
        followLine(0.8, 3, 20 , 40, "left")
        straight = False


