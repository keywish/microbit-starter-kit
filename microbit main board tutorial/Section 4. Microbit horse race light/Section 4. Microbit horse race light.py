import microbit  
from microbit import *
display.show(Image.HAPPY)
sleep(200)
display.clear()
boat1 = Image("00700:00000:00000:00000:00000")
boat2 = Image("00000:00700:00000:00000:00000")
boat3 = Image("00000:00000:00700:00000:00000")
boat4 = Image("00000:00000:00000:00700:00000")
boat5 = Image("00000:00000:00000:00000:00700")
all_boat = [boat1,boat2,boat3,boat4,boat5]
while True:
    display.show(all_boat,delay = 100)