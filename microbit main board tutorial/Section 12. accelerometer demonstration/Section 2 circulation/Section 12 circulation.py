import microbit
from microbit import *
image1 = Image("70070:77077:00000:07770:70007")
image2 = Image("77077:70070:00000:07770:70007")
image3 = Image("77077:07007:00000:07770:70007")
image4 = Image("07007:77077:00000:07770:70007")
image5 = Image("77077:77077:00000:07770:70007")
image6 = Image("00000:09090:00000:07770:70007")
all_image1 = [image1,image2,image3,image4]
all_image2 = [image5,image6]
while True:
    if accelerometer.get_x() < 500 and accelerometer.get_x() > -500:
        display.show(Image.HAPPY)
    if accelerometer.get_x() > 500 or accelerometer.get_x() < -500:
        if accelerometer.get_y() > 500 or accelerometer.get_y() < -500:
            for i in range(1,3):
                display.show(all_image1,delay=500)
            display.show(all_image2,delay=500)
            display.show(all_image2,delay=500)