from PIL import Image
# create an empty (black) image
im_b = Image.new("RGB", (640, 480), color=(0,0,255))
# print "created a black image"
for x in range(0,im_b.size[0],4):
    for y in range(0,im_b.size[1],4):
        im_b.putpixel((x,y), (255,255,255))
        # print "put inner loop", x, y
im_b.save("black-grid.png")
# print "saved that image"
