from PIL import Image
import numpy as np



try:
    image = Image.open("picturetest.png")
    #some images might be in cmyk format
    image = image.convert('RGB')
    px = image.load()
    changed = []
    for y in range(image.size[1]):
        row = []
        for x in range(image.size[0]):
            row.append(tuple([px[x,y][0]+1,px[x,y][1],px[x,y][2]]))
        changed.append(row)
    
    changed_array = np.array(changed,dtype=np.uint8)
    changed_image = Image.fromarray(changed_array)
    changed_image.save("changed_image.png")
except IOError:
    print("Error")