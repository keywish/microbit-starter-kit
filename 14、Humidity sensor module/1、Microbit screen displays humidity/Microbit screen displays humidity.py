import microbit
from microbit import *
display.show(Image.HAPPY)
while True:
    temp = pin2.read_analog()//5
    display.scroll(temp)