import scipy.io
import numpy
import numpy as np
#coding=utf-8
import shutil
import os
from PIL import Image
# import matplotlib.image as mpimg
folder="V2002-267_21"

#os.mkdir(folder+"/c")

c=os.listdir("D:\dinalbio")
#new = "D:\finalbio"
for i in range(len(c)):
    pos="D:\dinalbio\\"+c[i]
    e=os.listdir(pos)
    for eveyr in e:
        if str(eveyr) != "c":
            if str(eveyr)[-1]=="g":

                os.remove(pos+"\\"+eveyr)
            else:
                shutil.rmtree(pos + "\\" + eveyr, ignore_errors=True)
                #os.rmdir(pos + "\\" + eveyr)
