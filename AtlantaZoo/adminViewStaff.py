# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminViewStaff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import sys
app = QtWidgets.QApplication(sys.argv)

import re

headerDict = {
    0: "Username",
    1: "Email"
}

orderDict = {
    0: "ASC",
    1: "DESC"
}

class Ui_adminViewStaff(object):
    def setupUi(self, adminViewStaff):
        adminViewStaff.setObjectName("adminViewStaff")
        adminViewStaff.resize(701, 469)
        self.centralwidget = QtWidgets.QWidget(adminViewStaff)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(2, 2, 682, 426))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.homeButton = QtWidgets.QPushButton(self.widget)
        self.homeButton.setMinimumSize(QtCore.QSize(93, 37))
        self.homeButton.setMaximumSize(QtCore.QSize(93, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(114, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(225, 42))
        self.label_2.setMaximumSize(QtCore.QSize(229, 42))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(215, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 3)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(133, 23))
        self.label.setMaximumSize(QtCore.QSize(133, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(526, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 9)
        spacerItem3 = QtWidgets.QSpacerItem(143, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(89, 29))
        self.label_3.setMaximumSize(QtCore.QSize(89, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 2)
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setMinimumSize(QtCore.QSize(237, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 5, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(147, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 9, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(266, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 6)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setMinimumSize(QtCore.QSize(93, 32))
        self.searchButton.setMaximumSize(QtCore.QSize(93, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 3, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(239, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 7, 1, 4)
        spacerItem7 = QtWidgets.QSpacerItem(102, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 2)
        self.staffList = QtWidgets.QTableWidget(self.widget)
        self.staffList.setMinimumSize(QtCore.QSize(429, 192))
        self.staffList.setObjectName("staffList")
        self.staffList.setColumnCount(2)
        self.staffList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.staffList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.staffList.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.staffList, 4, 2, 1, 8)
        spacerItem8 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 10, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 4)
        self.deleteStaffMemberButton = QtWidgets.QPushButton(self.widget)
        self.deleteStaffMemberButton.setMinimumSize(QtCore.QSize(225, 32))
        self.deleteStaffMemberButton.setMaximumSize(QtCore.QSize(229, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.deleteStaffMemberButton.setFont(font)
        self.deleteStaffMemberButton.setObjectName("deleteStaffMemberButton")
        self.gridLayout.addWidget(self.deleteStaffMemberButton, 5, 4, 1, 4)
        spacerItem10 = QtWidgets.QSpacerItem(202, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 8, 1, 3)
        adminViewStaff.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminViewStaff)
        self.statusbar.setObjectName("statusbar")
        adminViewStaff.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(adminViewStaff)
        QtCore.QMetaObject.connectSlotsByName(adminViewStaff)

    def retranslateUi(self, adminViewStaff):
        _translate = QtCore.QCoreApplication.translate
        adminViewStaff.setWindowTitle(_translate("adminViewStaff", "MainWindow"))
        self.homeButton.setText(_translate("adminViewStaff", "Home"))
        self.label_2.setText(_translate("adminViewStaff", "View Staff"))
        self.label.setText(_translate("adminViewStaff", "Atlanta Zoo"))
        self.label_3.setText(_translate("adminViewStaff", "Username"))
        self.searchButton.setText(_translate("adminViewStaff", "Search"))
        item = self.staffList.horizontalHeaderItem(0)
        item.setText(_translate("adminViewStaff", "Username"))
        item = self.staffList.horizontalHeaderItem(1)
        item.setText(_translate("adminViewStaff", "Email"))
        self.deleteStaffMemberButton.setText(_translate("adminViewStaff", "Delete Staff Member"))



    # initialize the delete function to delete selected row from the table
    def userDefinedInitialization(self):
        self.currentOrder = 0
        self.searchButton.clicked.connect(self.loadData)
        self.deleteStaffMemberButton.clicked.connect(self.deleteData)
        self.homeButton.clicked.connect(self.home)
        self.staffList.cellClicked.connect(self.highlightRow)
        header = self.staffList.horizontalHeader()
        header.sectionClicked.connect(self.loadData)

    def highlightRow(self, row, column):
        # highlight the row selected
        self.staffList.selectRow(row)




    # load all the data in the table view load all if no username
    # is given if username is given then only load that particular
    # staff
    def loadData(self, column = 0):
        connection_object = connection_pool.get_connection()
        username = self.username.text();
        query = ""
        if(username ==""):
            query = "select Username, Email from USER where UserType ='Staff'"
        else :
            query = "select Username, Email from USER where Username = \'"+username+"\'"

        query += " order by " + headerDict[column] + " " + orderDict[self.currentOrder] + ";"
        if(self.currentOrder == 0):
            self.currentOrder = 1
        else: 
            self.currentOrder = 0
        cursor = connection_object.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self.staffList.setRowCount(0)
        for row, row_data in enumerate(result):
            self.staffList.insertRow(row)
            for column ,data in enumerate(row_data):
                self.staffList.setItem(row, column, QtWidgets.QTableWidgetItem(str (data)))
        cursor.close()
        connection_object.close()

    # this function allow the admin to select the rows and delete those staff
    def deleteData(self):
        index_list = []                                                          
        for model_index in self.staffList.selectionModel().selectedRows():       
            index = QtCore.QPersistentModelIndex(model_index)         
            index_list.append(index)                                             

        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        for index in index_list:                                     
            row = index.row()
            name = index.sibling(row, 0).data()
            email = index.sibling(row, 1).data()
            query = "delete from USER WHERE Username =\'" + name + "\'and Email =\'"+email+"\';"
            cursor.execute(query)
            connection_object.commit()
            self.staffList.removeRow(index.row())
        cursor.close()
        connection_object.close()


    # linked the home button to take the admin back to the home page
    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality']
        app.exit()
    

def render():
    __main__.state = -10
    adminViewStaff = QtWidgets.QMainWindow()
    ui = Ui_adminViewStaff()
    ui.setupUi(adminViewStaff)
    adminViewStaff.show()
    app.exec_()
    adminViewStaff.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminViewStaff = QtWidgets.QMainWindow()
    ui = Ui_adminViewStaff()
    ui.setupUi(adminViewStaff)
    adminViewStaff.show()
    sys.exit(app.exec_())

