import pygame
from time import sleep
from pygame.locals import*

WIDTH = 800
HEIGHT = 480
pygame.init()
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)flash = pygame.Color(255,0,0)
noFlash = pygame.Color(0,0,0)

# flashing alternates to flash colors
flashing = 0

# 0 flash       to stop
# 1 no flash    to go
def chooseIm(num):
    global flashing
    if (num == 0 and flashing == 0):
        windowSurface.fill(flash)
        flashing = 1
    elif (num == 0 and flashing == 1):
        windowSurface.fill(noFlash)
        flashing = 0
    elif (num == 1):
        windowSurface.fill(noFlash)
        flashing = 0
    sleep(0.5)



test = [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0]
for x in test
    chooseIm(x)

myfile = open("sign.txt", "rt")
signal = myfile.read()
myfile.close()
chooseIm(signal)
