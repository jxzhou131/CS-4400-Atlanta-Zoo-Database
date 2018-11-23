# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorFunctionality.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#################### MUST HAVE #################################################################
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import sys
app = QtWidgets.QApplication(sys.argv)
################################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(286, 76, 202, 44))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.button_ser_exb = QtWidgets.QPushButton(self.centralwidget)
        self.button_ser_exb.setGeometry(QtCore.QRect(104, 165, 248, 41))
        self.button_ser_exb.setMinimumSize(QtCore.QSize(248, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_ser_exb.setFont(font)
        self.button_ser_exb.setObjectName("button_ser_exb")
        self.button_ser_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_ser_show.setGeometry(QtCore.QRect(108, 259, 244, 39))
        self.button_ser_show.setMinimumSize(QtCore.QSize(244, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_ser_show.setFont(font)
        self.button_ser_show.setObjectName("button_ser_show")
        self.button_ser_anm = QtWidgets.QPushButton(self.centralwidget)
        self.button_ser_anm.setGeometry(QtCore.QRect(111, 359, 243, 45))
        self.button_ser_anm.setMinimumSize(QtCore.QSize(243, 45))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_ser_anm.setFont(font)
        self.button_ser_anm.setObjectName("button_ser_anm")
        self.button_view_exb_his = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_exb_his.setGeometry(QtCore.QRect(390, 164, 248, 41))
        self.button_view_exb_his.setMinimumSize(QtCore.QSize(248, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_view_exb_his.setFont(font)
        self.button_view_exb_his.setObjectName("button_view_exb_his")
        self.button_view_show_his = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_show_his.setGeometry(QtCore.QRect(392, 260, 246, 39))
        self.button_view_show_his.setMinimumSize(QtCore.QSize(246, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_view_show_his.setFont(font)
        self.button_view_show_his.setObjectName("button_view_show_his")
        self.button_lgo = QtWidgets.QPushButton(self.centralwidget)
        self.button_lgo.setGeometry(QtCore.QRect(395, 360, 243, 44))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_lgo.setFont(font)
        self.button_lgo.setObjectName("button_lgo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.userDefinedInitialization()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_header.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.button_ser_exb.setText(_translate("MainWindow", "Search Exhibits"))
        self.button_ser_show.setText(_translate("MainWindow", "Search Show"))
        self.button_ser_anm.setText(_translate("MainWindow", "Search for Animals"))
        self.button_view_exb_his.setText(_translate("MainWindow", "View Exhibit History"))
        self.button_view_show_his.setText(_translate("MainWindow", "View Show History"))
        self.button_lgo.setText(_translate("MainWindow", "Logout"))



    def userDefinedInitialization(self):
        self.button_lgo.clicked.connect(self.logout)
        self.button_ser_anm.clicked.connect(self.searchAnimals)
        self.button_ser_show.clicked.connect(self.searchShow)
        self.button_ser_exb.clicked.connect(self.searchExhibit)
        self.button_view_show_his.clicked.connect(self.showHistory)
        self.button_view_exb_his.clicked.connect(self.exhibitHistory)

    def searchExhibit(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorSearchExhibit']
        app.exit()

    def searchShow(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorSearchShow']
        app.exit()

    def searchAnimals(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorSearchAnimals']
        app.exit()

    def showHistory(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorShowHistory']
        app.exit()

    def exhibitHistory(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorExhibitHistory']
        app.exit()

    def logout(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['logout']
        app.exit()

def render():
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    # close the windows
    MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

