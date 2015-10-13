from PIL import Image
si = Image.open("OLP2.JPG")
print si.size
# w = si.size[0]
# h = si.size[1]
# whoa, we could do this in one go :
w,h = si.size

for x in range(w):
    for y in range(h):
        print x, y
        print si.getpixel((x,y))
        """
        prints a list of pixel coordinates, then their RGB value, like so:
        499 369
        (212, 205, 238)
        499 370
        (212, 202, 236)
        499 371
        (213, 202, 236)
        499 372
        (214, 203, 237)
        499 373
        (213, 202, 236)
        499 374
        (212, 201, 235)
        """
