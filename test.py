from PIL import Image
import numpy as np


try:
    image = Image.open("test.png")
    px = image.load()
    l = []
    for y in range(image.size[1]):
        k = []
        for x in range(image.size[0]):
            k.append(tuple([i+1 for i in px[x,y]]))
        l.append(k)
    
    lnp = np.array(l,dtype=np.uint8)
    imag1 = Image.fromarray(lnp)
    imag1.save("test1.png")
except IOError:
    print("loda")