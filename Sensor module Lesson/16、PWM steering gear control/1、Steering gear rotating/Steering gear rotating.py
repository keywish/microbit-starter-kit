import microbit
import utime
from microbit import *
display.show(Image.HAPPY)
pin2.write_digital(0)
utime.sleep_us(2)
def servo(angle):
    analog_output = 1023 * (600 + 10 * angle) / 20000      #根据角度计算出占空比的量
    pin0.set_analog_period(20)
    pin0.write_analog(analog_output)
while True:
    servo(0)
    sleep(2000)
    servo(90)
    sleep(2000)
    servo(180)
    sleep(2000)