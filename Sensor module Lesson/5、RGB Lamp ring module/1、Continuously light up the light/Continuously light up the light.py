import microbit
import neopixel
from random import randint
from microbit import *
np = neopixel.NeoPixel(pin2,12)
display.show(Image.HAPPY)
while True:
    for pixel_id in range(0,len(np)):
        red = randint(0,150)
        green = randint(0,150)
        blue = randint(0,150)
        np[pixel_id] = (red, green, blue)
        np.show()
        sleep(1000)