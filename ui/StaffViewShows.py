# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffViewShows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_staffViewShows(object):
    def setupUi(self, staffViewShows):
        staffViewShows.setObjectName("staffViewShows")
        staffViewShows.resize(800, 604)
        self.centralwidget = QtWidgets.QWidget(staffViewShows)
        self.centralwidget.setObjectName("centralwidget")
        self.HomePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomePushButton.setGeometry(QtCore.QRect(0, 0, 101, 41))
        self.HomePushButton.setObjectName("HomePushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 501, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.StaffTable = QtWidgets.QTableWidget(self.centralwidget)
        self.StaffTable.setGeometry(QtCore.QRect(150, 120, 511, 311))
        self.StaffTable.setObjectName("StaffTable")
        self.StaffTable.setColumnCount(3)
        self.StaffTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.StaffTable.setHorizontalHeaderItem(2, item)
        staffViewShows.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(staffViewShows)
        self.statusbar.setObjectName("statusbar")
        staffViewShows.setStatusBar(self.statusbar)

        self.retranslateUi(staffViewShows)
        QtCore.QMetaObject.connectSlotsByName(staffViewShows)

    def retranslateUi(self, staffViewShows):
        _translate = QtCore.QCoreApplication.translate
        staffViewShows.setWindowTitle(_translate("staffViewShows", "View Staff Show"))
        self.HomePushButton.setText(_translate("staffViewShows", "Home"))
        self.label.setText(_translate("staffViewShows", " Staff - Show History"))
        item = self.StaffTable.horizontalHeaderItem(0)
        item.setText(_translate("staffViewShows", "Name"))
        item = self.StaffTable.horizontalHeaderItem(1)
        item.setText(_translate("staffViewShows", "Time"))
        item = self.StaffTable.horizontalHeaderItem(2)
        item.setText(_translate("staffViewShows", "Exhibit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffViewShows = QtWidgets.QMainWindow()
    ui = Ui_staffViewShows()
    ui.setupUi(staffViewShows)
    staffViewShows.show()
    sys.exit(app.exec_())

