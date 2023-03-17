#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from PCA9685 import PCA9685
import pygame
import sys
pygame.init()
pwm = PCA9685()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("pygame")
try:
    print ("This is a PCA9685 routine")
    pwm.setPWMFreq(50)
    i=10
    pwm.setRotationAngle(1, i)
    j=10
    pwm.setRotationAngle(0, j)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exit")
                sys.exit()
                time.sleep(3)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('left')
                    if (i >= 0 and i <= 170):   
                        i = i+10
                        pwm.setRotationAngle(1, i)
                        time.sleep(3)
                elif event.key == pygame.K_RIGHT:
                    print('right')
                    if (i >= 10 and i <= 180):
                        i = i-10
                        pwm.setRotationAngle(1, i)
                if event.key == pygame.K_UP:
                    print("up")
                    if (j >= 0 and j <= 170):
                        j = j+10
                        pwm.setRotationAngle(0, j)
                elif event.key == pygame.K_DOWN:
                    print("down")
                    if (j >= 10 and j <= 180):
                        j = j-10
                        pwm.setRotationAngle(0, j)
except:
    pwm.exit_PCA9685()
    print ("\nProgram end")
    exit()       
        
    

    
 