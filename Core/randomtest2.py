import sys
import os
from pathlib import Path
from astropy.nddata import CCDData
from astropy.io import fits
from ccdproc import ImageFileCollection
import ccdproc as cp
from ccdproc import CCDData
import matplotlib.pyplot as plt
import numpy as np


data_dir = (r'C:\Users\PC-CP\Desktop\tres1b')
comb_path = (r'C:\Users\PC-CP\Desktop\tres1b\reduced_bias')
comb_path_final = os.path.join(comb_path, 'master_bias.fit')
#im_collection = ImageFileCollection(data_dir)

biasimages = []

#for filename in im_collection.files_filtered(imagetyp='Bias Frame'):
ccd = CCDData.read(r'C:\Users\PC-CP\Desktop\tres1b\bias-001bias.fit', unit='adu')
biasimages.append(ccd)
print(biasimages)

master_bias = cp.combine(biasimages, method='median')
master_bias_file = open(comb_path_final, "w")
master_bias_file.write('master_bias.fit')
master_bias_file.close()