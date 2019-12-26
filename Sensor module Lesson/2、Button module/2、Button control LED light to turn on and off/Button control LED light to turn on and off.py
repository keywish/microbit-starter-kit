import microbit
from microbit import *
display.show(Image.HAPPY)
while True:
    pin2.write_digital(pin1.read_digital()) 