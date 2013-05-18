from SimpleCV import Image, Color

bluePincels = Image("ex19.jpg") # Open mm.png too :)

# Get a random value for color in a pixel 100,100 of the image
pixel = bluePincels.getPixel(100,100)
print pixel 

# Distantiate the color of pixel picked previously
colorDist = bluePincels.colorDistance(pixel)

# Binarize the image and invert the colors to show most of the blue parts of the image
colorDistBin = colorDist.binarize(50).invert()
colorDistBin.show()
