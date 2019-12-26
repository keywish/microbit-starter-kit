import microbit
from microbit import *
display.show(Image.HAPPY)
while True:
    pin2.write_analog(1024-pin1.read_analog())