from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveTank, MediumMotor, OUTPUT_A, OUTPUT_D
from reset import *
print("ready")
m = MoveTank(OUTPUT_B, OUTPUT_C)
m.stop()
yhand = MediumMotor(OUTPUT_A)
xhand = MediumMotor(OUTPUT_D)
reset(yhand)
reset(xhand)
xhand.reset()
yhand.reset()