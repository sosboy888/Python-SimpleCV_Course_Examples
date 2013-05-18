from SimpleCV import Image
from SimpleCV.Shell import plot

img = Image('ex21a.jpg') # Open ex21b.jpg and ex21c.jpg too :)

# Generate the histogram with 256 bins, one for each color
histogram = img.histogram(256)
# Show how many elements are in the list
len(histogram)
# Graphically display the histogram
plot(histogram)
