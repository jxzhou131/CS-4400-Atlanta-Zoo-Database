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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 782, 508))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.HomePushButton = QtWidgets.QPushButton(self.widget)
        self.HomePushButton.setMinimumSize(QtCore.QSize(111, 49))
        self.HomePushButton.setMaximumSize(QtCore.QSize(111, 49))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.HomePushButton.setFont(font)
        self.HomePushButton.setObjectName("HomePushButton")
        self.gridLayout.addWidget(self.HomePushButton, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(344, 74))
        self.label.setMaximumSize(QtCore.QSize(344, 74))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 3, 2, 1)
        self.AtlantaZoo = QtWidgets.QLabel(self.widget)
        self.AtlantaZoo.setMinimumSize(QtCore.QSize(146, 41))
        self.AtlantaZoo.setMaximumSize(QtCore.QSize(146, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.AtlantaZoo.setFont(font)
        self.AtlantaZoo.setObjectName("AtlantaZoo")
        self.gridLayout.addWidget(self.AtlantaZoo, 2, 0, 2, 2)
        spacerItem1 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        self.StaffTable = QtWidgets.QTableWidget(self.widget)
        self.StaffTable.setMinimumSize(QtCore.QSize(577, 381))
        self.StaffTable.setMaximumSize(QtCore.QSize(577, 381))
        self.StaffTable.setObjectName("StaffTable")
        self.StaffTable.setColumnCount(3)
        self.StaffTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.StaffTable, 4, 1, 1, 4)
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
        self.AtlantaZoo.setText(_translate("staffViewShows", "Atlanta Zoo "))
        item = self.StaffTable.horizontalHeaderItem(0)
        item.setText(_translate("staffViewShows", "Name"))
        item = self.StaffTable.horizontalHeaderItem(1)
        item.setText(_translate("staffViewShows", "Time"))
        item = self.StaffTable.horizontalHeaderItem(2)
        item.setText(_translate("staffViewShows", "Exhibit"))


    def userDefinedInitialization(self):
        self.ShowDisplay()
        self.HomePushButton.clicked.connect(self.home)
        self.StaffTable.cellClicked.connect(self.highlightRow)
        header = self.StaffTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def highlightRow(self, row, column):
        # highlight the row selected
        self.StaffTable.selectRow(row)

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

