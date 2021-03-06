

from PyQt5 import QtCore, QtGui, QtWidgets
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import sys

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

app = QtWidgets.QApplication(sys.argv)
import util
class Ui_staffSearchAnimals(object):
    def setupUi(self, staffSearchAnimals):
        staffSearchAnimals.setObjectName("staffSearchAnimals")
        staffSearchAnimals.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(staffSearchAnimals)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 11, 781, 576))
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.HomePushButton = QtWidgets.QPushButton(self.widget)
        self.HomePushButton.setMinimumSize(QtCore.QSize(110, 47))
        self.HomePushButton.setMaximumSize(QtCore.QSize(110, 47))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.HomePushButton.setFont(font)
        self.HomePushButton.setObjectName("HomePushButton")
        self.gridLayout_6.addWidget(self.HomePushButton, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Max = QtWidgets.QLabel(self.widget)
        self.Max.setMinimumSize(QtCore.QSize(93, 28))
        self.Max.setMaximumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Max.setFont(font)
        self.Max.setObjectName("Max")
        self.gridLayout_3.addWidget(self.Max, 0, 2, 1, 1)
        self.Min = QtWidgets.QLabel(self.widget)
        self.Min.setMinimumSize(QtCore.QSize(94, 28))
        self.Min.setMaximumSize(QtCore.QSize(94, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Min.setFont(font)
        self.Min.setObjectName("Min")
        self.gridLayout_3.addWidget(self.Min, 0, 1, 1, 1)
        self.Age = QtWidgets.QLabel(self.widget)
        self.Age.setMinimumSize(QtCore.QSize(93, 29))
        self.Age.setMaximumSize(QtCore.QSize(93, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Age.setFont(font)
        self.Age.setObjectName("Age")
        self.gridLayout_3.addWidget(self.Age, 1, 0, 1, 1)
        self.MaxSpinBox = QtWidgets.QSpinBox(self.widget)
        self.MaxSpinBox.setMinimumSize(QtCore.QSize(93, 29))
        self.MaxSpinBox.setMaximumSize(QtCore.QSize(93, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.MaxSpinBox.setFont(font)
        self.MaxSpinBox.setMinimum(0)
        self.MaxSpinBox.setMaximum(8)
        self.MaxSpinBox.setProperty("value", 0)
        self.MaxSpinBox.setObjectName("MaxSpinBox")
        self.gridLayout_3.addWidget(self.MaxSpinBox, 1, 2, 1, 1)
        self.MinSpinBox = QtWidgets.QSpinBox(self.widget)
        self.MinSpinBox.setMinimumSize(QtCore.QSize(94, 29))
        self.MinSpinBox.setMaximumSize(QtCore.QSize(94, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.MinSpinBox.setFont(font)
        self.MinSpinBox.setMaximum(8)
        self.MinSpinBox.setObjectName("MinSpinBox")
        self.gridLayout_3.addWidget(self.MinSpinBox, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Type = QtWidgets.QLabel(self.widget)
        self.Type.setMinimumSize(QtCore.QSize(144, 28))
        self.Type.setMaximumSize(QtCore.QSize(144, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Type.setFont(font)
        self.Type.setObjectName("Type")
        self.gridLayout_4.addWidget(self.Type, 0, 0, 1, 1)
        self.TypeComboBox = QtWidgets.QComboBox(self.widget)
        self.TypeComboBox.setMinimumSize(QtCore.QSize(143, 28))
        self.TypeComboBox.setMaximumSize(QtCore.QSize(143, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TypeComboBox.setFont(font)
        self.TypeComboBox.setObjectName("TypeComboBox")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.TypeComboBox.addItem("")
        self.gridLayout_4.addWidget(self.TypeComboBox, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Exhibit = QtWidgets.QLabel(self.widget)
        self.Exhibit.setMinimumSize(QtCore.QSize(144, 28))
        self.Exhibit.setMaximumSize(QtCore.QSize(144, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Exhibit.setFont(font)
        self.Exhibit.setObjectName("Exhibit")
        self.gridLayout_2.addWidget(self.Exhibit, 0, 0, 1, 1)
        self.ExhibitComboBox = QtWidgets.QComboBox(self.widget)
        self.ExhibitComboBox.setMinimumSize(QtCore.QSize(143, 28))
        self.ExhibitComboBox.setMaximumSize(QtCore.QSize(143, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ExhibitComboBox.setFont(font)
        self.ExhibitComboBox.setObjectName("ExhibitComboBox")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.ExhibitComboBox.addItem("")
        self.gridLayout_2.addWidget(self.ExhibitComboBox, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 3, 1)
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
        self.gridLayout_6.addWidget(self.AtlantaZoo, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Name = QtWidgets.QLabel(self.widget)
        self.Name.setMinimumSize(QtCore.QSize(74, 29))
        self.Name.setMaximumSize(QtCore.QSize(74, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 0, 0, 1, 1)
        self.NameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.NameLineEdit.setMinimumSize(QtCore.QSize(249, 29))
        self.NameLineEdit.setMaximumSize(QtCore.QSize(249, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.NameLineEdit.setFont(font)
        self.NameLineEdit.setText("")
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.gridLayout.addWidget(self.NameLineEdit, 0, 1, 1, 1)
        self.Species = QtWidgets.QLabel(self.widget)
        self.Species.setMinimumSize(QtCore.QSize(74, 29))
        self.Species.setMaximumSize(QtCore.QSize(74, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Species.setFont(font)
        self.Species.setObjectName("Species")
        self.gridLayout.addWidget(self.Species, 1, 0, 1, 1)
        self.SpeciesLineEdit = QtWidgets.QLineEdit(self.widget)
        self.SpeciesLineEdit.setMinimumSize(QtCore.QSize(249, 29))
        self.SpeciesLineEdit.setMaximumSize(QtCore.QSize(249, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.SpeciesLineEdit.setFont(font)
        self.SpeciesLineEdit.setText("")
        self.SpeciesLineEdit.setObjectName("SpeciesLineEdit")
        self.gridLayout.addWidget(self.SpeciesLineEdit, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.SearchPushButton = QtWidgets.QPushButton(self.widget)
        self.SearchPushButton.setMinimumSize(QtCore.QSize(93, 33))
        self.SearchPushButton.setMaximumSize(QtCore.QSize(93, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SearchPushButton.setFont(font)
        self.SearchPushButton.setObjectName("SearchPushButton")
        self.gridLayout_6.addWidget(self.SearchPushButton, 2, 2, 1, 1)
        self.AnimalTable = QtWidgets.QTableWidget(self.widget)
        self.AnimalTable.setMinimumSize(QtCore.QSize(761, 281))
        self.AnimalTable.setMaximumSize(QtCore.QSize(761, 281))
        self.AnimalTable.setObjectName("AnimalTable")
        self.AnimalTable.setColumnCount(5)
        self.AnimalTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.AnimalTable.setHorizontalHeaderItem(4, item)
        self.gridLayout_6.addWidget(self.AnimalTable, 3, 0, 1, 3)
        staffSearchAnimals.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staffSearchAnimals)
        self.statusbar.setObjectName("statusbar")
        staffSearchAnimals.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(staffSearchAnimals)
        QtCore.QMetaObject.connectSlotsByName(staffSearchAnimals)

    def retranslateUi(self, staffSearchAnimals):
        _translate = QtCore.QCoreApplication.translate
        staffSearchAnimals.setWindowTitle(_translate("staffSearchAnimals", "Search Animals"))
        self.HomePushButton.setText(_translate("staffSearchAnimals", "Home"))
        self.Max.setText(_translate("staffSearchAnimals", "Max"))
        self.Min.setText(_translate("staffSearchAnimals", "Min"))
        self.Age.setText(_translate("staffSearchAnimals", "Age"))
        self.Type.setText(_translate("staffSearchAnimals", "Type"))
        self.TypeComboBox.setItemText(0, _translate("staffSearchAnimals", "All"))
        self.TypeComboBox.setItemText(1, _translate("staffSearchAnimals", "Fish"))
        self.TypeComboBox.setItemText(2, _translate("staffSearchAnimals", "Amphibian"))
        self.TypeComboBox.setItemText(3, _translate("staffSearchAnimals", "Mammal"))
        self.TypeComboBox.setItemText(4, _translate("staffSearchAnimals", "Bird"))
        self.Exhibit.setText(_translate("staffSearchAnimals", "Exhibit"))
        self.ExhibitComboBox.setItemText(0, _translate("staffSearchAnimals", "All"))
        self.ExhibitComboBox.setItemText(1, _translate("staffSearchAnimals", "Pacific"))
        self.ExhibitComboBox.setItemText(2, _translate("staffSearchAnimals", "Jungle"))
        self.ExhibitComboBox.setItemText(3, _translate("staffSearchAnimals", "Sahara"))
        self.ExhibitComboBox.setItemText(4, _translate("staffSearchAnimals", "Mountainous"))
        self.ExhibitComboBox.setItemText(5, _translate("staffSearchAnimals", "Birds"))
        self.AtlantaZoo.setText(_translate("staffSearchAnimals", "Atlanta Zoo "))
        self.Name.setText(_translate("staffSearchAnimals", "Name"))
        self.Species.setText(_translate("staffSearchAnimals", "Species"))
        self.SearchPushButton.setText(_translate("staffSearchAnimals", "Search"))
        item = self.AnimalTable.horizontalHeaderItem(0)
        item.setText(_translate("staffSearchAnimals", "Name"))
        item = self.AnimalTable.horizontalHeaderItem(1)
        item.setText(_translate("staffSearchAnimals", "Species"))
        item = self.AnimalTable.horizontalHeaderItem(2)
        item.setText(_translate("staffSearchAnimals", "Exhibit"))
        item = self.AnimalTable.horizontalHeaderItem(3)
        item.setText(_translate("staffSearchAnimals", "Age"))
        item = self.AnimalTable.horizontalHeaderItem(4)
        item.setText(_translate("staffSearchAnimals", "Type"))

    def userDefinedInitialization(self):
        self.currentOrder = 0
        self.SearchPushButton.clicked.connect(self.SearchAnimals)
        self.HomePushButton.clicked.connect(self.home)
        self.AnimalTable.cellClicked.connect(self.highlightRowOrToAnimal)
        self.MaxSpinBox.setMaximum(1000)
        self.MinSpinBox.setMaximum(1000)
        header = self.AnimalTable.horizontalHeader()
        header.sectionClicked.connect(self.SearchAnimals)
        self.SearchAnimals()

    def SearchAnimals(self, column = 0):
        Name = self.NameLineEdit.text()
        Species = self.SpeciesLineEdit.text()
        Exhibit = self.ExhibitComboBox.currentText()
        Type = self.TypeComboBox.currentText()
        MaxAge = self.MaxSpinBox.value()
        MinAge = self.MinSpinBox.value()

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

        print(record)
        self.AnimalTable.setRowCount(0)
        for row_number, row_data in enumerate(record):
            self.AnimalTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.AnimalTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    def highlightRowOrToAnimal(self,row, column):
        self.AnimalTable.selectRow(row)
        if (column == 0 ):
            Name = str(self.AnimalTable.item(row,column).text())
            Species = str(self.AnimalTable.item(row,column+1).text())
            __main__.arg = [("Name", Name, "str"), ("Species", Species, "str")]
            __main__.status = __main__.statusDef["Normal"]
            __main__.state = __main__.staffUIs["staffAnimalCare"]
            app.exit()


    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.staffUIs['staffFunctionality'] # Login Page
        app.exit()

def render():
    __main__.state = -10
    staffSearchAnimals = QtWidgets.QMainWindow()
    ui = Ui_staffSearchAnimals()
    ui.setupUi(staffSearchAnimals)
    staffSearchAnimals.show()
    app.exec_()
    # close the WINDOWS
    staffSearchAnimals.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffSearchAnimals = QtWidgets.QMainWindow()
    ui = Ui_staffSearchAnimals()
    ui.setupUi(staffSearchAnimals)
    staffSearchAnimals.show()
    app.exec_()
    staffSearchAnimals.close()
