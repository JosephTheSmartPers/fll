from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.sound import Sound
from ev3dev2.sensor import *
gs = GyroSensor("in4")
spkr = Sound()
m = MoveTank(OUTPUT_A, OUTPUT_D)
gs.MODE_GYRO_ANG = 'GYRO-ANG'
gs.reset()
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
  
turn(-90, 50, 0.75)
"""300 *100"""