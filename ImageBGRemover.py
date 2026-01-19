# This code is similar to PriorityQueue kind of thing except it has a package pip installer

from rembg import remove
from PIL import Image
dogs = 'ImageToTransform\Back.jpg'
outputss = 'PlacesOfResults\output(Back).png'

input = Image.open(dogs)
output = remove(input)
output.save(outputss)

print("Done? idk")