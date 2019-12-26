from microbit import *
while True:
    display.scroll(str(temperature()))
    sleep(100)