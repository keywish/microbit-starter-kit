import microbit
import utime
from microbit import *
display.show(Image.HAPPY)
pin2.write_digital(0)
utime.sleep_us(2)
def servo(angle):
    analog_output = 1023 * (600 + 10 * angle) / 20000
    pin0.set_analog_period(20)
    pin0.write_analog(analog_output)
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
    t2=utime.ticks_us()
    distance=((t2-t1)/10000)*340/2 
    if distance>300:
        distance=300
    return distance
while True:
    servo(0)
    display.scroll(get_chaoshengbo())
    sleep(2000)
    servo(90)
    display.scroll(get_chaoshengbo())
    sleep(2000)
    servo(180)
    display.scroll(get_chaoshengbo())
    sleep(2000)