import microbit
import music
from microbit import *
display.show(Image.HAPPY)
sleep(100)
display.clear()
while True:
    if button_a.was_pressed():
        music.play(music.BIRTHDAY)
    elif button_b.was_pressed():
        music.play(music.BLUES)