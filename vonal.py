#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, MoveTank, MoveSteering, MediumMotor
from ev3dev2.sensor.lego import GyroSensor, ColorSensor 
import time
print("kesz az import")

gs = GyroSensor()
cs = ColorSensor()

gs.reset()

m1 = LargeMotor("outA")
m2 = LargeMotor("outD")
tank = MoveTank("outA", "outD")
tanki = MoveSteering("outA", "outD")
karle = MediumMotor("outB")
karjx = MediumMotor("outC")

def yhand(rot, spd):
    karle.on_for_seconds(rot, spd)
    time.sleep(spd)

def xhand(rot, spd, brake):
    karjx.on_for_seconds(rot, spd)
    if(brake == False):
        time.sleep(spd)
        karjx.reset()

def fordulat(szog, hbh, szorzo):
    alsohbh = hbh * -1
    difference = szog+gs.angle
    tspeed = difference * szorzo
    print(difference <= hbh and difference >=alsohbh)
    while not (difference <= hbh and difference >=alsohbh):
        tspeed = (szog-gs.angle)*-1 * szorzo
        if tspeed > 100:
            tspeed = 100
        elif tspeed < -100:
            tspeed = -100
        tank.on(tspeed, tspeed*-1)
        print(tspeed, gs.angle*-1) 
    tank.off()

def fordulat2(szog, szorzo):
    while gs.angle*-1 != szog:
        tspeed = (szog-gs.angle*-1) * szorzo
        if tspeed > 100:
            tspeed = 100
        elif tspeed < -100:
            tspeed = -100
        tank.on(tspeed*-1, tspeed)
        print(tspeed, gs.angle*-1) 
            
def vonal(foszog, tav, speed):
    m1.reset()
    m2.reset()
    gs.reset()
    fordulat(foszog, 3, 0.8)
    tav = tav*360
    szog = foszog
    poz = (m1.position + m2.position)/2
    print(poz)
    while abs(poz-tav)>100:
        print(poz)
        tanki.on(-szog*2, speed)
            
        szog = gs.angle*-1 - foszog
        
        if szog < -100:
            szog = -100
        elif szog > 100:
            szog = 100
        poz = (m1.position + m2.position)/2
    tanki.off()
    
def vonalstop(vonalszin):
    alvonal = vonalszin-5
    felvonal = vonalszin+5
    while True:
        tanki.on(0, 40)
        if cs.reflected_light_intensity >= alvonal and cs.reflected_light_intensity <= felvonal:
            tanki.off()
            break

def vonalkov():
    while True:
        tanki.on(cs.reflected_light_intensity-44, 40)
def teherrepulo():
    karle.on_for_seconds(90, 3)#3.9
    vonal(0, 4.15, 40)
    time.sleep(1)
    karle.on_for_rotations(-90, 3.9)#3.9
    karle.off(False)
    time.sleep(1)
    
    tank.on_for_rotations(-75, -75, 4.2)
    time.sleep(1)
    karle.on_for_seconds(90, 3)#3.9
    karle.reset()
    karjx.reset()
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
            tank.on(spd * -1, spd)
            print(spd)
    tank.stop()
    normal = gs.angle
  
def kakas():
    yhand(100, 1)
    xhand(100, 1, False)
    gs.reset()
    karle.on_for_seconds(-75, 0.6)
    karle.reset()

    karjx.on_for_seconds(75, 1)
    karjx.reset()
    vonal(0, 4.2, 40)
    karle.on_for_seconds(75, 0.2)
    karle.reset()
    vonal(0, 1.7, 75)
    karle.on_for_seconds(75, 2.05)
    karle.reset()
    vonal(0, 1, 75)
    karle.on_for_seconds(-75, 0.45)
    karle.reset()
    tank.on_for_rotations(-68, -75, 2.8)
    yhand(100, 0.5)
    yhand(-75, 0.25)
    xhand(-100, 1, True)
    tank.on_for_rotations(-70, -75, 4)

def kontener():
    vonal(0, 1.6, 75)
    turn(-45, 75, 0.8)
    vonal(0, 2, 75)
    
    turn(-90, 75, 0.8)
    vonal(0, 1.5, 75)
    yhand(-100, 1)
    xhand(100, 1, False)
    yhand(100, 1)
    tank.on_for_rotations(-70, -75, 0.8)
    turn(65, 75, 0.8)
    vonal(0, 2.4, 75)
    xhand(100, 1, True)
    yhand(-100, 0.3)
    turn(45, 75, 0.8)
    vonal(0, 5, 75)

xyz = True
while xyz == True:
    if(cs.color == "5" or cs.color == 5): #piros
        kakas()
        yhand(100, 1)
    elif(cs.color == "3" or cs.color == 3): #zöld
        xhand(100, 1, False)
        teherrepulo()
    elif(cs.color == "6" or cs.color == 2): #fehér
        kontener()
