import os

from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path
# from PIL import Image
from ccdproc import ImageFileCollection
import ccdproc as ccdp 

from pathlib import Path
from photutils.aperture import EllipticalAperture
from astropy.nddata import CCDData
from astropy.io import fits
from astropy.stats import mad_std


# data_dir = (r'C:\Users\PC-CP\Desktop\tres1b')
# image_name = 'tres1-b-001.fit'
# image_path = Path(data_dir) / image_name

caldata_bias = Path(r'C:\Users\PC-CP\Desktop\tres1b', 'reduced_bias')
caldata_bias.mkdir(exist_ok=True)
# calibrated_path = Path('reduced_bias')
# reduced_images = ccdp.ImageFileCollection(calibrated_path)

def test(directory_path):
    print(directory_path)
