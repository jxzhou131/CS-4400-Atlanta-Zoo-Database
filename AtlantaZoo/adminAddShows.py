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
        MainWindow.resize(632, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 596, 435))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_home = QtWidgets.QPushButton(self.widget)
        self.button_home.setMinimumSize(QtCore.QSize(117, 48))
        self.button_home.setMaximumSize(QtCore.QSize(117, 48))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.gridLayout_2.addWidget(self.button_home, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.label_header = QtWidgets.QLabel(self.widget)
        self.label_header.setMinimumSize(QtCore.QSize(201, 50))
        self.label_header.setMaximumSize(QtCore.QSize(201, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.gridLayout_2.addWidget(self.label_header, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(195, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 3)
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setMinimumSize(QtCore.QSize(111, 24))
        self.label_title.setMaximumSize(QtCore.QSize(111, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setMinimumSize(QtCore.QSize(100, 27))
        self.label_name.setMaximumSize(QtCore.QSize(100, 27))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_exb = QtWidgets.QLabel(self.widget)
        self.label_exb.setMinimumSize(QtCore.QSize(100, 30))
        self.label_exb.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_exb.setFont(font)
        self.label_exb.setObjectName("label_exb")
        self.gridLayout.addWidget(self.label_exb, 1, 0, 1, 1)
        self.comboBox_staff = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.comboBox_staff.setFont(font)
        self.comboBox_staff.setObjectName("comboBox_staff")
        self.gridLayout.addWidget(self.comboBox_staff, 2, 1, 1, 1)
        self.comboBox_exb = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.comboBox_exb.setFont(font)
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.gridLayout.addWidget(self.comboBox_exb, 1, 1, 1, 1)
        self.label_staff = QtWidgets.QLabel(self.widget)
        self.label_staff.setMinimumSize(QtCore.QSize(100, 28))
        self.label_staff.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_staff.setFont(font)
        self.label_staff.setObjectName("label_staff")
        self.gridLayout.addWidget(self.label_staff, 2, 0, 1, 1)
        self.label_date = QtWidgets.QLabel(self.widget)
        self.label_date.setMinimumSize(QtCore.QSize(100, 35))
        self.label_date.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.gridLayout.addWidget(self.label_date, 3, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 3, 3)
        spacerItem2 = QtWidgets.QSpacerItem(199, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 3, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 3, 1, 1)
        self.button_add_show = QtWidgets.QPushButton(self.widget)
        self.button_add_show.setMinimumSize(QtCore.QSize(113, 32))
        self.button_add_show.setMaximumSize(QtCore.QSize(113, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.button_add_show.setFont(font)
        self.button_add_show.setObjectName("button_add_show")
        self.gridLayout_2.addWidget(self.button_add_show, 3, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 111, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 4, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.label_header.setText(_translate("MainWindow", "Add Shows"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit:"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Birds"))
        self.label_staff.setText(_translate("MainWindow", "Staff:"))
        self.label_date.setText(_translate("MainWindow", "DateTime:"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.button_add_show.setText(_translate("MainWindow", "Add Show"))

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality'] # administratorFunctionality Page
        app.exit()

    def userDefinedInitialization(self):
        self.button_home.clicked.connect(self.home)
        self.button_add_show.clicked.connect(self.addShows)
        self.populateStaffComboBox()

    def populateStaffComboBox(self):
        # construct query command
        cmd = " SELECT * FROM STAFF;"
        # obtain the connection_object
        connection_object = connection_pool.get_connection()
        # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
        print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
        # get cursor
        cursor = connection_object.cursor()        
        cursor.execute(cmd)
        result = cursor.fetchall()
        # close the cursor and connection
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")
        for staff in result:
            self.comboBox_staff.addItem(staff[0])

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

