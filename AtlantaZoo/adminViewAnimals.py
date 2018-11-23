# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminViewAnimals.ui'
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
import util

class Ui_adminViewAnimals(object):
    # load all the data in the table view load all animals if nothing
    # is given else  then only load that particular
    # animal all five field must be provided
    def loadData(self):
        connection_object = connection_pool.get_connection()

        Name = self.name.text()
        Species = self.species.text()
        Exhibit = self.exhibit.currentText()
        Type = self.type.currentText()
        MaxAge = self.maxAge.value()
        MinAge = self.minAge.value()
        if (Exhibit == "All"):
            Exhibit = ""
        if (Type == "All"):
            Type = ""
        if (MaxAge == 0 and MinAge == 0):
            MaxAge = ''
            MinAge = ''

        listTuple = [("Name", Name, "str"), ("Species", Species, "str"),("Exhibit",Exhibit, "str"),("Type", Type, "str"),("minAge", MinAge, "int"),("maxAge", MaxAge, "int")]
        cmd1 = "SELECT Name, Species, Type,Age, Exhibit FROM ANIMAL"
        cmd1 = util.addWHERE(cmd1,listTuple)     
        cursor = connection_object.cursor()
        cursor.execute(cmd1)
        result = cursor.fetchall()
        self.listOfAnimals.setRowCount(0)
        for row, row_data in enumerate(result):
            self.listOfAnimals.insertRow(row)
            for column ,data in enumerate(row_data):
                self.listOfAnimals.setItem(row, column, QtWidgets.QTableWidgetItem(str (data)))
        cursor.close()
        connection_object.close()

    # this function allow the admin to select the rows and delete that animal
    def deleteData(self):
        index_list = []                                                          
        for model_index in self.listOfAnimals.selectionModel().selectedRows():       
            index = QtCore.QPersistentModelIndex(model_index)         
            index_list.append(index)                                             

        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        for index in index_list:                                  
            row = index.row()
            name = index.sibling(row, 0).data()
            species = index.sibling(row, 1).data()
            atype = index.sibling(row, 2).data()
            age = index.sibling(row, 3).data()
            exhibit = index.sibling(row, 4).data()
            query = "delete from ANIMAL WHERE Name =\'" + name + "\'and Species =\'"+species+"\';"
            cursor.execute(query)
            connection_object.commit()
            self.listOfAnimals.removeRow(index.row())
        cursor.close()
        connection_object.close()

    # linked the home button to take the admin back to the home page
    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality']
        app.exit()

    # initialize the delete function to delete selected row from the table
    def userDefinedInitialization(self):
        self.Search.clicked.connect(self.loadData)
        self.RemoveAnimals.clicked.connect(self.deleteData)
        self.Home.clicked.connect(self.home)



    def setupUi(self, adminViewAnimals):
        adminViewAnimals.setObjectName("adminViewAnimals")
        adminViewAnimals.resize(728, 500)
        self.centralwidget = QtWidgets.QWidget(adminViewAnimals)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(94, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(147, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 8, 1, 2)
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_2 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.exhibit = QtWidgets.QComboBox(self.splitter_5)
        self.exhibit.setObjectName("exhibit")

        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")

        self.gridLayout.addWidget(self.splitter_5, 0, 10, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 14, 1, 3)
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Home.setFont(font)
        self.Home.setObjectName("Home")
        self.gridLayout.addWidget(self.Home, 0, 17, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 172, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 6, 6, 1)
        spacerItem4 = QtWidgets.QSpacerItem(232, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 7, 3, 5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 12, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 13, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 12, 2, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 13, 2, 2)
        spacerItem7 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 15, 3, 3)
        spacerItem8 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 8, 2, 3)
        spacerItem9 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.name = QtWidgets.QLineEdit(self.splitter_3)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.splitter_3, 4, 2, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 5, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.minAge = QtWidgets.QSpinBox(self.splitter_2)
        self.minAge.setObjectName("minAge")
        self.maxAge = QtWidgets.QSpinBox(self.splitter_2)
        self.maxAge.setObjectName("maxAge")
        self.gridLayout.addWidget(self.splitter_2, 4, 11, 1, 4)
        spacerItem11 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 4, 16, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 5, 0, 1, 2)
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_4 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.species = QtWidgets.QLineEdit(self.splitter_4)
        self.species.setObjectName("species")
        self.gridLayout.addWidget(self.splitter_4, 5, 2, 1, 3)
        spacerItem13 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 5, 5, 1, 1)
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Search.setFont(font)
        self.Search.setObjectName("Search")
        self.gridLayout.addWidget(self.Search, 6, 2, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(126, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 6, 9, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.type = QtWidgets.QComboBox(self.splitter)
        self.type.setObjectName("type")

        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")



        self.gridLayout.addWidget(self.splitter, 6, 11, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 6, 16, 1, 2)
        spacerItem16 = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 7, 0, 1, 3)
        self.listOfAnimals = QtWidgets.QTableWidget(self.centralwidget)
        self.listOfAnimals.setObjectName("listOfAnimals")
        self.listOfAnimals.setColumnCount(5)
        self.listOfAnimals.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listOfAnimals.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfAnimals.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfAnimals.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfAnimals.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listOfAnimals.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.listOfAnimals, 7, 3, 1, 10)
        spacerItem17 = QtWidgets.QSpacerItem(147, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 7, 13, 1, 5)
        self.RemoveAnimals = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RemoveAnimals.setFont(font)
        self.RemoveAnimals.setObjectName("RemoveAnimals")
        self.gridLayout.addWidget(self.RemoveAnimals, 8, 6, 1, 3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 9, 6, 1, 1)
        adminViewAnimals.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminViewAnimals)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 20))
        self.menubar.setObjectName("menubar")
        adminViewAnimals.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminViewAnimals)
        self.statusbar.setObjectName("statusbar")
        adminViewAnimals.setStatusBar(self.statusbar)
        
        self.retranslateUi(adminViewAnimals)
        self.userDefinedInitialization()
        QtCore.QMetaObject.connectSlotsByName(adminViewAnimals)

    def retranslateUi(self, adminViewAnimals):
        _translate = QtCore.QCoreApplication.translate
        adminViewAnimals.setWindowTitle(_translate("adminViewAnimals", "MainWindow"))
        self.label.setText(_translate("adminViewAnimals", "Atlanta Zoo"))
        self.label_7.setText(_translate("adminViewAnimals", "Animals"))
        self.label_2.setText(_translate("adminViewAnimals", "Exhibit"))
        self.Home.setText(_translate("adminViewAnimals", "Home"))
        self.label_8.setText(_translate("adminViewAnimals", "min"))
        self.label_9.setText(_translate("adminViewAnimals", "max"))
        self.label_3.setText(_translate("adminViewAnimals", "Name"))
        self.label_5.setText(_translate("adminViewAnimals", "Age"))
        self.label_4.setText(_translate("adminViewAnimals", "Species"))
        self.Search.setText(_translate("adminViewAnimals", "Search"))
        self.label_6.setText(_translate("adminViewAnimals", "Type"))

        self.exhibit.setItemText(0, _translate("staffSearchAnimals", "All"))
        self.exhibit.setItemText(1, _translate("staffSearchAnimals", "Pacific"))
        self.exhibit.setItemText(2, _translate("staffSearchAnimals", "Jungle"))
        self.exhibit.setItemText(3, _translate("staffSearchAnimals", "Sahara"))
        self.exhibit.setItemText(4, _translate("staffSearchAnimals", "Mountainous"))
        self.exhibit.setItemText(5, _translate("staffSearchAnimals", "Birds"))

        self.type.setItemText(0, _translate("staffSearchAnimals", "All"))
        self.type.setItemText(1, _translate("staffSearchAnimals", "Fish"))
        self.type.setItemText(2, _translate("staffSearchAnimals", "Amphibian"))
        self.type.setItemText(3, _translate("staffSearchAnimals", "Mammal"))
        self.type.setItemText(4, _translate("staffSearchAnimals", "Bird"))

        item = self.listOfAnimals.horizontalHeaderItem(0)
        item.setText(_translate("adminViewAnimals", "Name"))
        item = self.listOfAnimals.horizontalHeaderItem(1)
        item.setText(_translate("adminViewAnimals", "Species"))
        item = self.listOfAnimals.horizontalHeaderItem(2)
        item.setText(_translate("adminViewAnimals", "Type"))
        item = self.listOfAnimals.horizontalHeaderItem(3)
        item.setText(_translate("adminViewAnimals", "Age"))
        item = self.listOfAnimals.horizontalHeaderItem(4)
        item.setText(_translate("adminViewAnimals", "Exhibit"))
        self.RemoveAnimals.setText(_translate("adminViewAnimals", "Remove Animals"))

        

def render():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    __main__.state = -10
    adminViewAnimals = QtWidgets.QMainWindow()
    ui = Ui_adminViewAnimals()
    ui.setupUi(adminViewAnimals)
    adminViewAnimals.show()
    app.exec_()
    adminViewAnimals.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminViewAnimals = QtWidgets.QMainWindow()
    ui = Ui_adminViewAnimals()
    ui.setupUi(adminViewAnimals)
    adminViewAnimals.show()
    sys.exit(app.exec_())

