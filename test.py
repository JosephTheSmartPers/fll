from time import time
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MediumMotor
import time
print("ready")
m = MediumMotor(OUTPUT_A)

m.on_for_rotations(70, 0.4, False, False)
m.off(False)