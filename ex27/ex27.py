from SimpleCV import *

display = Display()
cam = Camera()
threshold = 5.0 # if mean exceeds this amount do something, the max level of difference 

while display.isDone() == False:
	previous = cam.getImage() # grab a frame
	time.sleep(0.5) # wait for half a second
	current = cam.getImage() # grab another frame
	diff = current - previous
	matrix = diff.getNumpy()
	mean = matrix.mean()

	diff.show()

	if mean >= threshold:
		print "Motion Detected"
