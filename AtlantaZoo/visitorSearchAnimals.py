from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__
import sys
app = QtWidgets.QApplication(sys.argv)

import util


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Homebutton.setGeometry(QtCore.QRect(20, 30, 113, 32))
        self.Homebutton.setObjectName("Homebutton")
        self.Searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Searchbutton.setGeometry(QtCore.QRect(280, 230, 113, 32))
        self.Searchbutton.setObjectName("Searchbutton")
        self.Heading_animal = QtWidgets.QLabel(self.centralwidget)
        self.Heading_animal.setGeometry(QtCore.QRect(270, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_animal.setFont(font)
        self.Heading_animal.setObjectName("Heading_animal")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(120, 110, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_species = QtWidgets.QLabel(self.centralwidget)
        self.label_species.setGeometry(QtCore.QRect(120, 160, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_species.setFont(font)
        self.label_species.setObjectName("label_species")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(400, 150, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")
        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setGeometry(QtCore.QRect(400, 190, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.label_exhibit = QtWidgets.QLabel(self.centralwidget)
        self.label_exhibit.setGeometry(QtCore.QRect(400, 90, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_exhibit.setFont(font)
        self.label_exhibit.setObjectName("label_exhibit")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(190, 110, 113, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_species = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_species.setGeometry(QtCore.QRect(190, 160, 113, 21))
        self.lineEdit_species.setObjectName("lineEdit_species")
        self.ExhibitCombo = QtWidgets.QComboBox(self.centralwidget)
        self.ExhibitCombo.setGeometry(QtCore.QRect(470, 90, 104, 26))
        self.ExhibitCombo.setObjectName("ExhibitCombo")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.ExhibitCombo.addItem("")
        self.TypeCombo = QtWidgets.QComboBox(self.centralwidget)
        self.TypeCombo.setGeometry(QtCore.QRect(460, 190, 104, 26))
        self.TypeCombo.setObjectName("TypeCombo")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.TypeCombo.addItem("")
        self.label_minage = QtWidgets.QLabel(self.centralwidget)
        self.label_minage.setGeometry(QtCore.QRect(460, 130, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_minage.setFont(font)
        self.label_minage.setObjectName("label_minage")
        self.label_maxage = QtWidgets.QLabel(self.centralwidget)
        self.label_maxage.setGeometry(QtCore.QRect(510, 130, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_maxage.setFont(font)
        self.label_maxage.setObjectName("label_maxage")
        self.spinBox_min = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_min.setGeometry(QtCore.QRect(450, 150, 48, 24))
        self.spinBox_min.setObjectName("spinBox_min")
        self.spinBox_max = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_max.setGeometry(QtCore.QRect(510, 150, 48, 24))
        self.spinBox_max.setObjectName("spinBox_max")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 280, 501, 192))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
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
        self.Searchbutton.setText(_translate("MainWindow", "Search"))
        self.Heading_animal.setText(_translate("MainWindow", "Animals"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_species.setText(_translate("MainWindow", "Species:"))
        self.label_age.setText(_translate("MainWindow", "Age:"))
        self.label_type.setText(_translate("MainWindow", "Type:"))
        self.label_exhibit.setText(_translate("MainWindow", "Exhibit:"))
        self.ExhibitCombo.setItemText(0, _translate("MainWindow", "All"))
        self.ExhibitCombo.setItemText(1, _translate("MainWindow", "Pacific"))
        self.ExhibitCombo.setItemText(2, _translate("MainWindow", "Jungle"))
        self.ExhibitCombo.setItemText(3, _translate("MainWindow", "Sahara"))
        self.ExhibitCombo.setItemText(4, _translate("MainWindow", "Mountainous"))
        self.ExhibitCombo.setItemText(5, _translate("MainWindow", "Birds"))
        self.TypeCombo.setItemText(0, _translate("MainWindow", "All"))
        self.TypeCombo.setItemText(1, _translate("MainWindow", "Mammal"))
        self.TypeCombo.setItemText(2, _translate("MainWindow", "Bird"))
        self.TypeCombo.setItemText(3, _translate("MainWindow", "Amphibian"))
        self.TypeCombo.setItemText(4, _translate("MainWindow", "Reptile"))
        self.TypeCombo.setItemText(5, _translate("MainWindow", "Fish"))
        self.TypeCombo.setItemText(6, _translate("MainWindow", "Invertebrate"))
        self.label_minage.setText(_translate("MainWindow", "Min"))
        self.label_maxage.setText(_translate("MainWindow", "Max"))
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
        self.Searchbutton.clicked.connect(self.searchAnimal)
        self.Homebutton.clicked.connect(self.home)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
    
    
    def searchAnimal(self):
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

        cmd1= "SELECT Name, Species, Exhibit, Type, Age FROM ANIMAL"
        
        cmd1 = util.addWHERE(cmd1, listTuple)


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



