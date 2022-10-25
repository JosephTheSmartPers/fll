from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank
print("ready")
m = MoveTank(OUTPUT_A, OUTPUT_D)
m.on_for_seconds(75, 75, 20)