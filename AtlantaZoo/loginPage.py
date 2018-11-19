# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import sys
app = QtWidgets.QApplication(sys.argv)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(799, 538)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 779, 488))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.atlantaZooLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.atlantaZooLabel.setFont(font)
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.gridLayout.addWidget(self.atlantaZooLabel, 1, 4, 2, 6)
        spacerItem1 = QtWidgets.QSpacerItem(273, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(299, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 9, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 3, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 2)
        self.emailLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.gridLayout.addWidget(self.emailLabel, 4, 2, 1, 1)
        self.emailLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.gridLayout.addWidget(self.emailLineEdit, 4, 3, 1, 7)
        spacerItem5 = QtWidgets.QSpacerItem(159, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 10, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem6, 5, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 0, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 6, 1, 1, 2)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.passwordLineEdit, 6, 3, 1, 7)
        spacerItem8 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 6, 10, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem9, 7, 6, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 8, 0, 1, 6)
        self.loginButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)
        self.gridLayout.addWidget(self.loginButton, 8, 6, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(332, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 8, 7, 1, 4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem12, 9, 6, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(295, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 10, 0, 1, 5)
        self.registrationButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.registrationButton.setFont(font)
        self.registrationButton.setObjectName("registrationButton")
        self.registrationButton.clicked.connect(self.registration)
        self.gridLayout.addWidget(self.registrationButton, 10, 5, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(313, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 10, 8, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem15, 11, 6, 1, 1)
        LoginPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "LoginPage"))
        self.atlantaZooLabel.setText(_translate("LoginPage", "Atlanta Zoo"))
        self.emailLabel.setText(_translate("LoginPage", "Email"))
        self.passwordLabel.setText(_translate("LoginPage", "Password"))
        self.loginButton.setText(_translate("LoginPage", "Login"))
        self.registrationButton.setText(_translate("LoginPage", "Registration"))

    def login(self):
        # retrive the strings from the lineEdit object
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()
        # build the SQL query command
        cmd1 = "select * from USER where password = md5(\'" + password + "\') and email = \'" + email + "\';"
        # obtain the connection_object
        connection_object = connection_pool.get_connection()
        # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
        print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
        # get cursor
        cursor = connection_object.cursor()
        # use cursor to execute sql command
        cursor.execute(cmd1)
        # there could have multiple lines of sql command
        # after all the command, retrieve the queries
        record = cursor.fetchall()
        print(record)
        if(len(record) > 0):
            __main__.loginIdentity = record
            __main__.status = __main__.statusDef['Normal']
            __main__.state = 3 # exit Initial UIs
            app.exit()
        else:
            self.showEmailNotExists()
        # close the cursor and connection
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def registration(self):
        # before exiting the ui REPORT STATUS
        __main__.status = __main__.statusDef['Normal']
        __main__.state = 1 # registration Page
        # EXIT the ui
        app.exit()

    # def showEmailNotValid(self):
    #      d = QtWidgets.QDialog()
    #      b1= QtWidgets.QPushButton("close",d)
    #      bl.clicked.connect(lambda : d.exit())
    #      b1.move(50,50)
    #      d.setWindowTitle("showEmailNotValid")
    #      d.setWindowModality(QtCore.Qt.ApplicationModal)
    #      d.exec_()        

    def showEmailNotExists(self):
         d = QtWidgets.QDialog()
         b1= QtWidgets.QPushButton("close",d)
         b1.move(50,50)
         d.setWindowTitle("showEmailNotExists")
         d.setWindowModality(QtCore.Qt.ApplicationModal)
         d.exec_()

def render():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    app.exec_()
    # close the WINDOWS
    LoginPage.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    app.exec_()
    # close the WINDOWS
    LoginPage.close()

