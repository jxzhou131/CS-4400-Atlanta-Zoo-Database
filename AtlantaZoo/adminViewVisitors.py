# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminViewVisitor.ui'
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
class Ui_adminViewVisitors(object):
    def setupUi(self, adminViewVisitors):
        adminViewVisitors.setObjectName("adminViewVisitors")
        adminViewVisitors.resize(680, 465)
        self.centralwidget = QtWidgets.QWidget(adminViewVisitors)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, -1, 668, 427))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.homeButton = QtWidgets.QPushButton(self.widget)
        self.homeButton.setMinimumSize(QtCore.QSize(117, 49))
        self.homeButton.setMaximumSize(QtCore.QSize(117, 49))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(194, 47))
        self.label_2.setMaximumSize(QtCore.QSize(194, 47))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(224, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 3)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(103, 24))
        self.label.setMaximumSize(QtCore.QSize(103, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(526, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 9)
        spacerItem3 = QtWidgets.QSpacerItem(154, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(90, 24))
        self.label_3.setMaximumSize(QtCore.QSize(90, 24))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 2)
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setMinimumSize(QtCore.QSize(224, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 2, 5, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(146, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 9, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(247, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 5)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setMinimumSize(QtCore.QSize(93, 33))
        self.searchButton.setMaximumSize(QtCore.QSize(93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 3, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 6, 1, 5)
        spacerItem7 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        self.visitorList = QtWidgets.QTableWidget(self.widget)
        self.visitorList.setMinimumSize(QtCore.QSize(454, 171))
        self.visitorList.setObjectName("visitorList")
        self.visitorList.setColumnCount(2)
        self.visitorList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.visitorList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitorList.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.visitorList, 4, 1, 1, 9)
        spacerItem8 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 10, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(251, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 5)
        self.deleteVisitorButton = QtWidgets.QPushButton(self.widget)
        self.deleteVisitorButton.setMinimumSize(QtCore.QSize(130, 33))
        self.deleteVisitorButton.setMaximumSize(QtCore.QSize(130, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.deleteVisitorButton.setFont(font)
        self.deleteVisitorButton.setObjectName("deleteVisitorButton")
        self.gridLayout.addWidget(self.deleteVisitorButton, 5, 5, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(253, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 7, 1, 4)
        adminViewVisitors.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminViewVisitors)
        self.statusbar.setObjectName("statusbar")
        adminViewVisitors.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(adminViewVisitors)
        QtCore.QMetaObject.connectSlotsByName(adminViewVisitors)

    def retranslateUi(self, adminViewVisitors):
        _translate = QtCore.QCoreApplication.translate
        adminViewVisitors.setWindowTitle(_translate("adminViewVisitors", "MainWindow"))
        self.homeButton.setText(_translate("adminViewVisitors", "Home"))
        self.label_2.setText(_translate("adminViewVisitors", "View Visitor"))
        self.label.setText(_translate("adminViewVisitors", "Atlanta Zoo"))
        self.label_3.setText(_translate("adminViewVisitors", "Username"))
        self.searchButton.setText(_translate("adminViewVisitors", "Search"))
        item = self.visitorList.horizontalHeaderItem(0)
        item.setText(_translate("adminViewVisitors", "Username"))
        item = self.visitorList.horizontalHeaderItem(1)
        item.setText(_translate("adminViewVisitors", "Email"))
        self.deleteVisitorButton.setText(_translate("adminViewVisitors", "Delete Visitor"))



    # initialize the delete function to delete selected row from the table
    def userDefinedInitialization(self):
        self.searchButton.clicked.connect(self.loadData)
        self.deleteVisitorButton.clicked.connect(self.deleteData)
        self.homeButton.clicked.connect(self.home)
        self.visitorList.cellClicked.connect(self.highlightRow)

    def highlightRow(self, row, column):
        # highlight the row selected
        self.visitorList.selectRow(row)


    # load all the data in the table view load all if no username
    # is given if username is given then only load that particular
    # visitor
    def loadData(self):
        connection_object = connection_pool.get_connection()
        username = self.username.text();
        print(username)
        query = ""
        if(username ==""):
            query = "select Username, Email from USER where UserType ='Visitor'"
        else :
            query = "select Username, Email from USER where Username = \'"+username+"\';"

        cursor = connection_object.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self.visitorList.setRowCount(0)
        for row, row_data in enumerate(result):
            self.visitorList.insertRow(row)
            for column ,data in enumerate(row_data):
                self.visitorList.setItem(row, column, QtWidgets.QTableWidgetItem(str (data)))
        cursor.close()
        connection_object.close()


    # this function allow the admin to select the rows and delete that visitor
    def deleteData(self):
        index_list = []                                                          
        for model_index in self.visitorList.selectionModel().selectedRows():    
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
            self.visitorList.removeRow(index.row())
        cursor.close()
        connection_object.close()


    # linked the home button to take the admin back to the home page
    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality']
        app.exit()


def render():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    __main__.state = -10
    adminViewVisitors = QtWidgets.QMainWindow()
    ui = Ui_adminViewVisitors()
    ui.setupUi(adminViewVisitors)
    adminViewVisitors.show()
    app.exec_()
    adminViewVisitors.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminViewVisitor = QtWidgets.QMainWindow()
    ui = Ui_adminViewVisitor()
    ui.setupUi(adminViewVisitor)
    adminViewVisitor.show()
    sys.exit(app.exec_())

