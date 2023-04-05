from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering
from ev3dev2.power import PowerSupply
#? Motorok és szenzorok importálása

from vonalKovet import *
from fordul import *
from egyenes import *
from visszaallit import *
from math import sqrt
#? Eljárások importálása

ballMotor = LargeMotor("outB")
jobbMotor = LargeMotor("outC")
yKez = MediumMotor("outA")
xKez = MediumMotor("outD")

tankMozgas = MoveTank("outB", "outC")
szogMozgas = MoveSteering("outB", "outC")
gs = GyroSensor("in2")
jobbSzenzor = ColorSensor("in3")
ballSzenzor = ColorSensor("in4")

ballSzenzor.MODE_COL_REFLECT = "COL-REFLECT"
jobbSzenzor.MODE_COL_REFLECT = "COL-REFLECT"
gs.MODE_GYRO_ANG = 'GYRO-ANG'


"""
reset(yhand, 2.5)
reset(xhand, 1.1)
"""

battery = PowerSupply()
feszultsegValtozo = (battery.measured_voltage - battery.min_voltage) / (battery.max_voltage - battery.min_voltage)
print("Az akumulátor " + str(round(float(feszultsegValtozo * -100), 2)) + "%" + "-on van")
#) Kiírja az akumulátor töltöttségét

#! Visszaállítja a alap pozicóba a karokat, kaparásveszély

def futas1():

    #gs.reset()
    kezdoIdo = time()

    egyenes(2.69, 60, 3, 1.4, 20)
    xKez.on_for_rotations(90, -1)
    #) Első víz cellához odamegy és mögé viszi a vízszintes kart

    egyenes(1.8, -60, 3, 1.4, 20)
    yKez.on_for_rotations(90, 0.4, False, False)
    #) Hátramegy, és ezáltal a home-ba behozza a kék cellát 

    egyenes(2.08, 60, 3, 1, 20)
    yKez.on_for_rotations(100, 1)
    xKez.on_for_rotations(90, 0.7)
    egyenes(0.2, -20, 0, 1.2, 20)
    #) Odamegy a vízerőműhöz, és a zöld cella fölé viszi a kart, és felemeli, ezáltal kigurl a zöld cella, utána picit hátramegy

    sleep(0.6) 
    #! Megvárjuk, hogy visszaguruljon a zöld a cella

    fordul(44, 45, 0.3, 0.5, relativ=False, motorLe=20)
    #) Ráfordul a dobozra


    xKez.on_for_rotations(-50, 0.8, False, False)
    yKez.on_for_rotations(10, 0.4, False, False)
    egyenes(4, 70, 50, 1, 20)
    #) Odamegy dobozhoz, közben elhúzza, mert nekimenne a kútnak a kart.

    yKez.on_for_rotations(45, -1.7)
    #) Leengedi a kart, és a pöcök belemegy a doboz piros részébe

    egyenes(1.25, -30, 51, 1.2, 10)
    #) Odamegy olajkút mellé

    raiseSpeed = 100
    raiseHeight = 0.8
    xKez.on_for_rotations(raiseSpeed, 0.45)
    #) a vízszintes kart behúzza az olajkút karja alá


    yKez.on_for_rotations(raiseSpeed, raiseHeight + 0.2)
    yKez.on_for_rotations(raiseSpeed, -raiseHeight)
    yKez.on_for_rotations(raiseSpeed, raiseHeight)
    yKez.on_for_rotations(raiseSpeed, -raiseHeight)
    yKez.on_for_rotations(raiseSpeed, raiseHeight)
    yKez.on_for_rotations(raiseSpeed, -raiseHeight)
    yKez.on_for_rotations(raiseSpeed, raiseHeight)
    yKez.on_for_rotations(raiseSpeed, (-1 * (raiseHeight + 0.1)))
    xKez.on_for_rotations(-10, 0.5, False, False)
    #) Kiszedi az olajat a kútból

    egyenes(2.5, -90, int(gs.angle) - 20, 1.5, 20, motorLe=-90)
    egyenes(2.5, -90, int(gs.angle) - 5, 1.2, 20, gyorsuljon=False)
    #) Hazajön miközben lefelé viszi karját

    print("Kész az 1. futás " + str(round(float(time() - kezdoIdo), 2)) + "mp alatt")

    visszaallit(xKez, 1.1)
    #) Visszaállítja vertikálisan mozgó kart

    yKez.stop()
    tankMozgas.stop()
    
    yKez.on_for_rotations(80, 1.8)
    #) Felemeli függőleges kart a következő futáshoz

def futas2():

    #gs.reset()

    egyenes(1.69, 80, int(gs.angle) + 3.5, 0.5, 5)
    #) Előre megy a kocsihoz

    yKez.stop()
    yKez.on_for_rotations(-70, 1.8, False)
    #) Leengedi a kezet hogy belemenjen a kamion elejébe

    egyenes(3.2, -80, int(gs.angle)+20, 0.5, 20)
    
    #) Hátramegy és reseteli a kezet

