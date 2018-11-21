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
        self.label_name.setGeometry(QtCore.QRect(61, 148, 74, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(10, 20, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.button_rmv_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_rmv_show.setGeometry(QtCore.QRect(312, 476, 129, 43))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_rmv_show.setFont(font)
        self.button_rmv_show.setObjectName("button_rmv_show")
        self.comboBox_exb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_exb.setGeometry(QtCore.QRect(146, 201, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.comboBox_exb.setFont(font)
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(30, 60, 91, 16))
        self.label_title.setObjectName("label_title")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(431, 144, 225, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(319, 23, 116, 46))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(390, 210, 105, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_search.setFont(font)
        self.button_search.setObjectName("button_search")
        self.label_exb = QtWidgets.QLabel(self.centralwidget)
        self.label_exb.setGeometry(QtCore.QRect(51, 213, 79, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_exb.setFont(font)
        self.label_exb.setObjectName("label_exb")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(144, 145, 211, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(368, 149, 62, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 260, 601, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(665, 149, 133, 20))
        self.checkBox.setObjectName("checkBox")
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
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.button_rmv_show.setText(_translate("MainWindow", "Log Visit"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(5, _translate("MainWindow", "Birds"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_header.setText(_translate("MainWindow", "Shows"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit"))
        self.label_date.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Exhibit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        self.checkBox.setText(_translate("MainWindow", "All Date and Time"))

    def userDefinedInitialization(self):
        self.button_home.clicked.connect(self.home)
        self.button_search.clicked.connect(self.searchShow)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.preloadTable()

    def highlightRowOrToExhibit(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
        # retrieve the content in the cell
        if(column == 1):
            Name = str(self.tableWidget.item(row,column).text())
            __main__.arg = [("Name", Name)]
            __main__.status = __main__.statusDef["Normal"]
            __main__.state = __main__.visitorUIs["exhibitDetail"]
        print("row, column, text")
        print(str(row) + "," + str(column) + "," + text)

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality']
        app.exit()

    def preloadTable(self):
        cmd1 = "SELECT Name, Location as Exhibit, DateTime from SHOWS ;"
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
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(record):
            self.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                # IMPORTANT
                # first you must determine in which column does the DateTime attribute occur in your 
                # query
                DATETIMECOLUMN = 2
                cellContent = None
                if(column_num == DATETIMECOLUMN):
                    cellContent = data.strftime("%m/%d/%Y %I:%M:%S %p")
                if(cellContent is None):
                    cellContent = str(data)
                self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(cellContent))

        # close the cursor and connection
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def searchShow(self):
        Name = self.lineEdit_name.text().lstrip().rstrip()
        Location = str(self.comboBox_exb.currentText())
        DateTime = self.dateTimeEdit.dateTime().toString("MM-dd-yyyy hh:mm:ss AP")

        if(Location == "All"):
            Exhibit = ""

        if(self.checkBox.isChecked()):
            DateTime = ""

        dictVar = {'Name': Name, "Location": Location, "DateTime": DateTime}

        cmd1 = "SELECT Name, Location as Exhibit, DateTime from SHOWS "
        cmd1 = util.addWHERE(cmd1, dictVar)
        # DEBUG OUTPUT
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

        print(record)

        # CONVERT DATETIME TO STRING
        # Example
        # print(record[0][1].strftime("%m/%d/%Y %I:%M:%S %p"))

        # Try datetime
        # print(time.strftime("%m/%d/%Y %I:%M:%S %p"))
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(record):
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
        # dt.toString("dd.MM.yyyy hh:mm:ss.zzz"))
        # dt_string = dt.toString(self.dateTimeEdit.displayFormat())
        pass


    # def addWHERE(cmd, dictVar):
    #     """ 
    #         How to create dictVar outside of this function?
    #         -----------------------------------------------
    #         Email = self.emailLineEdit.text()
    #         Username = self.usernameLineEdit.text()

    #         dictVar = {"Email": Email, "Username": Username}

    #         INPUTS
    #         =======
    #         cmd: command to be concatenated with WHERE conditions
    #         dictVar: contains {'name of variable': "value of variable"}
    #     """
    #     numWhereClausesAdded = 0
    #     for name, value in dictVar.item():
    #         if(value.lstrip().rstrip() == ""):
    #             if(numWhereClausesAdded == 0):
    #                 cmd += " WHERE "
    #             else:
    #                 cmd += " AND "
    #             cmd += (name + " = " + value)
    #     cmd += " ;"


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

