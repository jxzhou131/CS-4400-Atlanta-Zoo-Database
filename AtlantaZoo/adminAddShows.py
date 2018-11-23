# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminAddShows.ui'
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

import util

import mysql.connector

import sys
app = QtWidgets.QApplication(sys.argv)
################################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(50, 120, 60, 16))
        self.label_name.setObjectName("label_name")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(50, 250, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(13)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.comboBox_exb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_exb.setGeometry(QtCore.QRect(100, 160, 111, 41))
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.label_staff = QtWidgets.QLabel(self.centralwidget)
        self.label_staff.setGeometry(QtCore.QRect(50, 210, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(13)
        self.label_staff.setFont(font)
        self.label_staff.setObjectName("label_staff")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(340, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.comboBox_staff = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_staff.setGeometry(QtCore.QRect(90, 210, 131, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_staff.setFont(font)
        self.comboBox_staff.setObjectName("comboBox_staff")
        self.comboBox_staff.addItem("")
        self.comboBox_staff.addItem("")
        self.comboBox_staff.addItem("")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(10, 10, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.label_exb = QtWidgets.QLabel(self.centralwidget)
        self.label_exb.setGeometry(QtCore.QRect(50, 170, 60, 16))
        self.label_exb.setObjectName("label_exb")
        self.button_add_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_show.setGeometry(QtCore.QRect(440, 170, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_add_show.setFont(font)
        self.button_add_show.setObjectName("button_add_show")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(30, 50, 91, 16))
        self.label_title.setObjectName("label_title")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(110, 250, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 120, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_date.setText(_translate("MainWindow", "DateTime"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Birds"))
        self.label_staff.setText(_translate("MainWindow", "Staff"))
        self.label_header.setText(_translate("MainWindow", "Add Shows"))
        self.comboBox_staff.setItemText(0, _translate("MainWindow", "martha_johnson"))
        self.comboBox_staff.setItemText(1, _translate("MainWindow", "benjamin_rao"))
        self.comboBox_staff.setItemText(2, _translate("MainWindow", "ethan_roswell"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit"))
        self.button_add_show.setText(_translate("MainWindow", "Add Show"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality'] # administratorFunctionality Page
        app.exit()

    def userDefinedInitialization(self):
        self.button_home.clicked.connect(self.home)
        self.button_add_show.clicked.connect(self.addShows)

    def addShows(self):
        Name = self.lineEdit.text()
        DateTime = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy hh:mm:ss AP")
        Host = self.comboBox_staff.currentText()
        Location = self.comboBox_exb.currentText()

        if Name.lstrip().rstrip() == "" or Host.lstrip().rstrip() == "" or Location.lstrip().rstrip() == "":
            self.InformationNotComplete()
            return

        else:

            # obtain the connection_object
            connection_object = connection_pool.get_connection()
            # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
            if connection_object.is_connected():
                db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
            # get cursor
            cursor = connection_object.cursor()
            # SELECT DateTime, Host
            # FROM Shows
            # Where DateTime = STR_TO_DATE('2018/10/10 4:00:00 PM','%m/%d/%Y %r') and Host = 'benjamin_rao'
            cmd_query = "SELECT DateTime, Host From SHOWS"
            listTuple = [("DateTime", DateTime, "datatime"), ("Host", Host, "str")]
            cmd_query = util.addWHERE(cmd_query, listTuple)  + ";"
            cursor.execute(cmd_query)
            result = cursor.fetchall()
            if len(result) == 0:
                cmd = "INSERT INTO SHOWS VALUES (\'" + Name + "\', STR_TO_DATE(\'" + DateTime + "\',\'%m/%d/%Y %r\'), \'" + Host +"\', \'"+ Location + "\');"
                # use cursor to execute sql command
                try:
                    cursor.execute(cmd)
                    connection_object.commit()
                    self.Insert_successful()
                except mysql.connector.IntegrityError as err:
                    self.IntegrityError()
                    print("Error: {}", format(err))

            else:
                self.cannotAdd()

            # close the cursor and connection
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")


    def InformationNotComplete(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("Information is not complete")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_() 

    def IntegrityError(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("Integrity Error")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_() 

    def cannotAdd(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("A staff cannot host multiple shows at the same time")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def Insert_successful(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("Insertion Successful")
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
        # close the WINDOWS
        MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

