import microbit
from microbit import *
display.show(Image.HAPPY)
sleep(1000)
while True:
    display.scroll(pin1.read_analog())
    sleep(100)