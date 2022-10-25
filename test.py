from ev3dev2.motor import OUTPUT_C, OUTPUT_D, MoveTank
print("ready")
m = MoveTank(OUTPUT_C, OUTPUT_D)
m.on_for_rotations(100, 100, 10)