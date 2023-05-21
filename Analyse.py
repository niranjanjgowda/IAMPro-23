from PIL import Image

def analyse(original_path,test_image_path):
    original = Image.open(original_path)
    test_image = Image.open(test_image_path)
    ori_data = original.load()
    test_image_data = test_image.load()

    red_degree_change,green_degree_change,blue_degree_change = [j-i for i,j in zip(ori_data[0,0],test_image_data[0,0])]

    key = "R%03dG%03dB%03d"%(red_degree_change,green_degree_change,blue_degree_change)

    f = open("theatre_data.txt")
    theatre_name = ""
    data = f.readlines()
    for i in data:
        print(i)
        if(key in i):
            theatre_name = i.split(" -")[0]
            break

    return key,theatre_name
    

print(analyse("test.png","R001G000B001.png"))