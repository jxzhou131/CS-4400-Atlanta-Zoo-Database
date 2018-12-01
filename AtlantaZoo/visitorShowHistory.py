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

import mysql.connector

headerDict = {
    0: "ShowName",
    1: "DateTime",
    2: "Exhibit"
}

orderDict = {
    0: "ASC",
    1: "DESC"
}

app = QtWidgets.QApplication(sys.argv)
################################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 818, 505))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.homeButton = QtWidgets.QPushButton(self.widget)
        self.homeButton.setMinimumSize(QtCore.QSize(91, 51))
        self.homeButton.setMaximumSize(QtCore.QSize(91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout_2.addWidget(self.homeButton, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(154, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 2)
        self.exhibitHistoryLabel = QtWidgets.QLabel(self.widget)
        self.exhibitHistoryLabel.setMaximumSize(QtCore.QSize(231, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.exhibitHistoryLabel.setFont(font)
        self.exhibitHistoryLabel.setObjectName("exhibitHistoryLabel")
        self.gridLayout_2.addWidget(self.exhibitHistoryLabel, 0, 4, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(274, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 7, 1, 2)
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setMinimumSize(QtCore.QSize(112, 23))
        self.label_title.setMaximumSize(QtCore.QSize(175, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(637, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setMaximumSize(QtCore.QSize(71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nameLineEdit.setMaximumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)
        self.timeLabel = QtWidgets.QLabel(self.widget)
        self.timeLabel.setMaximumSize(QtCore.QSize(58, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 0, 2, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setMaximumSize(QtCore.QSize(218, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setDate(QtCore.QDate(2017, 1, 1))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 3, 1, 1)
        self.exhibitLabel = QtWidgets.QLabel(self.widget)
        self.exhibitLabel.setMaximumSize(QtCore.QSize(91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.gridLayout.addWidget(self.exhibitLabel, 1, 0, 1, 1)
        self.exhibitComboBox = QtWidgets.QComboBox(self.widget)
        self.exhibitComboBox.setMaximumSize(QtCore.QSize(196, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.exhibitComboBox.setFont(font)
        self.exhibitComboBox.setObjectName("exhibitComboBox")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.exhibitComboBox.addItem("")
        self.gridLayout.addWidget(self.exhibitComboBox, 1, 1, 1, 1)
        self.allTimeCheckBox = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.allTimeCheckBox.setFont(font)
        self.allTimeCheckBox.setObjectName("allTimeCheckBox")
        self.gridLayout.addWidget(self.allTimeCheckBox, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 8)
        spacerItem3 = QtWidgets.QSpacerItem(305, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 5)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setMinimumSize(QtCore.QSize(111, 41))
        self.searchButton.setMaximumSize(QtCore.QSize(111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 3, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(323, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 6, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMaximumSize(QtCore.QSize(734, 248))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 1, 1, 7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 4, 8, 1, 1)
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
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.exhibitHistoryLabel.setText(_translate("MainWindow", "Show History"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.timeLabel.setText(_translate("MainWindow", "Time:"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.exhibitLabel.setText(_translate("MainWindow", "Exhibit:"))
        self.exhibitComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.exhibitComboBox.setItemText(1, _translate("MainWindow", "Sahara"))
        self.exhibitComboBox.setItemText(2, _translate("MainWindow", "Pacific"))
        self.exhibitComboBox.setItemText(3, _translate("MainWindow", "Birds"))
        self.exhibitComboBox.setItemText(4, _translate("MainWindow", "Jungle"))
        self.exhibitComboBox.setItemText(5, _translate("MainWindow", "Mountainous"))
        self.allTimeCheckBox.setText(_translate("MainWindow", "All Time"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Exhibit"))


    def userDefinedInitialization(self):
        self.currentOrder = 1
        self.homeButton.clicked.connect(self.home)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
        self.searchShowHistory()
        self.allTimeCheckBox.setCheckState(2)
        header = self.tableWidget.horizontalHeader()
        header.sectionClicked.connect(self.searchShowHistory)
        self.searchButton.clicked.connect(self.searchShowHistory)
        self.searchShowHistory()

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

    def searchShowHistory(self, column = 1):
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
        cmdend1 = " order by " + headerDict[column] + " " + orderDict[self.currentOrder]
        if(self.currentOrder == 0):
            self.currentOrder = 1
        else: 
            self.currentOrder = 0
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

