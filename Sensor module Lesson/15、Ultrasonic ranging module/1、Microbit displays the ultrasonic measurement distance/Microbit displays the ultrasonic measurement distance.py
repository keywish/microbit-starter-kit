import microbit
from microbit import *
import utime
display.show(Image.HAPPY)
sleep(100)
pin2.write_digital(0)
utime.sleep_us(2)
def get_chaoshengbo():
    pin1.write_digital(0)
    pin2.write_digital(1)
    utime.sleep_us(15)
    pin2.write_digital(0)
    while(pin1.read_digital() == 0):
        pass
    t1=utime.ticks_us()
    while pin1.read_digital():
        pass
    t2 = utime.ticks_us()
    distance=((t2-t1)/10000)*340/2
    if distance > 300:
        distance = 300
    return distance
while True:
    display.scroll(get_chaoshengbo())  
    display.scroll('cm')
    sleep(1000)