def futas3(): 

    #m.reset()
    #gs.reset()
    #kezdoIdo = time()
    yKez.on_for_rotations(30, 1.2, True, False)


    egyenes(5.1, 70, 3, 0.98, 5, motorLe=30)
    egyenes(2.45, 70, 26, 0.2, 30)
    fordul(-15, 40, 0.6, 0.2, relativ=False, idotullepes=1)
    egyenes(0.5, 45, -10, 0.2, 10)
    fordul(-60, 20, 0.6, 0.3, relativ=False, idotullepes=1)
    egyenes(0.5, 40, -60, 0.2, 25, motorLe=30)
    egyenes(1.2, 30, -60, 0.2, 25, gyorsuljon=False)
    #) a három kapszula összegyűjtése

    yKez.on_for_rotations(40, 1, True, False)
    fordul(40, 10, 0.3, 0.6, idotullepes=1)
    m.on_for_rotations(-25, -25, 0.05)
    fordul(-115, 20, 0.4, 0.5)
    egyenes(0.05, 10, gs.angle, 1, 5)
    egyenes(1.5, -75, -180, 0.6, 70)
    sleep(0.05)
    gs.reset()
    sleep(0.05)
    yKez.on_for_rotations(-70, 2.3)
    yKez.on_for_rotations(70, 0.09)
    egyenes(0.2, 30, 0, 1, 10, motorLe=30)
    #* a falazás megvan

    
    egyenes(2.1, 50, 32, 1.1, 30, motorLe=40)
    #egyenes(0.9, 30, 35, 1, 20, motorLe=30)
    
    #egyenes(0.3, 30, 10, 0.8, 20, motorLe=30)
    #gyenes(1, 50, 30, 0.8, 30)
    egyenes(1.8, 50, 15, 0.5, 5, gyorsuljon=False)
    #) három kapszula körbe helyezése

    yKez.on_for_rotations(40, 1.2, block = False)
    egyenes(0.93, -30, int(gs.angle)+75, 1, 20)
    fordul(27, 10, 0.7, 0.4, relativ=False)
    yKez.on_for_rotations(-40, 1.3)
    yKez.on_for_rotations(40, 0.1)
    egyenes(2, 15, 35, 1, 10, True, False)
    egyenes(0.38, 40, 35, 1, 20)
    #) megáll a vonalra az erőmű felé

    fordul(2, 30, 0.3, 1, relativ=False)
    egyenes(0.9, 30, 0, 1, 20)
    yKez.on_for_rotations(37, 2.1, block=False)
    egyenes(0.4, 30, 0, 1, 5)

    egyenes(0.3, 25, 0, 1, 10)

    yKez.on_for_rotations(-100, 2.2, block=True)
    sleep(1)
    egyenes(0.12, 10, 0, 1, 20)
    egyenes(0.2, -10, 0, 1, 10)
    egyenes(0.6, -100, 0, 1, 10)
    egyenes(2, 80, 75, 1, 20, motorLe=70)
    egyenes(6, 80, 100, 1, 20, gyorsuljon=False)
    m.stop()
    
    yKez.on_for_rotations(-100, 0.1)

