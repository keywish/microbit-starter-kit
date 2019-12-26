from microbit import *
while True:
    if temperature() > 35 or temperature() <10:
        display.show(Image.ASLEEP)
    else :
        display.show(Image.HAPPY)