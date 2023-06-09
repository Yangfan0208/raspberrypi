#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from PCA9685 import PCA9685
import keyboard
import sys
pwm = PCA9685()
try:
    print ("This is a PCA9685 routine")
    pwm.setPWMFreq(50)
    i=10
    pwm.setRotationAngle(1, i)
    j=10
    pwm.setRotationAngle(0, j)
    while True:
                if keyboard.read_key() == "left":
                    print('left')
                    if (i >= 0 and i <= 170):   
                        i = i+10
                        pwm.setRotationAngle(1, i)
                elif keyboard.read_key() == "right":
                    print('right')
                    if (i >= 10 and i <= 180):
                        i = i-10
                        pwm.setRotationAngle(1, i)
                if keyboard.read_key() == "up":
                    print("up")
                    if (j >= 0 and j <= 170):
                        j = j+10
                        pwm.setRotationAngle(0, j)
                elif keyboard.read_key() == "down":
                    print("down")
                    if (j >= 10 and j <= 180):
                        j = j-10
                        pwm.setRotationAngle(0, j)
except:
    pwm.exit_PCA9685()
    print ("\nProgram end")
    exit()       
        
