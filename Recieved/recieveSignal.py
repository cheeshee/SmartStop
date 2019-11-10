import pygame
from time import sleep
from pygame.locals import*

pygame.init()
flash0 = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/flash0.png')
flash1 = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/flash1.png')
noFlash = pygame.image.load('/home/pi/Congested/SmartStop/Recieved/noFlash.png')
WIDTH = 800
HEIGHT = 480
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
flashing = 0

# 0 flash       to stop
# 1 no flash    to go
def chooseIm(num):
    global flashing
    if (num == 0 and flashing == 0):
        windowSurface.blit(flash0, (0,0))
        flashing = 1
    elif (num == 0 and flashing == 1):
        windowSurface.blit(flash1, (0,0))
        flashing = 0
    elif (num == 1):
        windowSurface.blit(noFlash, (0,0))
        flashing = 0
    sleep(0.5)
    pygame.display.update()

    

chooseIm(0)
