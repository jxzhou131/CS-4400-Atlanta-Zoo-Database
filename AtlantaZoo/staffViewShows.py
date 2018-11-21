# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffViewShows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__
import util
import time

import sys
app = QtWidgets.QApplication(sys.argv)

class Ui_staffViewShows(object):
    def setupUi(self, staffViewShows):
        staffViewShows.setObjectName("staffViewShows")
        staffViewShows.resize(800, 604)
        self.centralwidget = QtWidgets.QWidget(staffViewShows)
        self.centralwidget.setObjectName("centralwidget")
        self.HomePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomePushButton.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.HomePushButton.setObjectName("HomePushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 501, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.StaffTable = QtWidgets.QTableWidget(self.centralwidget)
        self.StaffTable.setGeometry(QtCore.QRect(150, 120, 511, 311))
        self.StaffTable.setObjectName("StaffTable")
        self.StaffTable.setColumnCount(3)
        self.StaffTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(2, item)
        self.ShowDisplay()
        staffViewShows.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staffViewShows)
        self.statusbar.setObjectName("statusbar")
        staffViewShows.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(staffViewShows)
        QtCore.QMetaObject.connectSlotsByName(staffViewShows)
        
    def retranslateUi(self, staffViewShows):
        _translate = QtCore.QCoreApplication.translate
        staffViewShows.setWindowTitle(_translate("staffViewShows", "View Staff Show"))
        self.HomePushButton.setText(_translate("staffViewShows", "Home"))
        self.label.setText(_translate("staffViewShows", " Staff - Show History"))
        item = self.StaffTable.horizontalHeaderItem(0)
        item.setText(_translate("staffViewShows", "Name"))
        item = self.StaffTable.horizontalHeaderItem(1)
        item.setText(_translate("staffViewShows", "Time"))
        item = self.StaffTable.horizontalHeaderItem(2)
        item.setText(_translate("staffViewShows", "Exhibit"))

    def userDefinedInitialization(self):
        self.HomePushButton.clicked.connect(self.home)

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.staffUIs['staffFunctionality'] # Login Page
        app.exit()

    def ShowDisplay(self):
        loginIdentity = __main__.loginIdentity[0][0]
        query = "SELECT Name, DateTime, Location FROM SHOWS WHERE Host = \'" + loginIdentity + "\';"
        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self.StaffTable.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.StaffTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                DATETIMECOLUMN = 1
                cellContent = None
                if(column_number == DATETIMECOLUMN):
                    cellContent = data.strftime("%m/%d/%Y %I:%M:%S %p")
                if(cellContent is None):
                    cellContent = str(data)
                self.StaffTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(cellContent)))

        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

            
def render():
    __main__.state = -10
    staffViewShows = QtWidgets.QMainWindow()
    ui = Ui_staffViewShows()
    ui.setupUi(staffViewShows)
    staffViewShows.show()
    app.exec_()
    # close the WINDOWS
    staffViewShows.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffViewShows = QtWidgets.QMainWindow()
    ui = Ui_staffViewShows()
    ui.setupUi(staffViewShows)
    staffViewShows.show()
    app.exec_()
    #close the WINDOWS
    staffViewShows.close()

