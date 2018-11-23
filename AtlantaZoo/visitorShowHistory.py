# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorShowHistory.ui'
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

import sys
app = QtWidgets.QApplication(sys.argv)
################################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(200, 140, 201, 31))
        self.nameLineEdit.setMinimumSize(QtCore.QSize(201, 31))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(330, 280, 111, 41))
        self.searchButton.setMinimumSize(QtCore.QSize(111, 41))
        self.searchButton.setMaximumSize(QtCore.QSize(111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.exhibitLabel = QtWidgets.QLabel(self.centralwidget)
        self.exhibitLabel.setGeometry(QtCore.QRect(100, 210, 91, 31))
        self.exhibitLabel.setMinimumSize(QtCore.QSize(91, 31))
        self.exhibitLabel.setMaximumSize(QtCore.QSize(91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(491, 140, 218, 31))
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(218, 31))
        self.dateTimeEdit.setMaximumSize(QtCore.QSize(218, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setDate(QtCore.QDate(2017, 1, 1))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(100, 140, 71, 31))
        self.nameLabel.setMinimumSize(QtCore.QSize(71, 31))
        self.nameLabel.setMaximumSize(QtCore.QSize(71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.exhibitHistoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.exhibitHistoryLabel.setGeometry(QtCore.QRect(280, 60, 231, 51))
        self.exhibitHistoryLabel.setMinimumSize(QtCore.QSize(231, 51))
        self.exhibitHistoryLabel.setMaximumSize(QtCore.QSize(231, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.exhibitHistoryLabel.setFont(font)
        self.exhibitHistoryLabel.setObjectName("exhibitHistoryLabel")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 91, 51))
        self.homeButton.setMinimumSize(QtCore.QSize(91, 51))
        self.homeButton.setMaximumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(420, 140, 58, 31))
        self.timeLabel.setMinimumSize(QtCore.QSize(58, 31))
        self.timeLabel.setMaximumSize(QtCore.QSize(58, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.exhibitComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.exhibitComboBox.setGeometry(QtCore.QRect(203, 208, 196, 35))
        self.exhibitComboBox.setMinimumSize(QtCore.QSize(196, 35))
        self.exhibitComboBox.setMaximumSize(QtCore.QSize(196, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.exhibitComboBox.setFont(font)
        self.exhibitComboBox.setObjectName("exhibitComboBox")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.allTimeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.allTimeCheckBox.setGeometry(QtCore.QRect(714, 146, 81, 20))
        self.allTimeCheckBox.setMinimumSize(QtCore.QSize(81, 20))
        self.allTimeCheckBox.setMaximumSize(QtCore.QSize(81, 20))
        self.allTimeCheckBox.setObjectName("allTimeCheckBox")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(32, 351, 734, 212))
        self.tableWidget.setMinimumSize(QtCore.QSize(734, 212))
        self.tableWidget.setMaximumSize(QtCore.QSize(734, 212))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
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
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.exhibitLabel.setText(_translate("MainWindow", "Exhibit"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.exhibitHistoryLabel.setText(_translate("MainWindow", "Show History"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.timeLabel.setText(_translate("MainWindow", "Time"))
        self.exhibitComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.exhibitComboBox.setItemText(1, _translate("MainWindow", "Sahara"))
        self.exhibitComboBox.setItemText(2, _translate("MainWindow", "Pacific"))
        self.exhibitComboBox.setItemText(3, _translate("MainWindow", "Birds"))
        self.exhibitComboBox.setItemText(4, _translate("MainWindow", "Jungle"))
        self.exhibitComboBox.setItemText(5, _translate("MainWindow", "Mountainous"))
        self.allTimeCheckBox.setText(_translate("MainWindow", "All Time"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Exhibit"))


    def userDefinedInitialization(self):
        self.homeButton.clicked.connect(self.home)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
        # self.preloadTable()
        self.searchButton.clicked.connect(self.searchShowHistory)

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality']
        app.exit()

    def highlightRowOrToExhibit(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
        # Enter IF statement if the selected column is the exhibit column
        if(column == 2):
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

# select * from
# (select ShowName, DateTime from VISITSHOWS
# where Visitor = 'xavier_swenson') as vs
# natural join
# (select Name as ShowName, DateTime, Location as Exhibit
# from SHOWS) as s;
    # def preloadTable(self):
    #     # contruct the sql command
    #     cmdheader1 = "SELECT * from "
    #     cmdTemp1 = "(SELECT ShowName, DateTime from VISITSHOWS as v1 WHERE Visitor = \'" \
    #                 + __main__.loginIdentity[0][0] + "\') as vs"
    #     cmdNatJoin = " Natural Join "
    #     cmdTemp2 = "(SELECT Name as ShowName, Datetime, Location as Exhibit from SHOWS) as s"
    #     cmdend1 = "" # "order by NumVisits DESC"
    #     cmd1 = cmdheader1 + "(" + cmdTemp1 + cmdNatJoin + cmdTemp2 + ") " + cmdend1 + ";"

    #     # for DEBUGGING
    #     print("cmd1")
    #     print(cmd1)

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
    #             DATETIMECOLUMN = 1
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

    def searchShowHistory(self):
        ShowName = self.nameLineEdit.text().lstrip().rstrip()
        DateTime = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy hh:mm:ss AP")
        Exhibit = str(self.exhibitComboBox.currentText())

        if(self.allTimeCheckBox.isChecked()):
            DateTime = ""
        if(Exhibit == "All"):
            Exhibit = ""

        listTuple = [("ShowName", ShowName, "str"), ("DateTime", DateTime, "datetime") \
                    , ("Exhibit", Exhibit, "str")]

        # contruct the sql command
        cmdheader1 = "SELECT * from "
        cmdTemp1 = "(SELECT ShowName, DateTime from VISITSHOWS as v1 WHERE Visitor = \'" \
                    + __main__.loginIdentity[0][0] + "\') as vs"
        cmdNatJoin = " Natural Join "
        cmdTemp2 = "(SELECT Name as ShowName, Datetime, Location as Exhibit from SHOWS) as s"
        cmdend1 = "" # "order by NumVisits DESC"
        cmd1 = cmdheader1 + "(" + cmdTemp1 + cmdNatJoin + cmdTemp2 + ") "
        cmd1 = util.addWHERE(cmd1, listTuple) + cmdend1 + ";"
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
        try:
            # use cursor to execute sql command
            cursor.execute(cmd1)
            # there could have multiple lines of sql command
            # after all the command, retrieve the queries
            record = cursor.fetchall()
            # for DEBUGGING purpose
            print(record)
            # this statement clears all the rows
            self.tableWidget.setRowCount(0)
            for row_num, row_data in enumerate(record):
                # insert a new blank row
                # in other words, expand the table by inserting a new row
                self.tableWidget.insertRow(row_num)
                for column_num, data in enumerate(row_data):
                    # IMPORTANT
                    # first you must determine in which column does the DateTime attribute occur in your 
                    # query
                    DATETIMECOLUMN = 1
                    cellContent = None
                    if(column_num == DATETIMECOLUMN):
                        cellContent = data.strftime("%m/%d/%Y %I:%M:%S %p")
                    if(cellContent is None):
                        cellContent = str(data)
                    self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(cellContent))
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        # close the cursor and connection
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

def render():
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()  
    # close the MainWindow
    MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

