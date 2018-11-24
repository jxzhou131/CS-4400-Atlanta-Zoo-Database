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
        MainWindow.resize(843, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 836, 543))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.homeButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout_2.addWidget(self.homeButton, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(156, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 2)
        self.exhibitHistoryLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.exhibitHistoryLabel.setFont(font)
        self.exhibitHistoryLabel.setObjectName("exhibitHistoryLabel")
        self.gridLayout_2.addWidget(self.exhibitHistoryLabel, 0, 4, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(265, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 7, 1, 2)
        self.label_title = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(652, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setMinimumSize(QtCore.QSize(71, 31))
        self.nameLabel.setMaximumSize(QtCore.QSize(71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 3)
        self.timeLabel = QtWidgets.QLabel(self.widget)
        self.timeLabel.setMinimumSize(QtCore.QSize(71, 31))
        self.timeLabel.setMaximumSize(QtCore.QSize(71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 0, 4, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(201, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 5, 1, 2)
        self.minLabel = QtWidgets.QLabel(self.widget)
        self.minLabel.setMinimumSize(QtCore.QSize(58, 31))
        self.minLabel.setMaximumSize(QtCore.QSize(58, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.minLabel.setFont(font)
        self.minLabel.setObjectName("minLabel")
        self.gridLayout.addWidget(self.minLabel, 1, 2, 1, 1)
        self.maxLabel = QtWidgets.QLabel(self.widget)
        self.maxLabel.setMinimumSize(QtCore.QSize(61, 31))
        self.maxLabel.setMaximumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.maxLabel.setFont(font)
        self.maxLabel.setObjectName("maxLabel")
        self.gridLayout.addWidget(self.maxLabel, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 4, 1, 2)
        self.dateTimeCheckBox = QtWidgets.QCheckBox(self.widget)
        self.dateTimeCheckBox.setMinimumSize(QtCore.QSize(98, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.dateTimeCheckBox.setFont(font)
        self.dateTimeCheckBox.setObjectName("dateTimeCheckBox")
        self.gridLayout.addWidget(self.dateTimeCheckBox, 1, 6, 1, 1)
        self.NoVLabel = QtWidgets.QLabel(self.widget)
        self.NoVLabel.setMinimumSize(QtCore.QSize(191, 31))
        self.NoVLabel.setMaximumSize(QtCore.QSize(191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.NoVLabel.setFont(font)
        self.NoVLabel.setObjectName("NoVLabel")
        self.gridLayout.addWidget(self.NoVLabel, 2, 0, 1, 2)
        self.numVisitsMinSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numVisitsMinSpinBox.setMinimumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.numVisitsMinSpinBox.setFont(font)
        self.numVisitsMinSpinBox.setObjectName("numVisitsMinSpinBox")
        self.gridLayout.addWidget(self.numVisitsMinSpinBox, 2, 2, 1, 1)
        self.numVisitsMaxSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numVisitsMaxSpinBox.setMinimumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.numVisitsMaxSpinBox.setFont(font)
        self.numVisitsMaxSpinBox.setObjectName("numVisitsMaxSpinBox")
        self.gridLayout.addWidget(self.numVisitsMaxSpinBox, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 8, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 0, 1, 5)
        self.searchPushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.searchPushButton.setFont(font)
        self.searchPushButton.setObjectName("searchPushButton")
        self.gridLayout_2.addWidget(self.searchPushButton, 4, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(315, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 4, 6, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 5, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_2.addWidget(self.tableWidget, 5, 1, 1, 7)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 5, 8, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.userDefinedInitialization()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExhibitHistory"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.exhibitHistoryLabel.setText(_translate("MainWindow", "Exhibit History"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.timeLabel.setText(_translate("MainWindow", "Time:"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.minLabel.setText(_translate("MainWindow", "Min"))
        self.maxLabel.setText(_translate("MainWindow", "Max"))
        self.dateTimeCheckBox.setText(_translate("MainWindow", "All Time"))
        self.NoVLabel.setText(_translate("MainWindow", "Number of Visits:"))
        self.searchPushButton.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Number of Visits"))


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
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

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

