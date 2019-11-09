from time import sleep
from picamera import PiCamera

#for naming the photos
picounter = 0

#sets the resolution to capture and starts the camera preview
def startup():
    camera.resolution = (224, 224)
    camera.start_preview()
    
#takes a photo and saves it as picounter
def capture():
    camera.capture("%d" % picounter)
    piccounter++

    
#main loop
def main(numpics):
    for x in range(numpics):
        capture()
        sleep(0.5)



camera = PiCamera()
startup()
main(10)
camera.stop_preview()


