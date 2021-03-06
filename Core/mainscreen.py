# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 720)
        MainWindow.setMinimumSize(QtCore.QSize(720, 720))
        MainWindow.setMaximumSize(QtCore.QSize(720, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.runphoto = QtWidgets.QPushButton(self.centralwidget)
        self.runphoto.setGeometry(QtCore.QRect(290, 440, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.runphoto.setFont(font)
        self.runphoto.setObjectName("runphoto")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 701, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.flatdir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.flatdir.setObjectName("flatdir")
        self.gridLayout.addWidget(self.flatdir, 2, 1, 1, 1)
        self.darkdir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.darkdir.setObjectName("darkdir")
        self.gridLayout.addWidget(self.darkdir, 1, 1, 1, 1)
        self.biasdir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.biasdir.setObjectName("biasdir")
        self.gridLayout.addWidget(self.biasdir, 0, 1, 1, 1)
        self.darklabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(False)
        self.darklabel.setFont(font)
        self.darklabel.setFrameShape(QtWidgets.QFrame.Box)
        self.darklabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.darklabel.setLineWidth(2)
        self.darklabel.setIndent(0)
        self.darklabel.setObjectName("darklabel")
        self.gridLayout.addWidget(self.darklabel, 1, 0, 1, 1)
        self.biaslabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(False)
        self.biaslabel.setFont(font)
        self.biaslabel.setFrameShape(QtWidgets.QFrame.Box)
        self.biaslabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.biaslabel.setLineWidth(2)
        self.biaslabel.setIndent(0)
        self.biaslabel.setObjectName("biaslabel")
        self.gridLayout.addWidget(self.biaslabel, 0, 0, 1, 1)
        self.flatlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(False)
        self.flatlabel.setFont(font)
        self.flatlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.flatlabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.flatlabel.setLineWidth(2)
        self.flatlabel.setIndent(0)
        self.flatlabel.setObjectName("flatlabel")
        self.gridLayout.addWidget(self.flatlabel, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.runphoto.setText(_translate("MainWindow", "Run Photometry"))
        self.flatdir.setText(_translate("MainWindow", "Select Directory"))
        self.darkdir.setText(_translate("MainWindow", "Select Directory"))
        self.biasdir.setText(_translate("MainWindow", "Select Directory"))
        self.darklabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Dark Frames</span></p></body></html>"))
        self.biaslabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Bias Frames</span></p></body></html>"))
        self.flatlabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Flat Frames</span></p></body></html>"))
