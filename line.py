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

def followLine(sensitivity, distance, maxSpeed, goodLight, sensor = False, straight = False):
        m.on(20,20)
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



