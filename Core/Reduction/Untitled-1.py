import os
import glob
import sys
from pathlib import Path
from astropy.nddata import CCDData
from astropy.io import fits
from ccdproc import ImageFileCollection
import ccdproc as cp
from ccdproc import CCDData
from matplotlib import pyplot as plt
import numpy as np
from PyQt5 import QtCore


data_dir = (r'C:\Users\PC-CP\Desktop\tres1b')
data_dir2 = (r'C:\Users\PC-CP\Desktop\tres1b\reduced frames')
data_dir = Path(data_dir)
data_dir2 = Path(data_dir2)
files = os.listdir(data_dir)
#print(files)
#arr = [ fits.getdata(data_dir + ff) for ff in files]
# for ff in files:
#     arr = fits.getdata(data_dir/ff)
    #print(arr)

#random_bias_open = fits.open(os.path.join(data_dir,"bias-001bias.fit"))
random_bias1 = fits.getdata(os.path.join(data_dir,"bias-001bias.fit"))
random_bias2 = fits.getdata(os.path.join(data_dir,"bias-002bias.fit"))
random_bias3 = fits.getdata(os.path.join(data_dir,"bias-003bias.fit"))
random_bias4 = fits.getdata(os.path.join(data_dir,"bias-004bias.fit"))
random_bias5 = fits.getdata(os.path.join(data_dir,"bias-005bias.fit"))
random_bias6 = fits.getdata(os.path.join(data_dir,"bias-006bias.fit"))
random_bias7 = fits.getdata(os.path.join(data_dir,"bias-007bias.fit"))
random_bias8 = fits.getdata(os.path.join(data_dir,"bias-008bias.fit"))
random_bias9 = fits.getdata(os.path.join(data_dir,"bias-009bias.fit"))
random_bias10 = fits.getdata(os.path.join(data_dir,"bias-010bias.fit"))
randomdark = fits.getdata(os.path.join(data_dir,"dark-001dark.fit"))

master_bias = fits.getdata(os.path.join(data_dir2,"master_bias.fit"))
masterdark = fits.getdata(os.path.join(data_dir2,"master_dark.fit"))
#random_bias_data = random_bias_open[0].data
print(random_bias1[0, 0])
print(random_bias2[0, 0])
print(random_bias3[0, 0])
print(random_bias4[0, 0])
print(random_bias5[0, 0])
print(random_bias6[0, 0])
print(random_bias7[0, 0])
print(random_bias8[0, 0])
print(random_bias9[0, 0])
print(random_bias10[0, 0])
print("median")
#print(master_bias[0, 0])
testlist = [234,203,240,233,227,253,221,243,225,259]
median = np.median(testlist)
print(median)
print("dark")
print(randomdark[0, 0])
print("masterdark")
print(masterdark[0, 0])

print((randomdark[0,0] + 10000 - master_bias[0,0])/120)
#print(random_bias)
#np.savetxt("stackedgit.csv", arr, delimiter=",")
#random_bias_open.info()