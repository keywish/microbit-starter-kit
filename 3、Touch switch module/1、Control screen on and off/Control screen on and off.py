import microbit
from microbit import *
display.show(Image.HAPPY)
boat = Image("99999:99999:99999:99999:99999")
while True:
    if pin1.read_digital() is 1:
        display.show(boat)
    elif pin1.read_digital() is 0:
        display.clear()