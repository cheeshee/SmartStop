from time import sleep
from picamera import PiCamera
import subprocess

#for naming the photos
picounter = 0

#sets the resolution to capture and starts the camera preview
def startup():
    camera.resolution = (224, 224)
    camera.start_preview()
    
#takes a photo and saves it as picounter
def capture1():
    global picounter
    camera.capture("picture" + str(picounter)+".jpg")
    picounter = picounter + 1

    #main loop
def main(numpics):
    for x in range(numpics):
        capture1()
        sleep(0.5)



camera = PiCamera()
startup()
main(10)
camera.stop_preview()
subprocess.call(['transferfilestopi.sh'])

