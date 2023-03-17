import time
import tkinter as tk
import RPi.GPIO as GPIO
from PCA9685 import PCA9685
import sys


pwm = PCA9685()##没有设置频率
pwm.setPWMFreq(50)
root = tk.Tk()
root.title("direction")
root.geometry("500x500")
LONG_CLICK = 1.0
mark = None
i = 90
j = 90
pwm.setRotationAngle(1, i)
pwm.setRotationAngle(0, j)


def on_button_down(event):
    print("click detected")
    global start_time, timer
    start_time = time.perf_counter()
    timer = check_time()


def check_time():
    global timer
    global mark
    global i, j
    if (time.perf_counter() - start_time) < LONG_CLICK:
        timer = root.after(10, check_time)
    else:
        if i >= 10 and i < 170:
            i = i + 1
            print(i, j)
            pwm.setRotationAngle(1, i)
            mark is True
        timer = root.after(10, check_time)

        
def on_button_up(event):
    global timer, mark
    mark is None
    if timer:
        root.after_cancel(timer)
        print("released")


def on_button_down_r(event):
    global start_time, timer
    start_time = time.perf_counter()
    timer = check_time_r()
    print("click detected")


def check_time_r():
    global timer
    global mark
    global i, j
    if (time.perf_counter() - start_time) < LONG_CLICK:
        timer = root.after(10, check_time_r)
    else:
        if i > 10 and i <= 170:
            i = i - 1
            print(i, j)
            pwm.setRotationAngle(1, i)
            mark is True
        timer = root.after(10, check_time_r)


def on_button_up_r(event):
    global timer, mark
    mark is None
    if timer:
        root.after_cancel(timer)
        print("released")


def on_button_down_u(event):
    global start_time, timer
    start_time = time.perf_counter()
    timer = check_time_u()
    print("click detected")


def check_time_u():
    global timer
    global mark
    global j, i
    if (time.perf_counter() - start_time) < LONG_CLICK:
        timer = root.after(10, check_time_u)
    else:
        if j >= 10 and j < 170:
            j = j + 1
            print(i, j)
            mark is True
            pwm.setRotationAngle(0, j)
        timer = root.after(10, check_time_u)


def on_button_up_u(event):
    global timer, mark
    mark is None
    if timer:
        root.after_cancel(timer)
        print("released")


def on_button_down_d(event):
    global start_time, timer
    start_time = time.perf_counter()
    timer = check_time_d()
    print("click detected")


def check_time_d():
    global timer
    global mark
    global j, i
    if (time.perf_counter() - start_time) < LONG_CLICK:
        timer = root.after(10, check_time_d)
    else:
        if j > 10 and j <= 170:
            j = j - 1
            print(i, j)
            mark is True
            pwm.setRotationAngle(0, j)
        timer = root.after(10, check_time_d)


def on_button_up_d(event):
    global timer, mark
    mark is None
    if timer:
        root.after_cancel(timer)
        print("released")


def left():
    global mark, i, j
    if mark is True:
        print("long")
    else:
        if i >= 10 and i < 170:
            i = i + 10
            print(i, j)
            pwm.setRotationAngle(1, i)


def right():
    global mark, i, j
    if mark is True:
        print("long")
    else:
        if i > 10 and i <= 170:
            i = i - 10
            print(i, j)
            pwm.setRotationAngle(1, i)


def up():
    global mark, i, j
    if mark is True:
        print("long")
    else:
        if j >= 10 and j < 170:
            j = j + 10
            print(i, j)
            pwm.setRotationAngle(0, j)


def down():
    global mark, i, j
    if mark is True:
        print("long")
    else:
        if i > 10 and i <= 170:
            j = j - 10
            print(i, j)
            pwm.setRotationAngle(0, j)

            
btl = tk.Button(root, width=10, height=2, text='左', command=left)
btl.pack()
btl.bind('<ButtonPress-1>', on_button_down)
btl.bind('<ButtonRelease-1>', on_button_up)


btr = tk.Button(root, width=10, height=2, text='右', command=right)
btr.pack()
btr.bind('<ButtonPress-1>', on_button_down_r)
btr.bind('<ButtonRelease-1>', on_button_up_r)


btu = tk.Button(root, width=10, height=2, text='上', command=up)
btu.pack()
btu.bind('<ButtonPress-1>', on_button_down_u)
btu.bind('<ButtonRelease-1>', on_button_up_u)


btd = tk.Button(root, width=10, height=2, text='下', command=down)
btd.pack()
btd.bind('<ButtonPress-1>', on_button_down_d)
btd.bind('<ButtonRelease-1>', on_button_up_d)

root.mainloop()

   
