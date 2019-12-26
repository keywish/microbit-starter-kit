import microbit
from microbit import *
from random import randint
display.show(Image.HAPPY)
sleep(100)
while True:
    if button_a.was_pressed():
        x = randint(0,9)
        display.show(str(x))
        sleep(500)
        display.show(Image.ARROW_E)
    elif button_b.was_pressed():
        x = randint(0,9)
        display.show(str(x))
        sleep(500)
        display.show(Image.ARROW_W)