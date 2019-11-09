from PIL import Image
        
flash = Image.open('flash.gif')
noFlash = Image.open('noFlash.jpg')

# 0 flash       to stop
# 1 no flash    to go
def chooseIm(num):
    if (num == 0):
        flash.show()
    elif (num == 1):
        noFlash.show()

chooseIm(1)
