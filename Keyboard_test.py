import random, sys, time, math, pygame, Car
from pygame.locals import *

myCar = Car()
forward = False
backward = False
moveLeft = False
moveRight = False
pera = 0

def terminate():
    myCar.neutral()
    pygame.quit()
    sys.exit()

while (1):
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            terminate()

        elif event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                if(pera < 0):
                    pera = 0
                else
                    pera += 10
            elif event.key in (K_DOWN, K_s):
                if(pera > 0):
                    pera = 0
                else           
                    pera -= 10
            elif event.key in (K_LEFT, K_a):
                moveLeft = True
            elif event.key in (K_RIGHT, K_d):
                moveRight = True
            elif event.key == K_ESCAPE:
                terminate()

    if(pera > 0):
        forward = True
        backward = False
        neutral = False
    elif(pera < 0):
        backward = True
        forward = False
        neutral = False
    elif(pera == 0):
        neutral = True
        backward = False
        forward = False

    if (forward): 
        myCar.forward(pera)
    if (backward):
        myCar.reverse(pera)
    if (neutral):
        myCar.neutral()