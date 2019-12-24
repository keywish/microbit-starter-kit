import microbit
import music
from microbit import *
display.show(Image.MUSIC_QUAVERS)
while True:
    if pin1.read_digital() is 0:
        music.play('a4:1')
        sleep(10)
    elif pin2.read_digital() is 0:
        music.play('b4:1')
        sleep(10)
    elif pin8.read_digital() is 0:
        music.play('c4:1')
        sleep(10)
    elif pin12.read_digital() is 0:
        music.play('d4:1')
        sleep(10)