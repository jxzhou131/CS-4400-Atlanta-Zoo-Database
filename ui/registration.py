# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
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
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(220, 130, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(190, 180, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(190, 230, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_confirmpassword = QtWidgets.QLabel(self.centralwidget)
        self.label_confirmpassword.setGeometry(QtCore.QRect(140, 280, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_confirmpassword.setFont(font)
        self.label_confirmpassword.setObjectName("label_confirmpassword")
        self.Heading_register = QtWidgets.QLabel(self.centralwidget)
        self.Heading_register.setGeometry(QtCore.QRect(260, 30, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_register.setFont(font)
        self.Heading_register.setObjectName("Heading_register")
        self.Homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Homebutton.setGeometry(QtCore.QRect(10, 10, 113, 32))
        self.Homebutton.setObjectName("Homebutton")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(290, 130, 113, 21))
        self.lineEdit_email.setText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(290, 180, 113, 21))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(290, 230, 113, 21))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 280, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
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
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.label_username.setText(_translate("MainWindow", "Username:"))
        self.label_password.setText(_translate("MainWindow", "Password:"))
        self.label_confirmpassword.setText(_translate("MainWindow", "Confirm password:"))
        self.Heading_register.setText(_translate("MainWindow", "Registration"))
        self.Homebutton.setText(_translate("MainWindow", "HOME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

