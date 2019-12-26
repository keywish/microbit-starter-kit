import microbit
import music
from microbit import *
display.show(Image.HAPPY)
while True:
    temp = pin2.read_analog()//5
    if temp > 40:
        music.play('c4:1')
        pin1.write_digital(1)
    elif temp <= 40:
        pin1.write_digital(0)