# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminViewStaff.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adminViewStaff(object):
    def setupUi(self, adminViewStaff):
        adminViewStaff.setObjectName("adminViewStaff")
        adminViewStaff.resize(665, 465)
        self.centralwidget = QtWidgets.QWidget(adminViewStaff)
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
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.gridLayout.addWidget(self.homeButton, 0, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(106, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 9, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(159, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 3)
        self.userList = QtWidgets.QTableWidget(self.centralwidget)
        self.userList.setMinimumSize(QtCore.QSize(300, 150))
        self.userList.setObjectName("userList")
        self.userList.setColumnCount(2)
        self.userList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.userList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.userList.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.userList, 2, 3, 1, 5)
        spacerItem7 = QtWidgets.QSpacerItem(173, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 8, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 6, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(249, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 0, 1, 5)
        self.deleteStaffMemberButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deleteStaffMemberButton.setFont(font)
        self.deleteStaffMemberButton.setObjectName("deleteStaffMemberButton")
        self.gridLayout.addWidget(self.deleteStaffMemberButton, 4, 5, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 7, 1, 3)
        adminViewStaff.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(adminViewStaff)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 20))
        self.menubar.setObjectName("menubar")
        adminViewStaff.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(adminViewStaff)
        self.statusbar.setObjectName("statusbar")
        adminViewStaff.setStatusBar(self.statusbar)

        self.retranslateUi(adminViewStaff)
        QtCore.QMetaObject.connectSlotsByName(adminViewStaff)

    def retranslateUi(self, adminViewStaff):
        _translate = QtCore.QCoreApplication.translate
        adminViewStaff.setWindowTitle(_translate("adminViewStaff", "MainWindow"))
        self.label.setText(_translate("adminViewStaff", "Atlanta Zoo"))
        self.label_2.setText(_translate("adminViewStaff", "View Staff"))
        self.homeButton.setText(_translate("adminViewStaff", "Home"))
        item = self.userList.horizontalHeaderItem(0)
        item.setText(_translate("adminViewStaff", "Username"))
        item = self.userList.horizontalHeaderItem(1)
        item.setText(_translate("adminViewStaff", "email"))
        self.deleteStaffMemberButton.setText(_translate("adminViewStaff", "Delete Staff Member"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminViewStaff = QtWidgets.QMainWindow()
    ui = Ui_adminViewStaff()
    ui.setupUi(adminViewStaff)
    adminViewStaff.show()
    sys.exit(app.exec_())

