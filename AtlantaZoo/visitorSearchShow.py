# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorSearchShow.ui'
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

import time

import mysql.connector

import sys
app = QtWidgets.QApplication(sys.argv)
################################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(6, 5, 778, 599))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_home = QtWidgets.QPushButton(self.widget)
        self.button_home.setMinimumSize(QtCore.QSize(120, 50))
        self.button_home.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.gridLayout_2.addWidget(self.button_home, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label_header = QtWidgets.QLabel(self.widget)
        self.label_header.setMinimumSize(QtCore.QSize(116, 39))
        self.label_header.setMaximumSize(QtCore.QSize(116, 39))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.gridLayout_2.addWidget(self.label_header, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(322, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 2)
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setMinimumSize(QtCore.QSize(105, 33))
        self.label_title.setMaximumSize(QtCore.QSize(105, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(631, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setMinimumSize(QtCore.QSize(79, 22))
        self.label_name.setMaximumSize(QtCore.QSize(79, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(211, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_date = QtWidgets.QLabel(self.widget)
        self.label_date.setMinimumSize(QtCore.QSize(62, 21))
        self.label_date.setMaximumSize(QtCore.QSize(62, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.gridLayout.addWidget(self.label_date, 0, 2, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(225, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 3, 1, 1)
        self.label_exb = QtWidgets.QLabel(self.widget)
        self.label_exb.setMinimumSize(QtCore.QSize(79, 24))
        self.label_exb.setMaximumSize(QtCore.QSize(79, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_exb.setFont(font)
        self.label_exb.setObjectName("label_exb")
        self.gridLayout.addWidget(self.label_exb, 1, 0, 1, 1)
        self.comboBox_exb = QtWidgets.QComboBox(self.widget)
        self.comboBox_exb.setMinimumSize(QtCore.QSize(210, 38))
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
        self.comboBox_exb.addItem("")
        self.gridLayout.addWidget(self.comboBox_exb, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setMinimumSize(QtCore.QSize(185, 20))
        self.checkBox.setMaximumSize(QtCore.QSize(185, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(309, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 0, 1, 3)
        self.button_search = QtWidgets.QPushButton(self.widget)
        self.button_search.setMinimumSize(QtCore.QSize(106, 37))
        self.button_search.setMaximumSize(QtCore.QSize(106, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.button_search.setFont(font)
        self.button_search.setObjectName("button_search")
        self.gridLayout_2.addWidget(self.button_search, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 4, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMinimumSize(QtCore.QSize(646, 230))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 1, 1, 4)
        spacerItem8 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(296, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 5, 0, 1, 3)
        self.button_log_visit = QtWidgets.QPushButton(self.widget)
        self.button_log_visit.setMinimumSize(QtCore.QSize(119, 41))
        self.button_log_visit.setMaximumSize(QtCore.QSize(119, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.button_log_visit.setFont(font)
        self.button_log_visit.setObjectName("button_log_visit")
        self.gridLayout_2.addWidget(self.button_log_visit, 5, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(325, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 5, 4, 1, 2)
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
        self.label_header.setText(_translate("MainWindow", "Shows"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_date.setText(_translate("MainWindow", "Date:"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit:"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(5, _translate("MainWindow", "Birds"))
        self.checkBox.setText(_translate("MainWindow", "All Date and Time"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Exhibit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        self.button_log_visit.setText(_translate("MainWindow", "Log Visit"))
        
    def userDefinedInitialization(self):
        self.button_home.clicked.connect(self.home)
        self.button_search.clicked.connect(self.searchShow)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
        # self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.button_log_visit.clicked.connect(self.logVisit)
        # self.preloadTable()

    def highlightRowOrToExhibit(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
        # Enter IF statement if the selected column is the exhibit column
        if(column == 1):
            # retrieve the content in the cell
            Name = str(self.tableWidget.item(row,column).text())
            # store the information into the __main__.arg
            # the information is later passed to the exhibitDetails page
            __main__.arg = [("Name", Name, "str")]
            __main__.status = __main__.statusDef["Normal"]
            __main__.state = __main__.visitorUIs["exhibitDetails"]
            app.exit()
            # FOR DEBUGGING PURPOSE
            print("row, column, ExhibitName")
            print(str(row) + "," + str(column) + "," + Name)

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality']
        app.exit()

    # def preloadTable(self):
    #     cmd1 = "SELECT Name, Location as Exhibit, DateTime from SHOWS ;"
    #     # obtain the connection_object
    #     connection_object = connection_pool.get_connection()
    #     # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
    #     if connection_object.is_connected():
    #         db_Info = connection_object.get_server_info()
    #     print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
    #     # get cursor
    #     cursor = connection_object.cursor()
    #     # use cursor to execute sql command
    #     cursor.execute(cmd1)
    #     # there could have multiple lines of sql command
    #     # after all the command, retrieve the queries
    #     record = cursor.fetchall()
    #     # for DEBUGGING purpose
    #     print(record)
    #     # this statement clears all the rows
    #     self.tableWidget.setRowCount(0)
    #     for row_num, row_data in enumerate(record):
    #         # insert a new blank row
    #         # in other words, expand the table by inserting a new row
    #         self.tableWidget.insertRow(row_num)
    #         for column_num, data in enumerate(row_data):
    #             # IMPORTANT
    #             # first you must determine in which column does the DateTime attribute occur in your 
    #             # query
    #             DATETIMECOLUMN = 2
    #             cellContent = None
    #             if(column_num == DATETIMECOLUMN):
    #                 cellContent = data.strftime("%m/%d/%Y %I:%M:%S %p")
    #             if(cellContent is None):
    #                 cellContent = str(data)
    #             self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(cellContent))

    #     # close the cursor and connection
    #     if(connection_object.is_connected()):
    #         cursor.close()
    #         connection_object.close()
    #         print("MySQL connection is closed")

    def searchShow(self):
        Name = self.lineEdit_name.text().lstrip().rstrip()
        Location = str(self.comboBox_exb.currentText())
        DateTime = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy hh:mm:ss AP")

        if(Location == "All"):
            Location = ""

        if(self.checkBox.isChecked()):
            DateTime = ""

        listTuple = [('Name', Name, "str"), ("Location", Location, "str"), ("DateTime", DateTime, "datetime")]

        cmd1 = "SELECT Name, Location as Exhibit, DateTime from SHOWS "
        cmd1 = util.addWHERE(cmd1, listTuple)
        cmd1 += ";"
        # DEBUG OUTPUT
        print("listTuple")
        print(listTuple)
        print("cmd1")
        print(cmd1)
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
        # for DEBUGGING purpose only
        print(record)
        # this statement clear all the rows in the table
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(record):
            # insert a new blank row
            # in other words, expand the table by inserting a new row
            self.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                # IMPORTANT
                DATETIMECOLUMN = 2
                cellContent = None
                if(column_num == DATETIMECOLUMN):
                    cellContent = data.strftime("%m/%d/%Y %I:%M:%S %p")
                if(cellContent == None):
                    cellContent = str(data)
                self.tableWidget.setItem(row_num, column_num,QtWidgets.QTableWidgetItem(cellContent))

        # close the cursor and connection
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def logVisit(self):
        rowsSelected = self.tableWidget.selectionModel().selectedRows()
        
        if(len(rowsSelected) >0):
            index = rowsSelected[0]
            # index consist of row() column()
            row = index.row()
            Visitor = __main__.loginIdentity[0][0]
            ShowName = self.tableWidget.item(row,0).text()
            ExhibitName = self.tableWidget.item(row,1).text()
            DateTime = self.tableWidget.item(row,2).text()
            print("DateTime")
            print(DateTime)

            cmd1 = "INSERT INTO VISITSHOWS VALUES (\'" + Visitor + "\' , \'" + ShowName + "\' , STR_TO_DATE(\'" + DateTime + "\' , \'%m/%d/%Y %r\') );"
            cmd2 = "INSERT INTO VISITEXHIBIT VALUES (\'" + Visitor + "\' , \'" + ExhibitName + "\' , STR_TO_DATE(\'" + DateTime + "\' , \'%m/%d/%Y %r\') );"
            print("cmd1: " + cmd1)
            print("cmd2: " + cmd2)
            # obtain the connection_object
            connection_object = connection_pool.get_connection()
            # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
            if connection_object.is_connected():
                db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
            # get cursor
            cursor = connection_object.cursor()
            ########## This block of code is used to catch the exception in the database################
            ########## To detect whether there already exist such tuples which violates ################
            ########## PRIMARY KEY INTEGRITY
            try:
                # use cursor to execute sql command
                cursor.execute(cmd1)
                cursor.execute(cmd2)
                # commit your transaction
                connection_object.commit()
                print("Insert Successfully")
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
                self.showCannotLogVisitMultipleTimes()
            #########################################################################################
            # close the cursor and connection
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
        else:
            print("No row is selected")


    def showCannotLogVisitMultipleTimes(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("Cannot Log Visit Multiple Times")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()  

def render():
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

