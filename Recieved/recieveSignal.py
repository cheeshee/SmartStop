import pygame
from time import sleep
from pygame.locals import*

pygame.init()        
flash = Image.open('flash.gif')
noFlash = Image.open('noFlash.jpg')
WIDTH = 1280
HEIGHT = 800
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)


# 0 flash       to stop
# 1 no flash    to go
def chooseIm(num):
    if (num == 0):
        window.Surface.blit(flash, (0,0))
    elif (num == 1):
        window.Surface.blit(noFlash, (0,0))
    sleep(0.5)

    

chooseIm(1)
