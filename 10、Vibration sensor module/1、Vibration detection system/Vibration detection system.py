import microbit
import music
from microbit import *
display.show(Image.HAPPY)
while True:
    if pin2.read_digital() is 1:
        sign = 1
        while sign == 1:
            music.play('c4:1')
            if button_a.is_pressed():
                sign = 0