from PIL import Image
from time import sleep
        
flash = Image.open('flash.gif')
noFlash = Image.open('noFlash.jpg')

# 0 flash       to stop
# 1 no flash    to go
def chooseIm(num):
    if (num == 0):
        flash.show()
    elif (num == 1):
        noFlash.show()
    sleep(0.5)

    

chooseIm(1)
