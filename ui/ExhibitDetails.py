# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExhibitDetails.ui'
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
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(40, 20, 113, 32))
        self.Home.setObjectName("Home")
        self.Heading_exhibit = QtWidgets.QLabel(self.centralwidget)
        self.Heading_exhibit.setGeometry(QtCore.QRect(290, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_exhibit.setFont(font)
        self.Heading_exhibit.setObjectName("Heading_exhibit")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(170, 110, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setGeometry(QtCore.QRect(350, 110, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.label_numanimal = QtWidgets.QLabel(self.centralwidget)
        self.label_numanimal.setGeometry(QtCore.QRect(90, 150, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_numanimal.setFont(font)
        self.label_numanimal.setObjectName("label_numanimal")
        self.label_waterfeature = QtWidgets.QLabel(self.centralwidget)
        self.label_waterfeature.setGeometry(QtCore.QRect(330, 150, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_waterfeature.setFont(font)
        self.label_waterfeature.setObjectName("label_waterfeature")
        self.text_name = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_name.setGeometry(QtCore.QRect(220, 100, 91, 31))
        self.text_name.setObjectName("text_name")
        self.text_size = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_size.setGeometry(QtCore.QRect(430, 100, 91, 31))
        self.text_size.setObjectName("text_size")
        self.text_numanimals = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_numanimals.setGeometry(QtCore.QRect(220, 140, 91, 31))
        self.text_numanimals.setObjectName("text_numanimals")
        self.text_waterfeature = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_waterfeature.setGeometry(QtCore.QRect(430, 140, 91, 31))
        self.text_waterfeature.setObjectName("text_waterfeature")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(150, 240, 381, 171))
        self.tableView.setObjectName("tableView")
        self.Logvisit = QtWidgets.QPushButton(self.centralwidget)
        self.Logvisit.setGeometry(QtCore.QRect(290, 190, 113, 32))
        self.Logvisit.setObjectName("Logvisit")
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
        self.Home.setText(_translate("MainWindow", "HOME"))
        self.Heading_exhibit.setText(_translate("MainWindow", "Exhibit Details"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_size.setText(_translate("MainWindow", "Size:"))
        self.label_numanimal.setText(_translate("MainWindow", "Number of animals:"))
        self.label_waterfeature.setText(_translate("MainWindow", "Water feature:"))
        self.Logvisit.setText(_translate("MainWindow", "Log visit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

