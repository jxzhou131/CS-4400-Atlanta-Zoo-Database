# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorFunctionality.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(350, 70, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.button_ser_exb = QtWidgets.QPushButton(self.centralwidget)
        self.button_ser_exb.setGeometry(QtCore.QRect(130, 170, 121, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.button_ser_exb.setFont(font)
        self.button_ser_exb.setObjectName("button_ser_exb")
        self.button_ser_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_ser_show.setGeometry(QtCore.QRect(130, 260, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.button_ser_show.setFont(font)
        self.button_ser_show.setObjectName("button_ser_show")
        self.button_ser_anm = QtWidgets.QPushButton(self.centralwidget)
        self.button_ser_anm.setGeometry(QtCore.QRect(130, 360, 141, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.button_ser_anm.setFont(font)
        self.button_ser_anm.setObjectName("button_ser_anm")
        self.button_view_exb_his = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_exb_his.setGeometry(QtCore.QRect(410, 170, 141, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.button_view_exb_his.setFont(font)
        self.button_view_exb_his.setObjectName("button_view_exb_his")
        self.button_view_show_his = QtWidgets.QPushButton(self.centralwidget)
        self.button_view_show_his.setGeometry(QtCore.QRect(410, 260, 141, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.button_view_show_his.setFont(font)
        self.button_view_show_his.setObjectName("button_view_show_his")
        self.button_lgo = QtWidgets.QPushButton(self.centralwidget)
        self.button_lgo.setGeometry(QtCore.QRect(410, 360, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.button_lgo.setFont(font)
        self.button_lgo.setObjectName("button_lgo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label_header.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.button_ser_exb.setText(_translate("MainWindow", "Search Exhibits"))
        self.button_ser_show.setText(_translate("MainWindow", "Search Show"))
        self.button_ser_anm.setText(_translate("MainWindow", "Search for Animals"))
        self.button_view_exb_his.setText(_translate("MainWindow", "View exhibt history"))
        self.button_view_show_his.setText(_translate("MainWindow", "View show history"))
        self.button_lgo.setText(_translate("MainWindow", "Log out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

