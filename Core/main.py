import sys
import numpy as np
import mainscreen
from Reduction import test #DOKIMASTIKO EINAI GIA DIAGRAFH

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from astropy.io import fits as pf

directory_path = ""


class main(QtWidgets.QMainWindow):
    def __init__(self):
        super(main,self).__init__()
        loadUi("mainscreen.ui",self)       
        self.biasdir.clicked.connect(self.get_directory)
        #self.runreduct.clicked.connect()

    def get_directory(self):
        #fname=QFileDialog.getOpenFileName(self, 'Open file')    
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.biasdir.setText('{}'.format(file))
        directory_path = file
        test(directory_path)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainwindow = main()
    mainwindow.show()
    sys.exit(app.exec())