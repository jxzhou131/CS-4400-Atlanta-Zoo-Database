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

headerDict = {
    0: "Name",
    1: "Species",
    2: "Exhibit",
    3: "Age",
    4: "Type"
}

orderDict = {
    0: "ASC",
    1: "DESC"
}
class Ui_adminViewAnimals(object):
    def setupUi(self, adminViewAnimals):
        adminViewAnimals.setObjectName("adminViewAnimals")
        adminViewAnimals.resize(1169, 649)
        self.centralwidget = QtWidgets.QWidget(adminViewAnimals)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 5, 1155, 614))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Home = QtWidgets.QPushButton(self.layoutWidget)
        self.Home.setMaximumSize(QtCore.QSize(101, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Home.setFont(font)
        self.Home.setObjectName("Home")
        self.gridLayout_3.addWidget(self.Home, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(121, 34, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 5, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(309, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 7, 1, 5)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(564, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 3, 1, 9)
        spacerItem3 = QtWidgets.QSpacerItem(51, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(90, 23))
        self.label_3.setMaximumSize(QtCore.QSize(90, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(88, 23))
        self.label_4.setMaximumSize(QtCore.QSize(88, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.species = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.species.setFont(font)
        self.species.setObjectName("species")
        self.gridLayout.addWidget(self.species, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 1, 1, 6)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(65, 28))
        self.label_2.setMaximumSize(QtCore.QSize(65, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.exhibit = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.exhibit.setFont(font)
        self.exhibit.setObjectName("exhibit")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.exhibit.addItem("")
        self.gridLayout_2.addWidget(self.exhibit, 0, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(55, 23))
        self.label_5.setMaximumSize(QtCore.QSize(55, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.minAge = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.minAge.setFont(font)
        self.minAge.setObjectName("minAge")
        self.gridLayout_2.addWidget(self.minAge, 2, 1, 1, 1)
        self.maxAge = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.maxAge.setFont(font)
        self.maxAge.setObjectName("maxAge")
        self.gridLayout_2.addWidget(self.maxAge, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(57, 23))
        self.label_6.setMaximumSize(QtCore.QSize(57, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.type = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.gridLayout_2.addWidget(self.type, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 8, 3, 3)
        self.Search = QtWidgets.QPushButton(self.layoutWidget)
        self.Search.setMinimumSize(QtCore.QSize(95, 31))
        self.Search.setMaximumSize(QtCore.QSize(95, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.Search.setFont(font)
        self.Search.setObjectName("Search")
        self.gridLayout_3.addWidget(self.Search, 3, 1, 2, 3)
        spacerItem4 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 3, 11, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(52, 26, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 4, 4, 1, 4)
        spacerItem7 = QtWidgets.QSpacerItem(72, 17, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 5, 0, 1, 2)
        self.listOfAnimals = QtWidgets.QTableWidget(self.layoutWidget)
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
        self.gridLayout_3.addWidget(self.listOfAnimals, 5, 2, 2, 8)
        spacerItem8 = QtWidgets.QSpacerItem(74, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 6, 10, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 7, 0, 1, 6)
        self.RemoveAnimals = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.RemoveAnimals.setFont(font)
        self.RemoveAnimals.setObjectName("RemoveAnimals")
        self.gridLayout_3.addWidget(self.RemoveAnimals, 7, 6, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(286, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 7, 9, 1, 3)
        adminViewAnimals.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminViewAnimals)
        self.statusbar.setObjectName("statusbar")
        adminViewAnimals.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(adminViewAnimals)
        QtCore.QMetaObject.connectSlotsByName(adminViewAnimals)

    def retranslateUi(self, adminViewAnimals):
        _translate = QtCore.QCoreApplication.translate
        adminViewAnimals.setWindowTitle(_translate("adminViewAnimals", "MainWindow"))
        self.Home.setText(_translate("adminViewAnimals", "Home"))
        self.label_7.setText(_translate("adminViewAnimals", "Animals"))
        self.label.setText(_translate("adminViewAnimals", "Atlanta Zoo"))
        self.label_3.setText(_translate("adminViewAnimals", "Name:"))
        self.label_4.setText(_translate("adminViewAnimals", "Species:"))
        self.label_2.setText(_translate("adminViewAnimals", "Exhibit:"))
        self.exhibit.setItemText(0, _translate("adminViewAnimals", "All"))
        self.exhibit.setItemText(1, _translate("adminViewAnimals", "Pacific"))
        self.exhibit.setItemText(2, _translate("adminViewAnimals", "Birds"))
        self.exhibit.setItemText(3, _translate("adminViewAnimals", "Sahara"))
        self.exhibit.setItemText(4, _translate("adminViewAnimals", "Jungle"))
        self.exhibit.setItemText(5, _translate("adminViewAnimals", "Mountainous"))
        self.label_8.setText(_translate("adminViewAnimals", "Min"))
        self.label_9.setText(_translate("adminViewAnimals", "Max"))
        self.label_5.setText(_translate("adminViewAnimals", "Age:"))
        self.label_6.setText(_translate("adminViewAnimals", "Type:"))
        self.type.setItemText(0, _translate("adminViewAnimals", "All"))
        self.type.setItemText(1, _translate("adminViewAnimals", "Mammal"))
        self.type.setItemText(2, _translate("adminViewAnimals", "Bird"))
        self.type.setItemText(3, _translate("adminViewAnimals", "Amphibian"))
        self.type.setItemText(4, _translate("adminViewAnimals", "Reptile"))
        self.type.setItemText(5, _translate("adminViewAnimals", "Fish"))
        self.type.setItemText(6, _translate("adminViewAnimals", "Invertebrate"))
        self.Search.setText(_translate("adminViewAnimals", "Search"))
        item = self.listOfAnimals.horizontalHeaderItem(0)
        item.setText(_translate("adminViewAnimals", "Name"))
        item = self.listOfAnimals.horizontalHeaderItem(1)
        item.setText(_translate("adminViewAnimals", "Species"))
        item = self.listOfAnimals.horizontalHeaderItem(2)
        item.setText(_translate("adminViewAnimals", "Exhibit"))
        item = self.listOfAnimals.horizontalHeaderItem(3)
        item.setText(_translate("adminViewAnimals", "Age"))
        item = self.listOfAnimals.horizontalHeaderItem(4)
        item.setText(_translate("adminViewAnimals", "Type"))
        self.RemoveAnimals.setText(_translate("adminViewAnimals", "Remove Animals"))


    # linked the home button to take the admin back to the home page
    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality']
        app.exit()

    # initialize the delete function to delete selected row from the table
    def userDefinedInitialization(self):
        self.currentOrder = 0
        self.Search.clicked.connect(self.loadData)
        self.RemoveAnimals.clicked.connect(self.deleteData)
        self.Home.clicked.connect(self.home)
        self.maxAge.setMaximum(1000)
        self.minAge.setMaximum(1000)
        self.listOfAnimals.cellClicked.connect(self.highlightRow)
        header = self.listOfAnimals.horizontalHeader()
        header.sectionClicked.connect(self.loadData)

    def highlightRow(self, row, column):
        # highlight the row selected
        self.listOfAnimals.selectRow(row)

    # load all the data in the table view load all animals if nothing
    # is given else  then only load that particular
    # animal all five field must be provided
    def loadData(self, column = 0):
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

        listTuple = [("Name", Name, "str"), ("Species", Species, "str"),("Exhibit",Exhibit, "str"),("Type", Type, "str"),("MinAge", MinAge, "int"),("MaxAge", MaxAge, "int")]
        cmd1 = "SELECT Name, Species, Exhibit,Age, Type FROM ANIMAL"
        cmd1 = util.addWHERE(cmd1,listTuple)
        cmd1 += " order by " + headerDict[column] + " " + orderDict[self.currentOrder] +";"
        if(self.currentOrder == 0):
            self.currentOrder = 1
        else: 
            self.currentOrder = 0     
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

