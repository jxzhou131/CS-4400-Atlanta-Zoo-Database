# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminviewstaff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adminviewstaff(object):
    def setupUi(self, adminviewstaff):
        adminviewstaff.setObjectName("adminviewstaff")
        adminviewstaff.resize(665, 465)
        self.centralwidget = QtWidgets.QWidget(adminviewstaff)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(34, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(94, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 6, 1, 2)
        self.home = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.home.setFont(font)
        self.home.setObjectName("home")
        self.gridLayout.addWidget(self.home, 0, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(106, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 9, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(159, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 2, 3, 1, 5)
        spacerItem7 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 8, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 6, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(249, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 5, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 7, 1, 3)
        adminviewstaff.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminviewstaff)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 20))
        self.menubar.setObjectName("menubar")
        adminviewstaff.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminviewstaff)
        self.statusbar.setObjectName("statusbar")
        adminviewstaff.setStatusBar(self.statusbar)

        self.retranslateUi(adminviewstaff)
        QtCore.QMetaObject.connectSlotsByName(adminviewstaff)

    def retranslateUi(self, adminviewstaff):
        _translate = QtCore.QCoreApplication.translate
        adminviewstaff.setWindowTitle(_translate("adminviewstaff", "MainWindow"))
        self.label.setText(_translate("adminviewstaff", "Atlanta Zoo"))
        self.label_2.setText(_translate("adminviewstaff", "View Staff"))
        self.home.setText(_translate("adminviewstaff", "Home"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("adminviewstaff", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("adminviewstaff", "email"))
        self.pushButton.setText(_translate("adminviewstaff", "Delete Staff Member"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminviewstaff = QtWidgets.QMainWindow()
    ui = Ui_adminviewstaff()
    ui.setupUi(adminviewstaff)
    adminviewstaff.show()
    sys.exit(app.exec_())

