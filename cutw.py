
# import matplotlib.image as mpimg
def cal(folder):
    import scipy.io
    import numpy
    import numpy as np
    # coding=utf-8

    import os
    from PIL import Image
    #folder="V2007-761_AS"
    try:
        os.mkdir(folder+"/w")
        os.mkdir(folder+"/r")
        os.mkdir(folder+"/c")
    except:
        pass
    lena = Image.open(folder+"/a.png") #20000*15000, the size is correct. So i ONLY NEED TO FIND THE POSITION OF T CELLS
    # # #
    # # #
    # # # #
    lena2 = np.array(lena.convert("RGB"))
    a,b,c=lena2.shape #横着的是a,b 竖着的是b，a
    print("a,b,",a,b) #20000:12000
    resized=lena2
    # #
    # #
    # #
    # for k in range(int(len(data['centroids_all']))):
    #     #print(k)
    #     if data['centroids_all'][k][1]>=10 and data['centroids_all'][k][0]>=10 and data['centroids_all'][k][1]<a-10 and data['centroids_all'][k][0]<b-10:
    #
    #
    #
    #         x,y=int(data['centroids_all'][k][1]),int(data['centroids_all'][k][0])
    #         lena2[x-10:x+11,y-10:y+11,0]=255
    #         lena2[x - 10:x + 11, y - 10:y + 11, 1] = 0
    #         lena2[x - 10:x + 11, y - 10:y + 11, 2] = 0
    #
    #     else:
    #         print("i am not here")
    # #
    # # # firstpart= lena2[0:int(a/2)]
    # # # secondpart= lena2[int(a/2):]
    # # #scipy.misc.imsave("p23s.jpg", firstpart)
    # # #scipy.misc.imsave("p27bs.jpg", secondpart)
    # #
    # scipy.misc.imsave("p13s.jpg", lena2)
    # print(lena2.shape)
    # print(lena2.size)
    from PIL import Image
    #
    #
    #

    # img = Image.open("p13s.jpg")
    #
    height=a
    width=b

    #img=Image.fromarray(lena2)
    #img=lena2.convert("RGB")
    #resized = lena.resize((width,height))
    #scipy.misc.imsave("resized2006w.jpg", resized)
    print("done")
     #20000*15000, the size is correct. So i ONLY NEED TO FIND THE POSITION OF T CELLS
    #
    #
    #
    #resized= np.array(resized.convert("RGB"))
    #print(type(resized))
    #print(resized.shape)
    count = 0
    for i in range(int(height/64)-2):
        for j in range(int(width/64)-2):

            current = resized[64*i:64+64*i,64*j:64+64*j]

            print(i)
            name = folder+"/w/"+str(count)+".png"


            # count_t_cell = 0
            # count_ai_cell = 0
            # for ii in range(64):
            #     for jj in range(64):
            #         if current[ii][jj][0]>150:
            #             current[ii][jj][1]=255
            #             current[ii][jj][2]=0
                    # if int(current[ii][jj][0])>150 and int(current[ii][jj][1])>150 and int(current[ii][jj][2])>150:
                    #     count_ai_cell+=1
            #         if int(current[ii][jj][0])-int(current[ii][jj][1])>150:
            #             count_t_cell+=1
            # if count_ai_cell>=900 and count_t_cell>0:
            scipy.misc.imsave(name, current)
            count+=1

