import microbit
from microbit import *
sleep(200)
display.show(Image.HAPPY)
compass.calibrate()
while True:
    if compass.heading() > 260 and compass.heading() < 280:   #compass.heading()函数会返回microbit指南针所指向方向的一个数值，不同的方向数值不同
        display.show("W")
    elif compass.heading() > 170 and compass.heading() < 190:
        display.show("S")
    elif compass.heading() > 80 and compass.heading() < 100:
        display.show("E")
    elif compass.heading() > 350 or compass.heading() < 10:
        display.show("N")
    else:
        display.clear()