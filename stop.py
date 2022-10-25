from ev3dev2.motor import OUTPUT_C, OUTPUT_B, MoveTank
print("ready")
m = MoveTank(OUTPUT_B, OUTPUT_C)
m.stop()