import microbit
from microbit import *
while True:
    display.show(Image.HAPPY)
    if pin1.read_digital() is 0:
        display.show('1')
        sleep(1000)
        display.show(Image.HAPPY)
    elif pin2.read_digital() is 0:
        display.show('2')
        sleep(1000)
        display.show(Image.HAPPY)
    elif pin8.read_digital() is 0:
        display.show('3')
        sleep(1000)
        display.show(Image.HAPPY)
    elif pin12.read_digital() is 0:
        display.show('4')
        sleep(1000)
        display.show(Image.HAPPY)
    else :
        pass