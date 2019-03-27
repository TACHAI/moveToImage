import cv2,os
import numpy as np

path = os.getcwd()

movies = os.listdir(path+"/image2");

for movie in movies:
    print(movie)

    movieName = movie

    print(movieName)

    # 新建文件夹
    if (os.path.exists(path + "/small/" + movieName)):
        print()
    else:
        os.makedirs(path + "/small/" + movieName)

    images = os.listdir(path + "/image2/"+movieName)

    for image in images:
        print(image)
        img = cv2.imread(path+"/image2/"+movieName+"/"+image)
        # cv2.imshow('img',img)
        # num =np.zeros(img.shape,img.dtype)-150
        # imgIncrease = cv2.add(img,num)
        # imgSubtract = cv2.subtract(img, num)
        try:
            if img.any == None:
                print ("Error: could not load image")
                os._exit(0)

            height,width = img.shape[:2]

            # 缩小图像
            siez = (int(width/2),int(height/2))
            shrink = cv2.resize(img,siez,interpolation=cv2.INTER_AREA)

            cv2.imwrite((path + "/small/" + movieName+"/"+ image ), shrink)
        except:
            print("Error++")

