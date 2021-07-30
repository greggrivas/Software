import os
import glob
import sys
import astropy.io.fits as pyfits
from pathlib import Path
from astropy.nddata import CCDData
from astropy.io import fits
from ccdproc import ImageFileCollection
import ccdproc as cp
from ccdproc import CCDData
from matplotlib import pyplot as plt
import numpy as np
from PyQt5 import QtCore


class Reduction:
    
    def __init__(self,data_dir):
        self.data_dir = Path(data_dir) # αυτο πρεπει να αλλαξει και να λαμβάνεται απο κάποιο yaml file απο το ui;;
        #CHECKS IF OUTPUT DIRECTORY FOR THE REDUCED FRAMES EXISTS AND CREATES IT 
        self.outdir = os.path.join(self.data_dir, "reduced frames")
        os.makedirs(self.outdir, exist_ok=True)

        #INITIALIZING FRAMES TO BE REDUCED
        # self.files = os.listdir(data_dir)
        self.bias_frames = []
        self.dark_frames = []
        self.flat_frames = []

    def get_bias(self):
        '''
        Loads the bias frames to a flattened array
        '''
        self.bias_files = glob.glob(os.path.join(self.data_dir,"bias*.fit"))
        for ff in self.bias_files:
            self.tempbias_frames = fits.getdata(self.data_dir / ff)
            self.bias_frames.append(self.tempbias_frames.flatten())       
        self.bias_frames = np.array(self.bias_frames)
        print("bias")
        print(self.tempbias_frames.shape)
        print(self.bias_frames.shape)
        # print(self.bias_frames)  

    def get_master_bias(self):
        '''
        Combines Bias frames with MEDIAN and writes the Master Bias
        '''
        self.master_bias = np.median(self.bias_frames, axis=0)
        self.master_bias_vis = self.master_bias.reshape(1023, 1023)
        print(self.master_bias.shape)
        # print(self.master_bias)
        try:   # ΕΔΩ ΝΑ ΚΟΙΤΑΞΩ ΠΙΘΑΝΟ ERROR ΠΟΥ ΘΑ ΠΡΕΠΕΙ ΝΑ ΠΕΤΑΕΙ
            pyfits.writeto(Path(os.path.join(self.outdir,"master_bias.fit")), self.master_bias_vis)
        except:
            pass  

    def get_dark(self):
        '''
        Loads the master bias subtracted dark frames divided by exposure time
        '''
        self.dark_files = glob.glob(os.path.join(self.data_dir,"dark*.fit"))
        self.dhd = fits.getheader(self.dark_files[1])
        self.exptime = self.dhd['EXPTIME']
        for ff in self.dark_files:
            self.tempdark_frames = fits.getdata(self.data_dir / ff)
            self.dark_frames.append((self.tempdark_frames.flatten() + 1000 - self.master_bias) / self.exptime) #allazw to masterbiasvis se masterbias kai to temdarkframes me flatten
        self.dark_frames = np.array(self.dark_frames)
        print("darks")
        print(self.tempdark_frames.shape)
        print(self.dark_frames[0, 0])
        print(self.dark_frames.shape)
        # print(self.exptime)

    def get_master_dark(self):
        '''
        Combines the master bias subtracted dark frames with MEDIAN and writes the Master Dark
        '''
        self.master_dark = np.median(self.dark_frames, axis=0)
        self.master_dark_vis = self.master_dark.reshape(1023, 1023)
        try:   # ΕΔΩ ΝΑ ΚΟΙΤΑΞΩ ΠΙΘΑΝΟ ERROR ΠΟΥ ΘΑ ΠΡΕΠΕΙ ΝΑ ΠΕΤΑΕΙ
            pyfits.writeto(Path(os.path.join(self.outdir,"master_dark.fit")), self.master_dark_vis)
        except:
            pass
        print(self.master_dark_vis[0,0])

    def get_flat(self):
        '''
        Loads the callibrated flat frames
        '''
        self.flat_files = glob.glob(os.path.join(self.data_dir,"flat*.fit"))
        self.dhd2 = fits.getheader(self.flat_files[1])
        self.exptime2 = self.dhd2['EXPTIME']
        for ff in self.flat_files:
            self.tempflat_frames = fits.getdata(self.data_dir / ff)
            self.flat_frames.append((self.tempbias_frames + 1000 - self.master_bias_vis - self.exptime2) * self.master_dark_vis)
        self.flat_frames = np.array(self.flat_frames)
        # print(self.flat_frames)
        # print(self.flat_frames.shape) 

    def get_master_flat(self):
        self.master_flat = np.median(self.flat_frames, axis=0)
        self.meanvalue = np.median(self.master_flat)
        self.master_flat_norm = self.master_flat / self.meanvalue
        self.master_flat_vis = self.master_flat_norm.reshape(1023, 1023)
        print(self.master_flat)
        print(self.meanvalue)
        print("norm")
        print(self.master_flat_norm)
        print("vis")
        print(self.master_flat_vis)
        try:   # ΕΔΩ ΝΑ ΚΟΙΤΑΞΩ ΠΙΘΑΝΟ ERROR ΠΟΥ ΘΑ ΠΡΕΠΕΙ ΝΑ ΠΕΤΑΕΙ
            pyfits.writeto(Path(os.path.join(self.outdir,"master_flat.fit")), self.master_flat_vis)
        except:
            pass

data_dir = (r'C:\Users\PC-CP\Desktop\tres1b')
data_dir2 = (r'C:\Users\PC-CP\Desktop\tres1b\reduced frames')
test = Reduction(data_dir)
test2 = test.get_bias()
test3 = test.get_master_bias()
test4 = test.get_dark()
test5 = test.get_master_dark()
# test6 = test.get_flat()
# test7 = test.get_master_flat()

# random_bias = fits.getdata(os.path.join(data_dir,"bias-001bias.fit"))
# master_bias = fits.getdata(os.path.join(data_dir2, "master_bias.fit"))
# y = np.array(random_bias.flatten())
# x = np.array(master_bias.flatten())

#istogramma mias foto
# plt.figure(1)
# histo1 = plt.hist(y,150)
# plt.title("bias001")

#istogramma master bias
# plt.figure(2)
# histo2 = plt.hist(x,150)
# plt.title("master bias")
# plt.show()