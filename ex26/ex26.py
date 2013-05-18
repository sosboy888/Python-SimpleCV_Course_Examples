from SimpleCV import *

display = Display()
cam = Camera() # initialize the camera

haarcascade = HaarCascade("face")# a simple configuration for face detection features

while display.isDone() == False:
    img = cam.getImage().flipHorizontal().scale(0.5)# get image, flip it so it looks mirrored, scale to speed things up
    faces = img.findHaarFeatures(haarcascade) # load in trained face file
    if faces:
        face = faces[-1]
	face.draw(Color.RED, 1)
    img.show() # display the image
