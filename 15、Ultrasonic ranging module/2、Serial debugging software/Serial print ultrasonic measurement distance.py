import microbit
from microbit import *
import utime
display.show(Image.HAPPY)
uart.init(115200)
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
    t2=utime.ticks_us()
    shuju=((t2-t1)/10000)*340//2
    if shuju>300: 
        shuju=300
    return shuju
while True:
    uart.write(str(get_chaoshengbo())) 
    uart.write('   ')   
    sleep(1000)