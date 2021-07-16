import sys
import os
from pathlib import Path
from astropy.nddata import CCDData
from astropy.io import fits
from ccdproc import ImageFileCollection
import ccdproc as cp
from ccdproc import CCDData
from matplotlib import pyplot as plt
import numpy as np
from PyQt5 import QtCore
from astropy.stats import mad_std


class Reduction:
    
    def __init__(self,data_dir):
        self.data_dir = Path(data_dir)
        os.makedirs(os.path.join(self.data_dir,'reduced_frames'))
        im_collection = cp.ImageFileCollection(self.data_dir) # Loads all the images 
        #print(repr(im_collection.summary)) #KANEI PRINT TA PERIEXOMENA TOY DIRECTORY
        self.biaslist = im_collection.files_filtered(imagetyp='Bias Frame',  include_path=True) # Filters the Bias frames
        self.darklist = im_collection.files_filtered(imagetyp='Dark Frame',  include_path=True) # Filters the Dark frames
        self.flatlist = im_collection.files_filtered(imagetyp='Flat Field',  include_path=True) # Filters the Flat frames
        # print(self.flatlist)
   

    def get_master_bias(self):
       # Master Bias routine
        self.combined_bias = cp.combine(self.biaslist, method='average', unit='adu')#,sigma_clip=True, sigma_clip_low_thresh=5, sigma_clip_high_thresh=5,
                             #sigma_clip_func=np.ma.median, signma_clip_dev_func=mad_std, mem_limit=350e6)                          # Combines them using the combine function
        self.combined_bias.meta['combined'] = True                                                           # Adds the keyword COMBINED to the header
        self.combined_bias.write(Path(os.path.join(self.data_dir,'reduced_frames')) / "master_bias.fit")     # Writes the master bias
          
    def get_master_dark(self):
       # Master Dark routine
        combined_dark = cp.combine(self.darklist, method='average', unit='adu')                       # Combines them using the combine function
        combined_dark.meta['combined'] = True                                                        # Adds the keyword COMBINED to the header
        combined_dark.write(Path(os.path.join(self.data_dir,'reduced_frames')) / "master_dark.fit")  # Writes the master dark

    def inv_median(self, a):
        return 1 / np.median(a)

    def get_master_flat(self):
       # Master Flat routine
        combined_flat = cp.combine(self.flatlist, method='average',scale=self.inv_median, unit='adu')                          # Combines them using the combine function
        combined_flat.meta['combined'] = True                                                           # Adds the keyword COMBINED to the header
        combined_flat.write(Path(os.path.join(self.data_dir,'reduced_frames')) / "master_flat.fit")     # Writes the master flat

# Master Bias and random bias PLOTS for comparison
data_dir = (r'C:\Users\PC-CP\Desktop\tres1b')
test = Reduction(data_dir)
test.get_master_flat()
flat = fits.getdata(r'C:\Users\PC-CP\Desktop\tres1b\reduced_frames\master_flat.fit', ext=0) 
# biasm = fits.getdata(r'C:\Users\PC-CP\Desktop\tres1b\reduced_frames\master_bias.fit', ext=0) 
# bias2 = fits.getdata(r'C:\Users\PC-CP\Desktop\tres1b\bias-001bias.fit', ext=0)
# plt.figure("masterbias")
# plt.imshow(biasm, cmap='gray')
# plt.figure("random bias")
# plt.imshow(bias2, cmap='gray')
# plt.show()

# PLOT MASTER FLAT
plt.figure("masterflat")
plt.imshow(flat, cmap="gray")
plt.show()

# READING A SINGLE IMAGE
# image_name = 'flat-001flat.fit'
# image_path = Path(data_dir) / image_name
# ccdflat = CCDData.read(image_path, unit = 'adu')
# print(ccdflat.header)

