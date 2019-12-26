import microbit
from microbit import *
display.show(Image.HAPPY)
while True:
    if accelerometer.get_y() > 500:
        display.show(Image.ARROW_N)
        sleep(1000)
    elif accelerometer.get_y() < -500:
        display.show(Image.ARROW_S)
        sleep(1000)
    else :
        display.clear()