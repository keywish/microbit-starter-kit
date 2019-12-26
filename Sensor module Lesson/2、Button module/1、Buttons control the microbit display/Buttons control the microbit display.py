import microbit
from microbit import *
display.show(Image.HAPPY)
a=0
while True:
    if pin1.read_digital():
        if a==1:
            display.show(Image.NO)
            a=0
            sleep(200)
        elif a==0:
            display.show(Image.YES)
            a=1
            sleep(200)