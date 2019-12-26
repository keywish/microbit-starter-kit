import microbit
from microbit import *
display.show(Image.HAPPY)
while True:
    pin2.write_digital(0)
    sleep(1000)
    pin2.write_digital(1)
    sleep(1000)