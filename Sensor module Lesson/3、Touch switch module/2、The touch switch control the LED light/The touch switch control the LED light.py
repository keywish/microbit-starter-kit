import microbit
from microbit import *
display.show(Image.HAPPY)
sign = 1
while True:
    if pin1.read_digital() is 1:
        if sign is 1:
            sign = 0
            pin2.write_digital(0)
        else:
            sign = 1
            pin2.write_digital(1)
        sleep(1000)