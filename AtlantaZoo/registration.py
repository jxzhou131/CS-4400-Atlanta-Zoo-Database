# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import re

import sys
app = QtWidgets.QApplication(sys.argv)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(3, 11, 936, 378))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 5)
        self.Homebutton = QtWidgets.QPushButton(self.widget)
        self.Homebutton.setObjectName("Homebutton")
        self.Homebutton.clicked.connect(self.Home)
        self.gridLayout.addWidget(self.Homebutton, 0, 0, 1, 1)
        self.Heading_register = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.Heading_register.setFont(font)
        self.Heading_register.setObjectName("Heading_register")
        self.gridLayout.addWidget(self.Heading_register, 1, 5, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(182, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 9, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 9, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(749, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 9)
        spacerItem5 = QtWidgets.QSpacerItem(306, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 7, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(17, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem7, 8, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 5, 9, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(17, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem9, 6, 6, 1, 1)
        self.registerStaffPushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.registerStaffPushButton.setFont(font)
        self.registerStaffPushButton.setObjectName("registerStaffPushButton")
        self.registerStaffPushButton.clicked.connect(self.register("STAFF"))
        self.gridLayout.addWidget(self.registerStaffPushButton, 7, 6, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(183, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 0, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 4, 9, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(17, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem12, 8, 6, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(17, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem13, 6, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(202, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 7, 8, 1, 2)
        self.label_email = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.gridLayout.addWidget(self.label_email, 2, 3, 1, 1)
        self.registerVisitorPushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.registerVisitorPushButton.setFont(font)
        self.registerVisitorPushButton.setObjectName("registerVisitorPushButton")
        self.registerVisitorPushButton.clicked.connect(self.register("VISITOR"))
        self.gridLayout.addWidget(self.registerVisitorPushButton, 7, 3, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(212, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 7, 0, 1, 3)
        self.emailLineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setText("")
        self.emailLineEdit.setMaxLength(50)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.gridLayout.addWidget(self.emailLineEdit, 2, 4, 1, 5)
        self.label_username = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 3, 2, 1, 2)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.gridLayout.addWidget(self.usernameLineEdit, 3, 4, 1, 5)
        self.label_password = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 4, 2, 1, 2)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.gridLayout.addWidget(self.passwordLineEdit, 4, 4, 1, 5)
        self.confirmPasswordLineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.confirmPasswordLineEdit.setFont(font)
        self.confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.confirmPasswordLineEdit.setObjectName("confirmPasswordLineEdit")
        self.gridLayout.addWidget(self.confirmPasswordLineEdit, 5, 4, 1, 5)
        self.label_confirmpassword = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_confirmpassword.setFont(font)
        self.label_confirmpassword.setObjectName("label_confirmpassword")
        self.gridLayout.addWidget(self.label_confirmpassword, 5, 1, 1, 3)
        spacerItem16 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Homebutton.setText(_translate("MainWindow", "Login"))
        self.Heading_register.setText(_translate("MainWindow", "Registration"))
        self.registerStaffPushButton.setText(_translate("MainWindow", "Register Staff"))
        self.label_email.setText(_translate("MainWindow", "Email:"))
        self.registerVisitorPushButton.setText(_translate("MainWindow", "Register Visitor"))
        self.label_username.setText(_translate("MainWindow", "   Username:"))
        self.label_password.setText(_translate("MainWindow", "    Password:"))
        self.label_confirmpassword.setText(_translate("MainWindow", "   Confirm password:"))

    def Home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.initialUIs['loginPage'] # Login Page
        app.exit()

    def register(self, userType):
        def _register():
            email = self.emailLineEdit.text()
            username = self.usernameLineEdit.text()
            password = self.passwordLineEdit.text()
            confirmPassword = self.confirmPasswordLineEdit.text()
            if(password == confirmPassword):
                # build the SQL query command
                UserType = ""
                if(userType == "VISITOR"):
                    UserType = "VUsername"
                elif(userType == "STAFF"):
                    UserType = "SUsername"

                cmd1 = "select * from " + userType + " where " + UserType + " = \'" + username + "\' ;"
                cmd2 = "insert into USER values(\'" + username + "\' , md5(\'" + password + "\') , \'" + email + "\' , \'" + userType.lower() + "\' );"
                cmd3 = "insert into " + userType + " values(\'" + username + "\');"
                # additional query to ensure that the USER record has been added to the database
                cmd4 = "select * from USER where Password = md5(\'" + password + "\') and Email = \'" + email + "\' ;"
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
                # close the cursor and connection
                # if the record is empty 
                # USER DOES NOT EXIST
                if(len(record) == 0):
                    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                        cursor.execute(cmd2)
                        cursor.execute(cmd3)
                        # for any changes/ alteration that should be done
                        # you MUST commit for the transaction to be executed
                        connection_object.commit()
                        cursor.execute(cmd4)
                        record = cursor.fetchall()
                        if(len(record) == 0):
                            self.showUsernameNotExists()
                        else:
                            __main__.loginIdentity = record
                            __main__.status = __main__.statusDef['Normal']
                            __main__.state = __main__.initialUIs['exitInitialUIs'] # exit initial UIs
                            print("loginIdentity")
                            print(__main__.loginIdentity)
                            app.exit()
                    else:
                        self.showEmailNotValid()
                else:
                    self.showUsernameExists()
                # close the cursor and connection   
                if(connection_object.is_connected()):
                    cursor.close()
                    connection_object.close()
                    print("MySQL connection is closed")
            else:
                self.showPasswordMissMatchDialog()
        return _register

    def showPasswordMissMatchDialog(self):
         d = QtWidgets.QDialog()
         d.setMinimumSize(350, 50)
         b1= QtWidgets.QPushButton("close",d)
         b1.move(50,50)
         b1.clicked.connect(lambda : d.close())
         d.setWindowTitle("PasswordsMissMatch")
         d.setWindowModality(QtCore.Qt.ApplicationModal)
         d.exec_()

    def showUsernameExists(self):
         d = QtWidgets.QDialog()
         d.setMinimumSize(350, 50)
         b1= QtWidgets.QPushButton("close",d)
         b1.clicked.connect(lambda : d.close())
         b1.move(50,50)
         d.setWindowTitle("showUsernameExists")
         d.setWindowModality(QtCore.Qt.ApplicationModal)
         d.exec_()

    def showUsernameNotExists(self):
         d = QtWidgets.QDialog()
         d.setMinimumSize(350, 50)
         b1= QtWidgets.QPushButton("close",d)
         b1.clicked.connect(lambda : d.close())
         b1.move(50,50)
         d.setWindowTitle("showUsernameNotExists")
         d.setWindowModality(QtCore.Qt.ApplicationModal)
         d.exec_()

    def showEmailNotValid(self):
         d = QtWidgets.QDialog()
         d.setMinimumSize(350, 50)
         b1= QtWidgets.QPushButton("close",d)
         b1.clicked.connect(lambda : d.close())
         b1.move(50,50)
         d.setWindowTitle("showEmailNotValid")
         d.setWindowModality(QtCore.Qt.ApplicationModal)
         d.exec_()     

def render():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    MainWindow.close()

