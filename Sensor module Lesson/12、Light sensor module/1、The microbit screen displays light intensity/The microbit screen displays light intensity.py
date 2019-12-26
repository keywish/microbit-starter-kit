import microbit
from microbit import *
display.show(Image.HAPPY)
while True:
    display.scroll(pin1.read_analog())