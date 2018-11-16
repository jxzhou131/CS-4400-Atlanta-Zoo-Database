# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorSearchShow.ui'
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
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(70, 150, 60, 16))
        self.label_name.setObjectName("label_name")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(10, 20, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.button_rmv_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_rmv_show.setGeometry(QtCore.QRect(330, 480, 113, 32))
        self.button_rmv_show.setObjectName("button_rmv_show")
        self.comboBox_exb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_exb.setGeometry(QtCore.QRect(120, 200, 111, 41))
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(30, 60, 91, 16))
        self.label_title.setObjectName("label_title")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(430, 150, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(350, 30, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(90, 280, 631, 181))
        self.tableView.setObjectName("tableView")
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(390, 210, 71, 32))
        self.button_search.setObjectName("button_search")
        self.label_exb = QtWidgets.QLabel(self.centralwidget)
        self.label_exb.setGeometry(QtCore.QRect(60, 210, 60, 16))
        self.label_exb.setObjectName("label_exb")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 150, 113, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(380, 150, 60, 16))
        self.label_date.setObjectName("label_date")
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
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.button_rmv_show.setText(_translate("MainWindow", "Log Visit"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Birds"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_header.setText(_translate("MainWindow", "Shows"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit"))
        self.label_date.setText(_translate("MainWindow", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
