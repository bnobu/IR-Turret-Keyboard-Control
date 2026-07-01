#!/usr/bin/env python3

import serial
import keyboard
import time

PORT = "/dev/ttyUSB0"   # Change this
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

print("Controls:")
print("  ↑ = UP")
print("  ↓ = DOWN")
print("  ← = LEFT")
print("  → = RIGHT")
print("  F = FIRE")
print("  R = RAPID FIRE")
print("  Esc = Quit")

last = {}

def send(cmd):
    ser.write((cmd + "\n").encode())
    print(cmd)

while True:
    if keyboard.is_pressed("up"):
        if not last.get("up"):
            send("UP")
            last["up"] = True
    else:
        last["up"] = False

    if keyboard.is_pressed("down"):
        if not last.get("down"):
            send("DOWN")
            last["down"] = True
    else:
        last["down"] = False

    if keyboard.is_pressed("left"):
        if not last.get("left"):
            send("LEFT")
            last["left"] = True
    else:
        last["left"] = False

    if keyboard.is_pressed("right"):
        if not last.get("right"):
            send("RIGHT")
            last["right"] = True
    else:
        last["right"] = False

    if keyboard.is_pressed("f"):
        if not last.get("f"):
            send("FIRE")
            last["f"] = True
    else:
        last["f"] = False

    if keyboard.is_pressed("r"):
        if not last.get("r"):
            send("FIREALL")
            last["r"] = True
    else:
        last["r"] = False

    if keyboard.is_pressed("esc"):
        break

    time.sleep(0.01)

ser.close()
