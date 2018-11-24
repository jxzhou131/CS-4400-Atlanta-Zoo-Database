# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminAddAnimals.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__

import mysql.connector

import sys
app = QtWidgets.QApplication(sys.argv)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(8, 15, 679, 413))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_home = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.gridLayout_2.addWidget(self.button_home, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label_header = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.gridLayout_2.addWidget(self.label_header, 0, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(211, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 5, 1, 1)
        self.label_title = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 3, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_exb = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_exb.setFont(font)
        self.label_exb.setObjectName("label_exb")
        self.gridLayout.addWidget(self.label_exb, 1, 0, 1, 1)
        self.comboBox_exb = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.comboBox_exb.setFont(font)
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.gridLayout.addWidget(self.comboBox_exb, 1, 1, 1, 1)
        self.label_type = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.gridLayout.addWidget(self.label_type, 2, 0, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.comboBox_type.setFont(font)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.gridLayout.addWidget(self.comboBox_type, 2, 1, 1, 1)
        self.label_species = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_species.setFont(font)
        self.label_species.setObjectName("label_species")
        self.gridLayout.addWidget(self.label_species, 3, 0, 1, 1)
        self.lineEdit_species = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_species.setFont(font)
        self.lineEdit_species.setObjectName("lineEdit_species")
        self.gridLayout.addWidget(self.lineEdit_species, 3, 1, 1, 1)
        self.label_age = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")
        self.gridLayout.addWidget(self.label_age, 4, 0, 1, 1)
        self.spinBox_age = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.spinBox_age.setFont(font)
        self.spinBox_age.setMaximum(1000)
        self.spinBox_age.setObjectName("spinBox_age")
        self.gridLayout.addWidget(self.spinBox_age, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 3, 3)
        spacerItem3 = QtWidgets.QSpacerItem(232, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 4, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 4, 1, 2)
        self.button_add_animal = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.button_add_animal.setFont(font)
        self.button_add_animal.setObjectName("button_add_animal")
        self.gridLayout_2.addWidget(self.button_add_animal, 3, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.userDefinedInitialization()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.label_header.setText(_translate("MainWindow", "Add Animal"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit:"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Birds"))
        self.label_type.setText(_translate("MainWindow", "Type:"))
        self.comboBox_type.setItemText(0, _translate("MainWindow", "Mammal"))
        self.comboBox_type.setItemText(1, _translate("MainWindow", "Bird"))
        self.comboBox_type.setItemText(2, _translate("MainWindow", "Amphibian"))
        self.comboBox_type.setItemText(3, _translate("MainWindow", "Reptile"))
        self.comboBox_type.setItemText(4, _translate("MainWindow", "Fish"))
        self.comboBox_type.setItemText(5, _translate("MainWindow", "Invertebrate"))
        self.label_species.setText(_translate("MainWindow", "Species:"))
        self.label_age.setText(_translate("MainWindow", "Age:"))
        self.button_add_animal.setText(_translate("MainWindow", "Add Animal"))

    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality'] # administratorFunctionality Page
        app.exit()

    def userDefinedInitialization(self):
        self.button_home.clicked.connect(self.home)
        self.button_add_animal.clicked.connect(self.addAnimals)
        self.spinBox_age.setMaximum(1000)
        # self.viewStaffButton.clicked.connect(self.viewStaff)
        # self.viewVisitorsButton.clicked.connect(self.viewVisitors)
        # self.viewAnimalsButton.clicked.connect(self.viewAnimals)
        # self.addShowButton.clicked.connect(self.addShows)
        # self.logOutButton.clicked.connect(self.logout)

    def addAnimals(self):
        Name = self.lineEdit.text()
        Species = self.lineEdit_species.text()
        Type = self.comboBox_type.currentText()
        Age = self.spinBox_age.value()
        Exhibit = self.comboBox_exb.currentText()

        if Name.lstrip().rstrip() == "" or Species.lstrip().rstrip() == "" or Type.lstrip().rstrip() == "" or Age < 0 or Exhibit.lstrip().rstrip() == "":
            self.InformationNotComplete()
            return

        else:
            cmd = "INSERT INTO ANIMAL VALUES (\'" + Name + "\', \'" + Species + "\', \'" + Type+"\', "+ str(Age) + ", \'" + Exhibit + "\');"
            # obtain the connection_object
            connection_object = connection_pool.get_connection()
            # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
            if connection_object.is_connected():
                db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
            # get cursor
            cursor = connection_object.cursor()
            # use cursor to execute sql command
            try:
                cursor.execute(cmd)
                connection_object.commit()
                self.Insert_successful()
            except mysql.connector.IntegrityError as err:
                self.IntegrityError()
                print("Error: {}", format(err))

            # close the cursor and connection
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")


    def InformationNotComplete(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("Information is not complete")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_() 

    def IntegrityError(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("Integrity Error")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()   

    def Insert_successful(self):
        d = QtWidgets.QDialog()
        d.setMinimumSize(400, 50)
        b1= QtWidgets.QPushButton("close",d)
        b1.clicked.connect(lambda : d.close())
        b1.move(50,50)
        d.setWindowTitle("Insertion Successful")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()        

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
    sys.exit(app.exec_())

