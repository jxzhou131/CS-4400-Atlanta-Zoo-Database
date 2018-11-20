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

import sys
app = QtWidgets.QApplication(sys.argv)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(20, 10, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(40, 50, 91, 16))
        self.label_title.setObjectName("label_title")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(350, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(60, 120, 60, 16))
        self.label_name.setObjectName("label_name")
        self.comboBox_exb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_exb.setGeometry(QtCore.QRect(110, 160, 111, 41))
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.label_exb = QtWidgets.QLabel(self.centralwidget)
        self.label_exb.setGeometry(QtCore.QRect(60, 170, 60, 16))
        self.label_exb.setObjectName("label_exb")
        self.spinBox_age = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_age.setGeometry(QtCore.QRect(100, 290, 48, 24))
        self.spinBox_age.setObjectName("spinBox_age")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(60, 290, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(13)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")
        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setGeometry(QtCore.QRect(60, 210, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(13)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.comboBox_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type.setGeometry(QtCore.QRect(120, 210, 104, 26))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_type.setFont(font)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.label_species = QtWidgets.QLabel(self.centralwidget)
        self.label_species.setGeometry(QtCore.QRect(60, 250, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(13)
        self.label_species.setFont(font)
        self.label_species.setObjectName("label_species")
        self.lineEdit_species = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_species.setGeometry(QtCore.QRect(130, 250, 113, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_species.setFont(font)
        self.lineEdit_species.setObjectName("lineEdit_species")
        self.button_add_animal = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_animal.setGeometry(QtCore.QRect(450, 170, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_add_animal.setFont(font)
        self.button_add_animal.setObjectName("button_add_animal")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 120, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_header.setText(_translate("MainWindow", "Add Animal"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Birds"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit"))
        self.label_age.setText(_translate("MainWindow", "Age:"))
        self.label_type.setText(_translate("MainWindow", "Type:"))
        self.comboBox_type.setItemText(0, _translate("MainWindow", "mammal"))
        self.comboBox_type.setItemText(1, _translate("MainWindow", "bird"))
        self.comboBox_type.setItemText(2, _translate("MainWindow", "amphibian"))
        self.comboBox_type.setItemText(3, _translate("MainWindow", "reptile"))
        self.comboBox_type.setItemText(4, _translate("MainWindow", "fish"))
        self.comboBox_type.setItemText(5, _translate("MainWindow", "invertebrate"))
        self.label_species.setText(_translate("MainWindow", "Species:"))
        self.button_add_animal.setText(_translate("MainWindow", "Add Animal"))

    def Home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.initialUIs['loginPage'] # Login Page
        app.exit()

    def userDefinedInitialization(self):
        # self.addAnimalsButton.clicked.connect(self.addAnimals)
        self.viewShowsButton.clicked.connect(self.viewShows)
        self.viewStaffButton.clicked.connect(self.viewStaff)
        self.viewVisitorsButton.clicked.connect(self.viewVisitors)
        self.viewAnimalsButton.clicked.connect(self.viewAnimals)
        self.addShowButton.clicked.connect(self.addShows)
        self.logOutButton.clicked.connect(self.logout)

    


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

