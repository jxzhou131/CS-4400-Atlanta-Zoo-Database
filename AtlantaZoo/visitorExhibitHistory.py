# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorExhibitHistory.ui'
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
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.exhibitHistoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.exhibitHistoryLabel.setGeometry(QtCore.QRect(280, 60, 231, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.exhibitHistoryLabel.setFont(font)
        self.exhibitHistoryLabel.setObjectName("exhibitHistoryLabel")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(100, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.NoVLabel = QtWidgets.QLabel(self.centralwidget)
        self.NoVLabel.setGeometry(QtCore.QRect(100, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.NoVLabel.setFont(font)
        self.NoVLabel.setObjectName("NoVLabel")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(430, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(200, 140, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.searchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QtCore.QRect(330, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.searchPushButton.setFont(font)
        self.searchPushButton.setObjectName("searchPushButton")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(500, 140, 201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.numVisitsMinSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.numVisitsMinSpinBox.setGeometry(QtCore.QRect(370, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.numVisitsMinSpinBox.setFont(font)
        self.numVisitsMinSpinBox.setObjectName("numVisitsMinSpinBox")
        self.minLabel = QtWidgets.QLabel(self.centralwidget)
        self.minLabel.setGeometry(QtCore.QRect(300, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.minLabel.setFont(font)
        self.minLabel.setObjectName("minLabel")
        self.maxLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxLabel.setGeometry(QtCore.QRect(460, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.maxLabel.setFont(font)
        self.maxLabel.setObjectName("maxLabel")
        self.numVisitsMaxSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.numVisitsMaxSpinBox.setGeometry(QtCore.QRect(540, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.numVisitsMaxSpinBox.setFont(font)
        self.numVisitsMaxSpinBox.setObjectName("numVisitsMaxSpinBox")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(62, 346, 678, 213))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.dateTimeCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.dateTimeCheckBox.setGeometry(QtCore.QRect(711, 147, 81, 20))
        self.dateTimeCheckBox.setObjectName("dateTimeCheckBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.userDefinedInitialization()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExhibitHistory"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.exhibitHistoryLabel.setText(_translate("MainWindow", "Exhibit History"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.NoVLabel.setText(_translate("MainWindow", "Number of Visits"))
        self.timeLabel.setText(_translate("MainWindow", "Time"))
        self.searchPushButton.setText(_translate("MainWindow", "Search"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.minLabel.setText(_translate("MainWindow", "(Min)"))
        self.maxLabel.setText(_translate("MainWindow", "(Max)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Number of Visits"))
        self.dateTimeCheckBox.setText(_translate("MainWindow", "All Time"))


    def userDefinedInitialization(self):
        self.homeButton.clicked.connect(self.home)
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
        # self.preloadTable()
        self.searchPushButton.clicked.connect(self.searchExhibitHistory)
        self.numVisitsMaxSpinBox.setMinimum(0)
        self.numVisitsMinSpinBox.setMinimum(0)
        self.numVisitsMaxSpinBox.setMaximum(100)
        self.numVisitsMinSpinBox.setMaximum(100)

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality']
        app.exit()


    def highlightRowOrToExhibit(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
        # Enter IF statement if the selected column is the exhibit column
        if(column == 0):
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

# -- search for all records
# -- when there are no inputs, range == no input if min > max
# select * from 
# ((select ExhibitName, DateTime 
# from VISITEXHIBIT as v2
# where Visitor = 'robert_bernheardt') as visitExhibit1
# Natural Join
# (select ExhibitName, count(*) as numVisits 
# from VISITEXHIBIT as v1
# where Visitor = 'robert_bernheardt'
# group by ExhibitName
# order by numVisits) as visitExhibit2)
# order by numVisits DESC;

    # def preloadTable(self):
    #     # contruct the sql command
    #     cmdheader1 = "SELECT * from "
    #     cmdTemp1 = "(SELECT ExhibitName, DateTime from VISITEXHIBIT as v1 WHERE Visitor = \'" \
    #                 + __main__.loginIdentity[0][0] + "\') as visitExhibit1"
    #     cmdNatJoin = " Natural Join "
    #     cmdTemp2 = "(SELECT ExhibitName, count(*) as NumVisits FROM VISITEXHIBIT as v2 WHERE Visitor = \'" \
    #                 + __main__.loginIdentity[0][0] + "\' group by ExhibitName order by NumVisits) as visitExhibit2"
    #     cmdend1 = "order by NumVisits DESC"
    #     cmd1 = cmdheader1 + "(" + cmdTemp1 + cmdNatJoin + cmdTemp2 + ") " + cmdend1 + ";"
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

    def searchExhibitHistory(self):
        ExhibitName = self.nameLineEdit.text().lstrip().rstrip()
        DateTime = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy hh:mm:ss AP")
        NumVisitsMin = str(self.numVisitsMinSpinBox.value())
        NumVisitsMax = str(self.numVisitsMaxSpinBox.value())

        if(self.dateTimeCheckBox.isChecked()):
            DateTime = ""
        if(NumVisitsMin == "0" and NumVisitsMax == "0"):
            NumVisitsMin = ""
            NumVisitsMax = ""
        listTuple = [("ExhibitName", ExhibitName, "str"), ("DateTime", DateTime, "datetime") \
                    , ("NumVisitsMin", NumVisitsMin, "int"), ("NumVisitsMax", NumVisitsMax, "int")]

        # contruct the sql command
        cmdheader1 = "SELECT * from "
        cmdTemp1 = "(SELECT ExhibitName, DateTime from VISITEXHIBIT as v1 WHERE Visitor = \'" \
                    + __main__.loginIdentity[0][0] + "\') as visitExhibit1"
        cmdNatJoin = " Natural Join "
        cmdTemp2 = "(SELECT ExhibitName, count(*) as NumVisits FROM VISITEXHIBIT as v2 WHERE Visitor = \'" \
                    + __main__.loginIdentity[0][0] + "\' group by ExhibitName order by NumVisits) as visitExhibit2"
        cmdend1 = " order by NumVisits DESC"
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
    #close the MainWindow
    MainWindow.close()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

