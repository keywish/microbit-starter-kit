'''本次实验包含四个函数，up_down(),down_up(),leftdown_rightup(),leftup_rightdown()
   在学习的过程中，四个函数单独分析学习，然后再学习循环的部分，
'''
import microbit   #调用microbit包
import neopixel   #调用多彩灯文件包
from random import randint   #调用随机函数
from microbit import *   #使用microbit所有文件
np = neopixel.NeoPixel(pin2,13)   #设置接在pin2引脚的RGB灯数量为13个（实际只有12个，之所以设置为13个是为了扩容np的容量），让变量np代表
display.show(Image.HAPPY)
def up_down():  #从上向下点亮RGB灯圈函数
    right = 6   #设置右边RGB位置控制变量
    left  = 6   #设置左边RGB位置控制变量
    for i in range(0, 7):   #循环7次
        red   = randint(0,150)   #为red赋一个在0~150之间的随机值
        green = randint(0,150)
        blue  = randint(0,150)
        np[right] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np[left] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np.show()  #刷新显示，点亮RGB灯
        right = right + 1   #改变RGB灯位置
        left  = left  - 1
        sleep(200)
    for j in range(0,12):   #循环12次，熄灭所有RGB灯
        np[j] = (0 ,0 ,0)
        np.show()
def down_up():  #从下向上点亮RGB灯圈函数
    right = 12
    left  = 0
    for i in range(0, 7):
        red   = randint(0,150)   #为red赋一个在0~150之间的随机值
        green = randint(0,150)
        blue  = randint(0,150)
        np[right] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np[left] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np.show()  #刷新显示，点亮RGB灯
        right = right - 1
        left  = left  + 1
        sleep(200)
    for j in range(0,12):
        np[j] = (0 ,0 ,0)
        np.show()
def leftdown_rightup():    #左边向下、右边向上点亮函数
    right = 11
    left  = 5
    np[6] = (100, 100, 100)     #位置为6的第七个RGB灯先点亮，然后再循环
    np[0] = (100, 100, 100)     #位置为0的第一个RGB灯先点亮，然后再循环
    np.show()  #刷新显示，点亮RGB灯
    sleep(200)
    for i in range(0, 6):
        red   = randint(0,150)   #为red赋一个在0~150之间的随机值
        green = randint(0,150)
        blue  = randint(0,150)
        np[right] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np[left] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np.show()  #刷新显示，点亮RGB灯
        right = right - 1
        left  = left  - 1
        sleep(200)
    for j in range(0,12):
        np[j] = (0 ,0 ,0)
        np.show()
def leftup_rightdown():   #左边向上、右边向下点亮函数
    right = 6
    left  = 0
    for i in range(0, 6):
        red   = randint(0,150)   #为red赋一个在0~150之间的随机值
        green = randint(0,150)
        blue  = randint(0,150)
        np[right] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np[left] = (red, green, blue)   #设置相应位置RGB灯的三基色
        np.show()  #刷新显示，点亮RGB灯
        right = right + 1
        left  = left  + 1
        sleep(200)
    for j in range(0,12):
        np[j] = (0 ,0 ,0)
        np.show()
while True:    #程序循环入口
    up_down()  #从上向下点亮
    down_up()  #从下向上点亮
    leftup_rightdown()   #左边向上、右边向下点亮
    leftdown_rightup()   #左边向下、右边向上点亮
