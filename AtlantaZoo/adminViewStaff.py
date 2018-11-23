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

class Ui_adminViewStaff(object):
    # load all the data in the table view load all if no username
    # is given if username is given then only load that particular
    # staff
    def loadData(self):
        connection_object = connection_pool.get_connection()
        username = self.username.text();
        print(username)
        query = ""
        if(username ==""):
            query = "select Username, Email from USER where UserType ='Staff'"
        else :
            query = "select Username, Email from USER where Username = \'"+username+"\';"

        cursor = connection_object.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self.userList.setRowCount(0)
        for row, row_data in enumerate(result):
            self.userList.insertRow(row)
            for column ,data in enumerate(row_data):
                self.userList.setItem(row, column, QtWidgets.QTableWidgetItem(str (data)))
        cursor.close()
        connection_object.close()

    # this function allow the admin to select the rows and delete those staff
    def deleteData(self):
        index_list = []                                                          
        for model_index in self.userList.selectionModel().selectedRows():       
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
            self.userList.removeRow(index.row())
        cursor.close()
        connection_object.close()

    # linked the home button to take the admin back to the home page
    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality']
        app.exit()
        
    # initialize the delete function to delete selected row from the table
    def userDefinedInitialization(self):
        self.pushButton.clicked.connect(self.loadData)
        self.deleteStaffMemberButton.clicked.connect(self.deleteData)
        self.homeButton.clicked.connect(self.home)

    def setupUi(self, adminViewStaff):
        adminViewStaff.setObjectName("adminViewStaff")
        adminViewStaff.resize(665, 465)
        self.centralwidget = QtWidgets.QWidget(adminViewStaff)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 0, 4, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 337, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 4, 3, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.splitter)
        self.username.setObjectName("username")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.splitter, 3, 1, 1, 2)
        self.userList = QtWidgets.QTableWidget(self.centralwidget)
        self.userList.setMinimumSize(QtCore.QSize(300, 150))
        self.userList.setObjectName("userList")
        self.userList.setColumnCount(2)
        self.userList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userList.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.userList, 4, 1, 1, 3)
        self.deleteStaffMemberButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteStaffMemberButton.setFont(font)
        self.deleteStaffMemberButton.setObjectName("deleteStaffMemberButton")
        self.gridLayout.addWidget(self.deleteStaffMemberButton, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 3, 1, 2)
        adminViewStaff.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminViewStaff)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 20))
        self.menubar.setObjectName("menubar")
        adminViewStaff.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminViewStaff)
        self.statusbar.setObjectName("statusbar")
        adminViewStaff.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(adminViewStaff)
        QtCore.QMetaObject.connectSlotsByName(adminViewStaff)

    def retranslateUi(self, adminViewStaff):
        _translate = QtCore.QCoreApplication.translate
        adminViewStaff.setWindowTitle(_translate("adminViewStaff", "MainWindow"))
        self.label.setText(_translate("adminViewStaff", "Atlanta Zoo"))
        self.label_2.setText(_translate("adminViewStaff", "View Staff"))
        self.homeButton.setText(_translate("adminViewStaff", "Home"))
        self.label_3.setText(_translate("adminViewStaff", "Username"))
        self.pushButton.setText(_translate("adminViewStaff", "Search"))
        item = self.userList.horizontalHeaderItem(0)
        item.setText(_translate("adminViewStaff", "Username"))
        item = self.userList.horizontalHeaderItem(1)
        item.setText(_translate("adminViewStaff", "email"))
        self.deleteStaffMemberButton.setText(_translate("adminViewStaff", "Delete Staff Member"))

def render():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
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

