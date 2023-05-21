from PIL import Image
import numpy as np



try:
    image = Image.open("picturetest.png")
    #some images might be in cmyk format
    image = image.convert('RGB')
    px = image.load()
    red_only = []
    green_only = []
    blue_only = []
    for y in range(image.size[1]):
        r = []
        g = []
        b = []
        for x in range(image.size[0]):
            #change in variation detected by human eye should be pin pointed
            r.append(tuple([px[x,y][0],0,0]))
            g.append(tuple([0,px[x,y][1],0]))
            b.append(tuple([0,0,px[x,y][2]]))
        red_only.append(r)
        green_only.append(g)
        blue_only.append(b)
    
    red = np.array(red_only,dtype=np.uint8)
    green = np.array(green_only,dtype=np.uint8)
    blue = np.array(blue_only,dtype=np.uint8)
    red_image = Image.fromarray(red)
    blue_image = Image.fromarray(blue)
    green_image = Image.fromarray(green)
    red_image.save("red_image.png")
    blue_image.save("blue_image.png")
    green_image.save("green_image.png")

except IOError:
    print("loda")