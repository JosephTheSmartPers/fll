from ev3dev2.motor import OUTPUT_D, OUTPUT_D, MediumMotor
print("ready")
m = MediumMotor(OUTPUT_D)
m.on_for_rotations(100, 100, 10)