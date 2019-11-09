from time import sleep
from picamera import PiCamera

camear = PiCamear()
camera.resolution = (224, 224)
camera.start_preview()

sleep(2)
camera.capture('hitony.jpg')
camera.stop_preview()
