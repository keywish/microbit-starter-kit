import radio
from microbit import *
radio.on()
while True:
    if button_a.was_pressed():
        radio.send('A')
    if button_b.was_pressed():
        radio.send('B')
    incoming = radio.receive()
    if incoming == 'A':
        display.show("A")
    if incoming == 'B':
        display.show("B")