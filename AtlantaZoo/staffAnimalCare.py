# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffAnimalCare.ui'
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
# WINDOWS VARIABLE
# staffAnimalCare = None

class Ui_staffAnimalCare(object):
    def setupUi(self, staffAnimalCare):
        staffAnimalCare.setObjectName("staffAnimalCare")
        staffAnimalCare.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(staffAnimalCare)
        self.centralwidget.setObjectName("centralwidget")
        self.HomePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomePushButton.setGeometry(QtCore.QRect(0, 0, 95, 43))
        self.HomePushButton.setMinimumSize(QtCore.QSize(95, 43))
        self.HomePushButton.setMaximumSize(QtCore.QSize(95, 43))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.HomePushButton.setFont(font)
        self.HomePushButton.setObjectName("HomePushButton")
        self.AnimalDetail = QtWidgets.QLabel(self.centralwidget)
        self.AnimalDetail.setGeometry(QtCore.QRect(270, 30, 221, 41))
        self.AnimalDetail.setMinimumSize(QtCore.QSize(221, 41))
        self.AnimalDetail.setMaximumSize(QtCore.QSize(221, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.AnimalDetail.setFont(font)
        self.AnimalDetail.setObjectName("AnimalDetail")
        self.AtlantaZoo = QtWidgets.QLabel(self.centralwidget)
        self.AtlantaZoo.setGeometry(QtCore.QRect(40, 80, 271, 31))
        self.AtlantaZoo.setMinimumSize(QtCore.QSize(271, 31))
        self.AtlantaZoo.setMaximumSize(QtCore.QSize(271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.AtlantaZoo.setFont(font)
        self.AtlantaZoo.setObjectName("AtlantaZoo")
        self.NoteTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NoteTextEdit.setGeometry(QtCore.QRect(40, 250, 536, 121))
        self.NoteTextEdit.setMinimumSize(QtCore.QSize(536, 121))
        self.NoteTextEdit.setMaximumSize(QtCore.QSize(536, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.NoteTextEdit.setFont(font)
        self.NoteTextEdit.setObjectName("NoteTextEdit")
        self.LogNotesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogNotesPushButton.setGeometry(QtCore.QRect(600, 280, 151, 51))
        self.LogNotesPushButton.setMinimumSize(QtCore.QSize(151, 51))
        self.LogNotesPushButton.setMaximumSize(QtCore.QSize(151, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.LogNotesPushButton.setFont(font)
        self.LogNotesPushButton.setObjectName("LogNotesPushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 380, 721, 192))
        self.tableWidget.setMinimumSize(QtCore.QSize(721, 192))
        self.tableWidget.setMaximumSize(QtCore.QSize(721, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.NameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameLineEdit.setGeometry(QtCore.QRect(117, 130, 119, 34))
        self.NameLineEdit.setMinimumSize(QtCore.QSize(119, 34))
        self.NameLineEdit.setMaximumSize(QtCore.QSize(119, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.NameLineEdit.setFont(font)
        self.NameLineEdit.setReadOnly(True)
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.ExhibitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ExhibitLineEdit.setGeometry(QtCore.QRect(118, 192, 119, 34))
        self.ExhibitLineEdit.setMinimumSize(QtCore.QSize(119, 34))
        self.ExhibitLineEdit.setMaximumSize(QtCore.QSize(119, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.ExhibitLineEdit.setFont(font)
        self.ExhibitLineEdit.setReadOnly(True)
        self.ExhibitLineEdit.setObjectName("ExhibitLineEdit")
        self.SpeciesLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SpeciesLineEdit.setGeometry(QtCore.QRect(327, 131, 157, 38))
        self.SpeciesLineEdit.setMinimumSize(QtCore.QSize(157, 38))
        self.SpeciesLineEdit.setMaximumSize(QtCore.QSize(157, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.SpeciesLineEdit.setFont(font)
        self.SpeciesLineEdit.setReadOnly(True)
        self.SpeciesLineEdit.setObjectName("SpeciesLineEdit")
        self.TypeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TypeLineEdit.setGeometry(QtCore.QRect(328, 189, 157, 38))
        self.TypeLineEdit.setMinimumSize(QtCore.QSize(157, 38))
        self.TypeLineEdit.setMaximumSize(QtCore.QSize(157, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.TypeLineEdit.setFont(font)
        self.TypeLineEdit.setReadOnly(True)
        self.TypeLineEdit.setObjectName("TypeLineEdit")
        self.AgeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AgeLineEdit.setGeometry(QtCore.QRect(550, 129, 157, 38))
        self.AgeLineEdit.setMinimumSize(QtCore.QSize(157, 38))
        self.AgeLineEdit.setMaximumSize(QtCore.QSize(157, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.AgeLineEdit.setFont(font)
        self.AgeLineEdit.setReadOnly(True)
        self.AgeLineEdit.setObjectName("AgeLineEdit")
        self.Species = QtWidgets.QLabel(self.centralwidget)
        self.Species.setGeometry(QtCore.QRect(239, 119, 119, 56))
        self.Species.setMinimumSize(QtCore.QSize(119, 56))
        self.Species.setMaximumSize(QtCore.QSize(119, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Species.setFont(font)
        self.Species.setObjectName("Species")
        self.Type = QtWidgets.QLabel(self.centralwidget)
        self.Type.setGeometry(QtCore.QRect(265, 177, 119, 56))
        self.Type.setMinimumSize(QtCore.QSize(119, 56))
        self.Type.setMaximumSize(QtCore.QSize(119, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Type.setFont(font)
        self.Type.setObjectName("Type")
        self.Age = QtWidgets.QLabel(self.centralwidget)
        self.Age.setGeometry(QtCore.QRect(494, 127, 76, 39))
        self.Age.setMinimumSize(QtCore.QSize(76, 39))
        self.Age.setMaximumSize(QtCore.QSize(76, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Age.setFont(font)
        self.Age.setObjectName("Age")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(41, 121, 99, 56))
        self.Name.setMinimumSize(QtCore.QSize(99, 56))
        self.Name.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.Exhibit = QtWidgets.QLabel(self.centralwidget)
        self.Exhibit.setGeometry(QtCore.QRect(41, 184, 99, 56))
        self.Exhibit.setMinimumSize(QtCore.QSize(99, 56))
        self.Exhibit.setMaximumSize(QtCore.QSize(99, 56))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Exhibit.setFont(font)
        self.Exhibit.setObjectName("Exhibit")
        staffAnimalCare.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staffAnimalCare)
        self.statusbar.setObjectName("statusbar")
        staffAnimalCare.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(staffAnimalCare)
        QtCore.QMetaObject.connectSlotsByName(staffAnimalCare)

    def retranslateUi(self, staffAnimalCare):
        _translate = QtCore.QCoreApplication.translate
        staffAnimalCare.setWindowTitle(_translate("staffAnimalCare", "MainWindow"))
        self.HomePushButton.setText(_translate("staffAnimalCare", "Home"))
        self.AnimalDetail.setText(_translate("staffAnimalCare", "Animal Detail"))
        self.AtlantaZoo.setText(_translate("staffAnimalCare", "Atlanta Zoo"))
        self.LogNotesPushButton.setText(_translate("staffAnimalCare", "Log Notes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("staffAnimalCare", "Staff Member"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("staffAnimalCare", "Note"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("staffAnimalCare", "Time"))
        self.Species.setText(_translate("staffAnimalCare", "Species:"))
        self.Type.setText(_translate("staffAnimalCare", "Type:"))
        self.Age.setText(_translate("staffAnimalCare", "Age:"))
        self.Name.setText(_translate("staffAnimalCare", "Name:"))
        self.Exhibit.setText(_translate("staffAnimalCare", "Exhibit:"))


    def userDefinedInitialization(self):
        self.HomePushButton.clicked.connect(self.home)
        self.loadAnimalDetails()
        self.LogNotesPushButton.clicked.connect(self.logNote)
        self.preloadTable()
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 200)
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.NoteTextEdit.textChanged.connect(self.limitCharacter)

    def limitCharacter(self):
        maxChar = 200
        Text = str(self.NoteTextEdit.toPlainText())
        if(len(Text) > maxChar):
            Text = self.NoteTextEdit.toPlainText()
            Text = Text[:maxChar]
            self.NoteTextEdit.setPlainText(Text)
            cursor = self.NoteTextEdit.textCursor()
            cursor.setPosition(maxChar)
            self.NoteTextEdit.setTextCursor(cursor)

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality']
        app.exit()

    def preloadTable(self):
        # construct the querycommand to retrieve logged notes regarding to the animal
        cmd1 = "SELECT Staff, Text, DateTime FROM NOTE "
        AnimalName = __main__.arg[0][1]
        AnimalSpecies = __main__.arg[1][1]
        listTuple = [("AnimalName", AnimalName, "str"), ("AnimalSpecies", AnimalSpecies, "str")]
        cmd1 = util.addWHERE(cmd1, listTuple) + ";"

        # for DEBUGGING
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
                    DATETIMECOLUMN = 2
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


# SELECT Staff, Text, DateTime
# FROM Note
# WHERE AnimalName = 'Goldy' AND AnimalSpecies = 'Goldfish'

    def loadAnimalDetails(self):
        # construct the query command to retrieve information about the animal
        cmd1 = "SELECT * FROM ANIMAL "
        cmd1 = util.addWHERE(cmd1, __main__.arg) + " ; "

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

            # Update all the labels in the UI
            self.NameLineEdit.setText(str(record[0][0]))
            self.SpeciesLineEdit.setText(str(record[0][1]))
            self.TypeLineEdit.setText(str(record[0][2]))
            self.AgeLineEdit.setText((str(record[0][3])) + " Months")
            self.ExhibitLineEdit.setText(str(record[0][4]))

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        # close the cursor and connection
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")


# INSERT INTO NOTE(Staff,AnimalName, AnimalSpecies, DateTime,Text)
# VALUES ('martha_johnson', 'Goldy', 'Goldfish', STR_TO_DATE('10/6/2018 9:00:00 AM','%m/%d/%Y %r'), 'Need more water')
    def logNote(self):
        Staff = __main__.loginIdentity[0][0]
        AnimalName = __main__.arg[0][1]
        AnimalSpecies = __main__.arg[1][1]
        DateTime = str(time.strftime("%m/%d/%Y %I:%M:%S %p"))
        Text = str(self.NoteTextEdit.toPlainText())


        print("Note to be Logged")
        print(Text)
        listTuple = [("Staff", Staff, "str"), ("AnimalName", AnimalName, "str"), ("AnimalSpecies", AnimalSpecies, "str") \
                    , ("DateTime", DateTime, "datetime"), ("Text", Text, "str")]

        # construct the INSERT command
        cmd1 = "INSERT INTO NOTE VALUES(\'" + Staff +"\' , \'" + AnimalName + "\', \'" + AnimalSpecies + "\' , STR_TO_DATE(\'" \
                + DateTime + "\' , \' %m/%d/%Y %r \'), \'" + Text + "\' )"
        
        # for DEBUGGING
        print("cmd1")
        print(cmd1)

        # construct the querycommand to retrieve logged notes regarding to the animal
        cmd2 = "SELECT Staff, Text, DateTime FROM NOTE "
        AnimalName = __main__.arg[0][1]
        AnimalSpecies = __main__.arg[1][1]
        listTuple = [("AnimalName", AnimalName, "str"), ("AnimalSpecies", AnimalSpecies, "str")]
        cmd2 = util.addWHERE(cmd2, listTuple) + ";"        

        # for DEBUGGING
        print("cmd2")
        print(cmd2)

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
            # commit your transaction
            connection_object.commit()
            print("Insert Successfully")
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))
        #########################################################################################
        ########## Query and update the table ##############
        try:
            # use cursor to execute sql command
            cursor.execute(cmd2)
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
                    DATETIMECOLUMN = 2
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
    staffAnimalCare = QtWidgets.QMainWindow()
    ui = Ui_staffAnimalCare()
    ui.setupUi(staffAnimalCare)
    staffAnimalCare.show()
    app.exec_()
    # close the staffAnimalCare window
    staffAnimalCare.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffAnimalCare = QtWidgets.QMainWindow()
    ui = Ui_staffAnimalCare()
    ui.setupUi(staffAnimalCare)
    staffAnimalCare.show()
    sys.exit(app.exec_())