def futas4():
    yKez.on_for_rotations(10, 0.04, True, False)
    #gs.reset()
    #? Elmenti a futás kezdetének idejét, így a végén ki lehet számolni, hogy mennyi időbe telt a futás.

    egyenes(2.8, 70, 0, 1.2, 20, motorLe=25)
    egyenes(0.7, 25, 0, 0.8, 15)
    #) Nekimegy a kanapénak, a végén már lassabban

    egyenes(1, -60, 0, 1.2, 20)
    #) Hátramegy egy picit, hogy ne menjen neki a kanapénak ha elindul előre

    fordul(35, 70, 0.6, 0.4, relativ=False, idotullepes=1.2)
    
    egyenes(1.5, 50, 23, 0.8, 5, motorLe=40)
    
    egyenes(1, 50, 43, 1.4, 5, gyorsuljon=False, motorLe=50)
    xKez.on_for_rotations(-27, 1, True, False)
    egyenes(1.25, 50, 43, 1.4, 5, gyorsuljon=False, motorLe=15)
    
    
    egyenes(0.7, 15, 43, 0.4, 5, gyorsuljon=False)

    #) Ráfordul és odamegy a felfüggesztett kocsihoz

    yKez.on_for_rotations(100, 0.5, True, False)
    
    #) Felemeli a kart, és ezáltall lerakja a kamiont

    egyenes(0.4, -90, 45, 0.6, 40)
    sleep(0.5)
    fordul(60, 70, 0.8, 0.5, relativ=False, idotullepes=1)
    xKez.on_for_rotations(100, 1, True, False)
    yKez.on_for_rotations(100, 1, True, False)
    egyenes(0.1, -30, 45, 0.6, 10)
    
    

    
    #) Hátramegy és közben leviszi a kart újra, különben nem tudja a rávezetőt használni

    fordul(-45, 10, 0.3, 0.2, relativ=False)
    yKez.on_for_rotations(-70, 1.48, True, False)
    egyenes(2.4, 70, -43, 1.2, 30)
    
    #) Ráfordul és nekimegy a szélturbina piros pöckének
    sleep(0.1)
    egyenes(0.25, -35, gs.angle, 0.8, 50)
    sleep(0.2)
    m.on_for_rotations(45, 45, 0.85)
    #egyenes(0.85, 45, gs.angle, 0.9, 35)

    sleep(0.1)
    egyenes(0.25, -35, gs.angle, 0, 50)
    sleep(0.2)
    egyenes(0.85, 45, gs.angle, 0, 30)
    #) Nekimegy még kétszer, hogy kiszedje mind a három cellát

    sleep(0.2)
    egyenes(0.25, -35, gs.angle, 0, 50)
    sleep(0.2)
    egyenes(0.85, 45, gs.angle, 0, 30)
   
    #! Plusz nekimenés a biztonság kedvéért

    yKez.on_for_rotations(-100, 0.1, True, False)
    egyenes(2.4, -45, -52, 1.4, 20, motorLe=-15)
    egyenes(0.6, -15, -52, 1.4, 15)
    #) Nekimegy a piros gyűjtőnek, és belerakja a 3 cellát

    egyenes(0.7, 45, int(gs.angle), 1.4, 20)

    fordul(-230, 35, 0.3, 0.4, relativ=False)
    #) Előremegy, egy picit, hogy legyen helye, és megfordul 180 fokban
    
    yKez.on_for_rotations(100, 0.7, True, False)
    xKez.on_for_rotations(-100, 1)
    egyenes(0.2, 10, int(gs.angle), 1.4, 10)
    yKez.on_for_rotations(100, 0.7, True)
    #) Előremegy enyhén és kiengedi az energia cellákat

    """
    egyenes(0.3, 10, int(gs.angle), 1.4, 10)
    
    #) Picit nekimegy a celláknak, mivel lehet hogy rajta van a határon, vagy arrafelé gurul
    # """

    egyenes(0.4, -25, int(gs.angle), 1.4, 20)
    egyenes(5, 100, -150, 1.4, 20)
    #) Hazajön a robot

    yKez.on_for_rotations(-100, 1.5)
    yKez.on_for_rotations(100, 1.8)
    #) Felemelve hagyja a kart az 5. futáshoz. 

"""    print("Kész a 4. futás " + str(round(float(time() - startTime), 2)) + "mp alatt")
"""
def futas5():
    #gs.reset()
    #startTime = time()
    
    egyenes(6.3, 70, -5, 0.9, 10)
    #) Odamegy a körbe

    yKez.on_for_rotations(100, 1.2, True)
    yKez.on_for_rotations(-15, 1.2, True, False)
    egyenes(3, 50, 0, 1.35, 10)
    #) Felemeli a függőleges kart, és utána nagyon lassan elkedzi leengedni,
    #) viszont el is indul lefelé, ezért otthagyyja az inovációs projektet

    
    yKez.on_for_rotations(-70, 2.1)
    sleep(0.5)
    egyenes(1, -70, 0, 1.35, 20,)
    #) Belemegy a vízerőműbe, leengedi a kart és a 3 cellát bennehagyja a körben, utána egy picit hátramegy

    egyenes(10, 90, 50, 1.35, 20)
    #) Hazamegy
    
    #print("Kész az 5. futás " + str(round(float(time() - startTime), 2)) + "mp alatt")

#xKez.on_for_rotations(-20, 0.5)
#xKez.on_for_rotations(20, 0.5)



"""try:  
    input("ready?:")
    sTime = time()
    gs.reset()
    futas4()
    m.stop()
    m.reset()
    yKez.reset()
    xKez.reset()
except KeyboardInterrupt:
    m.stop()
    m.reset()
    yKez.reset()
    xKez.reset()
    print("\n")
    try:
        print(str(round(float(time() - sTime), 2)) + "mp volt")
    except:
        pass"""


"""gs.reset()
while True:
    gyroSensi = float(input("Mi legyen a KP?: "))
    gs.reset()
    gs.calibrate()
    sleep(0.1)
    print(gs.angle)
    egyenes(4, 10, gs.angle, gyroSensi, 10)
    egyenes(4, -10, gs.angle, gyroSensi, 10)
    #1.4"""


