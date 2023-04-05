#!/usr/bin/env micropython
from ev3dev2.button import Button
from ev3dev2.console import Console
from ev3dev2.sensor.lego import GyroSensor, ColorSensor
from ev3dev2.sound import Sound
from ev3dev2 import DeviceNotFound
from os import system
konzol = Console()
konzol.set_font(font='Lat15-TerminusBold14', reset_console=False)

try: 
    gs = GyroSensor("in1")
except DeviceNotFound:
    konzol.text_at("|X| Gyroscope IN:2", column=1, row=1, reset_console=False, inverse=True)
else:
    konzol.text_at("Gyroscope IN:2", column=1, row=1, reset_console=False, inverse=True)

try: 
    gs = ColorSensor("in1")
except DeviceNotFound:
    konzol.text_at("☒ Colorsensor IN:3", column=1, row=2, reset_console=False, inverse=True)
else:
    konzol.text_at("☑ Colorsensor IN:3", column=1, row=2, reset_console=False, inverse=True)

try: 
    gs = ColorSensor("in1")
except DeviceNotFound:
    konzol.text_at("☒ Colorsensor IN:4", column=1, row=3, reset_console=False, inverse=True)
else:
    konzol.text_at("☑ Colorsensor IN:4", column=1, row=3, reset_console=False, inverse=True)



from kalibral import *
from futas import *
