# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(800, 532)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(340, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.registrationButton = QtWidgets.QPushButton(self.centralwidget)
        self.registrationButton.setGeometry(QtCore.QRect(310, 410, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.registrationButton.setFont(font)
        self.registrationButton.setObjectName("registrationButton")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(150, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.atlantaZooLabel = QtWidgets.QLabel(self.centralwidget)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(290, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.atlantaZooLabel.setFont(font)
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 140, 381, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 230, 381, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        LoginPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "LoginPage"))
        self.loginButton.setText(_translate("LoginPage", "Login"))
        self.registrationButton.setText(_translate("LoginPage", "Registration"))
        self.emailLabel.setText(_translate("LoginPage", "Email"))
        self.passwordLabel.setText(_translate("LoginPage", "Password"))
        self.atlantaZooLabel.setText(_translate("LoginPage", "Atlanta Zoo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())

