from SimpleCV import Image

img = Image('ex17.png')

# Rotate the image counter-clockwise 45 degrees
rot = img.rotate(45)
rot.show()
