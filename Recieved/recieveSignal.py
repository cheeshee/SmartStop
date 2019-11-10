import pygame
from time import sleep
from pygame.locals import*

pygame.init()        
flash = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/flash.jpg')
noFlash = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/noFlash.jpg')
WIDTH = 800
HEIGHT = 480
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)


# 0 flash       to stop
# 1 no flash    to go
def chooseIm(num):
    if (num == 0):
        windowSurface.blit(flash, (0,0))
    elif (num == 1):
        windowSurface.blit(noFlash, (0,0))
    sleep(0.5)

    

chooseIm(0)
