from PIL import Image
# import an existing image
si = Image.open("OLP2.JPG")
# get it's w and h
w,h = si.size
# make a new image, in RGB mode, with the size of the imported images, with all pixels set to black
im_b = Image.new("RGB", (w,h), color=(0,0,0))
# loop over the w value of the new image, every second pixel
for x in range(0,im_b.size[0],2):
    #  loop over the h of the new image, every second pixel
    for y in range(0,im_b.size[1],2):
        # get the rgb value of each pixel in the imported image
        p = si.getpixel((x,y))
        # assign rgb value to the itterations of x and y
        im_b.putpixel((x,y), p)
        # print "put inner loop", x, y
im_b.save("whatever.png")
print "saved that image"
