import sys
import os
import glob
import logging
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets, uic

#from Core.GUI.interface_tests import find_fits_files

class UISoftware(QtWidgets.QApplication):

    def __init__(self, parent=None):
        super(UISoftware, self).__init__(parent)
        self.logger = logging.getLogger(__name__) # Create the logger for the file

        # Create the main GUI window and the other windows
        self.main_window = QtWidgets.QMainWindow()
        self.ui_red_settings_window = QtWidgets.QMainWindow(parent=self.main_window)  # Create reduction target and settings window
        self.ui_man_target_window = QtWidgets.QMainWindow(parent=self.main_window) # Create reduction manual target window
        
        #Loading the ui files
        try:
            self.main_widget = uic.loadUi(r'C:\Users\PC-CP\Documents\Projects\Software\ui_files\main_menu.ui', self.main_window)
            self.red_set_win = uic.loadUi(r'C:\Users\PC-CP\Documents\Projects\Software\ui_files\reduction_settings_target.ui', self.ui_red_settings_window)
            self.manual_target_win = uic.loadUi(r'C:\Users\PC-CP\Documents\Projects\Software\ui_files\target_manually.ui', self.ui_man_target_window)
        except FileNotFoundError:
            self.logger.exception("Something happened when loading GUI files. See traceback")
            sys.exit(-1)  # Indicate a problematic shutdown
        self.setup_ui()  # Call the function to make all the connections for the GUI 

    def setup_ui(self):
        # MAIN MENU GUI WINDOWS
        self.main_widget.settings_target_btn.clicked.connect(self.red_set_win.show)

        # TARGET AND SETTINGS WINDOW
        self.red_set_win.target_manually_btn.clicked.connect(self.manual_target_win.show)
        self.red_set_win.open_dir_tool.clicked.connect(lambda: self.get_directory_dialog())
        #self.red_set_win.Nbias_found.setText(self.update_fits_files('test'))


    def get_directory_dialog(self):
        # METHOD TO GET DIRECTORY PATH
        self.directory_path = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.red_set_win.directory_path_qline.setText(self.directory_path)
    
    def find_fits_files(self, identifier):
        # FINDS FITS FILES BASED ON THE IDENTIFIER PROVIDED
        if len(self.identifier) > 0:
            self.fits_files = glob.glob('{0}.fits'.format(self.identifier))
            self.fits_files = list(self.fits_files)
            self.fits_files_length = len(self.fits_files)
            return self.fits_files_length



    def main():
        app = UISoftware(sys.argv)
        app.main_widget.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    UISoftware.main()
