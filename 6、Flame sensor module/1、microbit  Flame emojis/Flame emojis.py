import microbit
import music
from microbit import *
display.show(Image.HAPPY)
while True:
    if pin2.read_digital() is 0:
        display.show(Image.ANGRY)
        music.play('f4:1')
    elif pin2.read_digital() is 1:
        display.show(Image.HAPPY)