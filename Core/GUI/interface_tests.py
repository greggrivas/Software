
import sys
import os
import glob

def find_fits_files(self, identifier):
        # FINDS FITS FILE BASED ON THE IDENTIFIER PROVIDED
        if len(identifier) > 0:
            self.fits_files = glob.glob('{0}.fits'.format(self.identifier))
            self.fits_files = list(self.fits_files)
            self.fits_files_sort()
            return self.fits_files

        else:
            return []


find_fits_files(bias)
print(fits_files)
