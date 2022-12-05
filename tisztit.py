from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveTank
print("ready")
m = MoveTank(OUTPUT_B, OUTPUT_C)
from straight import *
gs.reset()
straight(10, 45, int(gs.angle), 2, 20)