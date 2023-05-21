from PIL import Image
import numpy as np

def change_image(theatre_name,original,red_change_degree=0,green_change_degree=0,blue_change_degree=0):
    i = Image.open(original)
    i = i.convert("RGB")
    img_data = i.load()
    changed_img_data = []
    for y in range(i.size[1]):
        row_data = []
        for x in range(i.size[0]):
            row_data.append((tuple([img_data[x,y][0]+red_change_degree,img_data[x,y][1]+green_change_degree,img_data[x,y][2]+blue_change_degree])))
        changed_img_data.append(row_data)

    changed_img_data_array = np.array(changed_img_data,dtype=np.uint8)
    changed_img = Image.fromarray(changed_img_data_array)
    changed_img.save("R%03dG%03dB%03d.png"%(red_change_degree,green_change_degree,blue_change_degree))

    f = open("theatre_data.txt","a+")
    f.write("%s - R%03dG%03dB%03d\n"%(theatre_name,red_change_degree,green_change_degree,blue_change_degree))


change_image("Theatre1","test.png",1,1,0)
#change_image("Theatre2","test.png",1,0,1)
