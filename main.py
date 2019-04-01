import os,threading
import cv2


# path = os.getcwd()

# movies = os.listdir(path+"/movie");

# 遍历视频  把move目录下的MP4 全部转成图片


# for movie in movies:
#     print(movie)
#
#     vc=cv2.VideoCapture(path+"/movie/"+movie)
#     movieName =movie.split('.')[0]
#
#     print(movieName)
#
#     # 新建文件夹
#     if(os.path.exists(path+"/image2/"+movieName)):
#         print()
#     else:
#         os.makedirs(path+"/image2/"+movieName)
#
#     c=1
#     if vc.isOpened():
#         rval,frame=vc.read()
#     else:
#         rval=False
#     i=1
#     while rval:
#         rval,frame=vc.read()
#         # rows, cols, channel = frame.shape
#         # frame2=cv2.resize(frame,(cols/3,rows/3),fx=0,fy=0,interpolation=cv2.INTER_AREA)
#
#
#         if ( c%5 == 0 or c%5-2==0):                            # 25fps
#
#             cv2.imwrite((path + '/image2/' + movieName + '/' + str(i) + '.jpg'), frame)
#             i=i+1
#
#         #     cv2.imwrite((path+'/image/'+str(c)+'.jpg'),frame)
#             # cropped001 = frame2[0:300,300:600]   #y change from 0 to 300 x change from 300 to 600
#             # cv2.imwrite('./cropped/'+str(c)+'_001.jpg',cropped001)
#         c=c+1
#         cv2.waitKey(1)
#     vc.release()






class MovieToImage(threading.Thread):
    def __init__(self,fileName):
        super(MovieToImage,self).__init__()

        self.fileName = fileName

    def run(self):
        vc=cv2.VideoCapture(path+"/movie/"+self.fileName)
        movieName =self.fileName.split('.')[0]

        print(movieName)

        # 新建文件夹
        if(os.path.exists(path+"/image2/"+movieName)):
            print()
        else:
            os.makedirs(path+"/image2/"+movieName)

        c=1
        if vc.isOpened():
            rval,frame=vc.read()
        else:
            rval=False
        i=1
        while rval:
            rval,frame=vc.read()
            # rows, cols, channel = frame.shape
            # frame2=cv2.resize(frame,(cols/3,rows/3),fx=0,fy=0,interpolation=cv2.INTER_AREA)


            if ( c%5 == 0 or c%5-2==0):                            # 25fps

                cv2.imwrite((path + '/image2/' + movieName + '/' + str(i) + '.jpg'), frame)
                i=i+1

            #     cv2.imwrite((path+'/image/'+str(c)+'.jpg'),frame)
                # cropped001 = frame2[0:300,300:600]   #y change from 0 to 300 x change from 300 to 600
                # cv2.imwrite('./cropped/'+str(c)+'_001.jpg',cropped001)
            c=c+1
            cv2.waitKey(1)
        vc.release()


if __name__ == '__main__':

    path = os.getcwd()

    movies = os.listdir(path + "/movie");

    t = []

    for movie in movies:
        print(movie)

        movieName = movie
        t.append(MovieToImage(movieName))
    for i in range(len(movies)):
        t[i].start()

    for i in range(len(movies)):
        t[i].join()