from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__
import sys
app = QtWidgets.QApplication(sys.argv)

import util
headerDict = {
    0: "Name",
    1: "Species",
    2: "Exhibit",
    3: "Type",
    4: "Age"
}

orderDict = {
    0: "ASC",
    1: "DESC"
}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(4, 4, 832, 539))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Homebutton = QtWidgets.QPushButton(self.widget)
        self.Homebutton.setMinimumSize(QtCore.QSize(117, 51))
        self.Homebutton.setMaximumSize(QtCore.QSize(117, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Homebutton.setFont(font)
        self.Homebutton.setObjectName("Homebutton")
        self.gridLayout_3.addWidget(self.Homebutton, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(166, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 3)
        self.Heading_animal = QtWidgets.QLabel(self.widget)
        self.Heading_animal.setMinimumSize(QtCore.QSize(137, 36))
        self.Heading_animal.setMaximumSize(QtCore.QSize(137, 36))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_animal.setFont(font)
        self.Heading_animal.setObjectName("Heading_animal")
        self.gridLayout_3.addWidget(self.Heading_animal, 0, 5, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(327, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 7, 1, 3)
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setMinimumSize(QtCore.QSize(172, 23))
        self.label_title.setMaximumSize(QtCore.QSize(172, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_3.addWidget(self.label_title, 1, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(651, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 3, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setMinimumSize(QtCore.QSize(63, 22))
        self.label_name.setMaximumSize(QtCore.QSize(63, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(167, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_species = QtWidgets.QLabel(self.widget)
        self.label_species.setMinimumSize(QtCore.QSize(81, 27))
        self.label_species.setMaximumSize(QtCore.QSize(81, 27))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_species.setFont(font)
        self.label_species.setObjectName("label_species")
        self.gridLayout_2.addWidget(self.label_species, 1, 0, 1, 1)
        self.lineEdit_species = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_species.setMinimumSize(QtCore.QSize(166, 27))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_species.setFont(font)
        self.lineEdit_species.setObjectName("lineEdit_species")
        self.gridLayout_2.addWidget(self.lineEdit_species, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 1, 1, 5)
        spacerItem4 = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 6, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_exhibit = QtWidgets.QLabel(self.widget)
        self.label_exhibit.setMinimumSize(QtCore.QSize(68, 28))
        self.label_exhibit.setMaximumSize(QtCore.QSize(68, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_exhibit.setFont(font)
        self.label_exhibit.setObjectName("label_exhibit")
        self.gridLayout.addWidget(self.label_exhibit, 0, 0, 1, 1)
        self.ExhibitCombo = QtWidgets.QComboBox(self.widget)
        self.ExhibitCombo.setMinimumSize(QtCore.QSize(168, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.ExhibitCombo.setFont(font)
        self.ExhibitCombo.setObjectName("ExhibitCombo")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.gridLayout.addWidget(self.ExhibitCombo, 0, 1, 1, 2)
        self.label_minage = QtWidgets.QLabel(self.widget)
        self.label_minage.setMinimumSize(QtCore.QSize(60, 21))
        self.label_minage.setMaximumSize(QtCore.QSize(60, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_minage.setFont(font)
        self.label_minage.setObjectName("label_minage")
        self.gridLayout.addWidget(self.label_minage, 1, 1, 1, 1)
        self.label_maxage = QtWidgets.QLabel(self.widget)
        self.label_maxage.setMinimumSize(QtCore.QSize(60, 21))
        self.label_maxage.setMaximumSize(QtCore.QSize(60, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_maxage.setFont(font)
        self.label_maxage.setObjectName("label_maxage")
        self.gridLayout.addWidget(self.label_maxage, 1, 2, 1, 1)
        self.label_age = QtWidgets.QLabel(self.widget)
        self.label_age.setMinimumSize(QtCore.QSize(64, 29))
        self.label_age.setMaximumSize(QtCore.QSize(64, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")
        self.gridLayout.addWidget(self.label_age, 2, 0, 1, 1)
        self.spinBox_min = QtWidgets.QSpinBox(self.widget)
        self.spinBox_min.setMinimumSize(QtCore.QSize(73, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.spinBox_min.setFont(font)
        self.spinBox_min.setObjectName("spinBox_min")
        self.gridLayout.addWidget(self.spinBox_min, 2, 1, 1, 1)
        self.spinBox_max = QtWidgets.QSpinBox(self.widget)
        self.spinBox_max.setMinimumSize(QtCore.QSize(74, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.spinBox_max.setFont(font)
        self.spinBox_max.setObjectName("spinBox_max")
        self.gridLayout.addWidget(self.spinBox_max, 2, 2, 1, 1)
        self.label_type = QtWidgets.QLabel(self.widget)
        self.label_type.setMinimumSize(QtCore.QSize(60, 21))
        self.label_type.setMaximumSize(QtCore.QSize(60, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.gridLayout.addWidget(self.label_type, 3, 0, 1, 1)
        self.TypeCombo = QtWidgets.QComboBox(self.widget)
        self.TypeCombo.setMinimumSize(QtCore.QSize(144, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.TypeCombo.setFont(font)
        self.TypeCombo.setObjectName("TypeCombo")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.gridLayout.addWidget(self.TypeCombo, 3, 1, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 8, 2, 1)
        spacerItem5 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 2, 9, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 3, 0, 1, 3)
        self.Searchbutton = QtWidgets.QPushButton(self.widget)
        self.Searchbutton.setMinimumSize(QtCore.QSize(116, 38))
        self.Searchbutton.setMaximumSize(QtCore.QSize(116, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.Searchbutton.setFont(font)
        self.Searchbutton.setObjectName("Searchbutton")
        self.gridLayout_3.addWidget(self.Searchbutton, 3, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 3, 4, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMinimumSize(QtCore.QSize(683, 258))
        self.tableWidget.setMaximumSize(QtCore.QSize(683, 258))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_3.addWidget(self.tableWidget, 4, 1, 1, 8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 4, 9, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 5, 5, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.userDefinedInitialisation()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Homebutton.setText(_translate("MainWindow", "HOME"))
        self.Heading_animal.setText(_translate("MainWindow", "Animals"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_species.setText(_translate("MainWindow", "Species:"))
        self.label_exhibit.setText(_translate("MainWindow", "Exhibit:"))
        self.ExhibitCombo.setItemText(0, _translate("MainWindow", "All"))
        self.ExhibitCombo.setItemText(1, _translate("MainWindow", "Pacific"))
        self.ExhibitCombo.setItemText(2, _translate("MainWindow", "Jungle"))
        self.ExhibitCombo.setItemText(3, _translate("MainWindow", "Sahara"))
        self.ExhibitCombo.setItemText(4, _translate("MainWindow", "Mountainous"))
        self.ExhibitCombo.setItemText(5, _translate("MainWindow", "Birds"))
        self.label_minage.setText(_translate("MainWindow", "Min"))
        self.label_maxage.setText(_translate("MainWindow", "Max"))
        self.label_age.setText(_translate("MainWindow", "Age:"))
        self.label_type.setText(_translate("MainWindow", "Type:"))
        self.TypeCombo.setItemText(0, _translate("MainWindow", "All"))
        self.TypeCombo.setItemText(1, _translate("MainWindow", "Mammal"))
        self.TypeCombo.setItemText(2, _translate("MainWindow", "Bird"))
        self.TypeCombo.setItemText(3, _translate("MainWindow", "Amphibian"))
        self.TypeCombo.setItemText(4, _translate("MainWindow", "Reptile"))
        self.TypeCombo.setItemText(5, _translate("MainWindow", "Fish"))
        self.TypeCombo.setItemText(6, _translate("MainWindow", "Invertebrate"))
        self.Searchbutton.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Species"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Exhibit"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Age"))

    def userDefinedInitialisation(self):
        self.currentOrder = 0
        self.Searchbutton.clicked.connect(self.searchAnimal)
        self.Homebutton.clicked.connect(self.home)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
        header = self.tableWidget.horizontalHeader()
        header.sectionClicked.connect(self.searchAnimal)
        # header = self.tableWidget.horizontalHeader()
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    
    def searchAnimal(self, column = 0):
        Name = self.lineEdit_name.text()
        Species = self.lineEdit_species.text()
        Exhibit = self.ExhibitCombo.currentText()
        Type = self.TypeCombo.currentText()
        MaxAge = self.spinBox_max.value()
        MinAge = self.spinBox_min.value()
        
        if(Exhibit=="All"):
            Exhibit=""
        if(Type=="All"):
            Type=""
        if(MaxAge==0):
            MaxAge=''
        if(MinAge==0):
            MinAge=''
        
        listTuple = [("Name", Name, "str"), ("Species", Species, "str"),("Exhibit",Exhibit, "str"),("Type", Type, "str"),("MinAge", MinAge, "int"),("MaxAge", MaxAge, "int")]

        cmd1= "SELECT Name, Species, Exhibit, Type, Age FROM ANIMAL "
        
        cmd1 = util.addWHERE(cmd1, listTuple)

        cmd1 += " order by " + headerDict[column] + " " + orderDict[self.currentOrder] + ";"
        if(self.currentOrder == 0):
            self.currentOrder = 1
        else: 
            self.currentOrder = 0

        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
        
        cursor = connection_object.cursor()
        cursor.execute(cmd1)
        record = cursor.fetchall()
        
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(record):
            # insert a new blank row
            # in other words, expand the table by inserting a new row
            self.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                # IMPORTANT
                # first you must determine in which column does the DateTime attribute occur in your
                # query
                cellContent = None
                if(cellContent is None):
                    cellContent = str(data)
                self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(cellContent))



        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")



    def highlightRowOrToExhibit(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
        # Enter IF statement if the selected column is the exhibit column
        if(column == 2):
            # retrieve the content in the cell
            Name = str(self.tableWidget.item(row,column).text())
            # store the information into the __main__.arg
            # the information is later passed to the exhibitDetails page
            __main__.arg = [("Name", Name)]
            __main__.status = __main__.statusDef["Normal"]
            __main__.state = __main__.visitorUIs["exhibitDetails"]
            app.exit()
            # FOR DEBUGGING PURPOSE
            print("row, column, ExhibitName")
            print(str(row) + "," + str(column) + "," + Name)



    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality'] # visitor
        app.exit()


def render():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    # close the WINDOWS
    MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    table = MyTable(data, 5, 5)
    table.show()
    sys.exit(app.exec_())



