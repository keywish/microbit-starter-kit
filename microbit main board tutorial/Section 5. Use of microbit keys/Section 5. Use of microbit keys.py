import microbit
from microbit import *
display.show(Image.HAPPY)
sleep(100)
while True:
    if button_a.was_pressed():
        if button_b.was_pressed():
            display.show("C")
        else :
            display.show("A")
    elif button_b.was_pressed():
        if button_a.was_pressed():
            display.show("C")
        else :
            display.show("B")