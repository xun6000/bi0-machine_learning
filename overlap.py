import scipy.io
import numpy
import numpy as np
#coding=utf-8

#baab 这是竖着的图
# dataFile = '/Users/gy12/Desktop/notebooks/bioml/training_set/poor/new/P13_p.mat'
# data = scipy.io.loadmat(dataFile)
# #print(len(data['final_tumor']))
#
# #data['final_tumor']
# #a= [[[0,0,0] for i in range(20000)] for j in range(15000)]
# #a=numpy.zeros((15000,20000,3))
# scipy.misc.imsave("p13.jpg", data['final_tumor']*255)
from PIL import Image
import os
# import matplotlib.image as mpimg
folder="V2001-086_S2001-01616_4"
#folder="xinde/V2002-348_S2002-27132_13"
lena1 = Image.open(folder+"/a.png") #20000*15000, the size is correct. So i ONLY NEED TO FIND THE POSITION OF T CELLS
# # #
# # #
# # # #
lena2 = Image.open(folder+"/b.png")
  # 20000*15000, the size is correct. So i ONLY NEED TO FIND THE POSITION OF T CELLS
# # #
# # #
# # # #

lena1 = np.array(lena1.convert("RGB"))
lena2 = np.array(lena2.convert("RGB"))
a= len(lena1)
b= len(lena1[0])
print(lena2.shape)
name=folder+"overlap.jpg"
for i in range(a):
    for j in range(b):
        #mav = max(lena1[i][j],mav)
        if lena2[i][j][0] >15 and lena1[i][j][0]>150 :
            print("fefe")
            lena1[i][j][2]=255
            lena1[i][j][0] = 0
            lena1[i][j][1] = 0
        elif lena2[i][j][0] >15:
            lena1[i][j][0] = 255

print(lena1)
scipy.misc.imsave(name, lena1)


