# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorsearchAnimals.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Homebutton.setGeometry(QtCore.QRect(20, 30, 113, 32))
        self.Homebutton.setObjectName("Homebutton")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(120, 290, 411, 192))
        self.tableView.setShowGrid(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.Searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Searchbutton.setGeometry(QtCore.QRect(260, 240, 113, 32))
        self.Searchbutton.setObjectName("Searchbutton")
        self.Heading_animal = QtWidgets.QLabel(self.centralwidget)
        self.Heading_animal.setGeometry(QtCore.QRect(270, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_animal.setFont(font)
        self.Heading_animal.setObjectName("Heading_animal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 110, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 90, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 190, 104, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
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
        self.Homebutton.setText(_translate("MainWindow", "HOME"))
        self.Searchbutton.setText(_translate("MainWindow", "Search"))
        self.Heading_animal.setText(_translate("MainWindow", "Animals"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_species.setText(_translate("MainWindow", "Species:"))
        self.label_age.setText(_translate("MainWindow", "Age:"))
        self.label_type.setText(_translate("MainWindow", "Type:"))
        self.label_exhibit.setText(_translate("MainWindow", "Exhibit:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "mammal"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "bird"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "amphibian"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "reptile"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "fish"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "invertebrate"))
        self.label_minage.setText(_translate("MainWindow", "Min"))
        self.label_maxage.setText(_translate("MainWindow", "Max"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

