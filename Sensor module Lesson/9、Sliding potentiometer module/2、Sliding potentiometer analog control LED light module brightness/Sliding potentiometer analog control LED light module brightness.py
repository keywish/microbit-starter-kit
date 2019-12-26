import microbit
from microbit import *
display.show(Image.HAPPY)
sleep(1000)
while True:
    pin2.write_analog(pin1.read_analog())