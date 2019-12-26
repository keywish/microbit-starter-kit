import microbit
from microbit import spi
_NOOP = 0
_DIGIT0 = 1
_DIGIT1 = 2
_DIGIT2 = 3
_DIGIT3 = 4
_DIGIT4 = 5
_DIGIT5 = 6
_DIGIT6 = 7
_DIGIT7 = 8
_DECODEMODE = 9
_INTENSITY = 10
_SCANLIMIT = 11
_SHUTDOWN = 12
_DISPLAYTEST = 15
class Matrix8x8:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.buffer = bytearray(8)
        spi.init()
        self.init()
    def _register(self, command, data):
        # write to display
        self.cs.write_digital(0)
        self.spi.write(bytearray([command, data]))
        self.cs.write_digital(1)
    def init(self):
        for command, data in ((_SHUTDOWN, 0),(_DISPLAYTEST, 0),(_SCANLIMIT, 7),(_DECODEMODE, 0),(_SHUTDOWN, 1),):
            self._register(command, data)
    def brightness(self, value):
        if not 0<= value <= 15:
            raise ValueError("Brightness out of range")
        self._register(_INTENSITY, value)
    def fill(self, color):
        data = 0xff if color else 0x00
        for y in range(8):
            self.buffer[y] = data
    def pixel(self, x, y, color=None):
        if color is None:
            return bool(self.buffer[y] & 1 << x)
        elif color:
            self.buffer[y] |= 1 << x
        else:
            self.buffer[y] &= ~(1 << x)
    def show(self):
        for y in range(8):
            self._register(_DIGIT0 + y, self.buffer[y])
def number_0():   #A function that displays' 0 '
    display.fill(False)  #All lights in the lattice are set to off
    display.pixel(1, 2, True)  #Set the lights with coordinates of (1,2) to light up
    display.pixel(1, 3, True)
    display.pixel(1, 4, True)
    display.pixel(1, 5, True)
    display.pixel(2, 2, True)
    display.pixel(3, 2, True)
    display.pixel(4, 2, True)
    display.pixel(5, 2, True)
    display.pixel(6, 2, True)
    display.pixel(6, 3, True)
    display.pixel(6, 4, True)
    display.pixel(6, 5, True)
    display.pixel(2, 5, True)
    display.pixel(3, 5, True)
    display.pixel(4, 5, True)
    display.pixel(5, 5, True)
while True:  #Start the program, infinite loop
    display = Matrix8x8(microbit.spi, microbit.pin0)  #Set CS to connect to pin0 on the IO extension board, DIN to MOSI pin on the extension board, and CLK to SCK pin on the extension board
    display.brightness(8)  #Set the brightness to 8
    number_0()  #Call the appropriate function to display the number '0'
    display.show()   #Refresh the state of the lattice, and the lights on or off in the corresponding position of the screen