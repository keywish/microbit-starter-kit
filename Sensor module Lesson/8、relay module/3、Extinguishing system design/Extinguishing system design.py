import microbit
import music
from microbit import *
display.show(Image.HAPPY)
while True:
    if pin1.read_digital() is 0:
        pin2.write_digital(0)
        display.show(Image.ANGRY)
        music.play('c4:1')
    elif pin1.read_digital() is 1:
        pin2.write_digital(1)