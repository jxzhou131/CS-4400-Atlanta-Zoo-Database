# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminViewVisitors.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewVisitor(object):
    def setupUi(self, ViewVisitor):
        ViewVisitor.setObjectName("ViewVisitor")
        ViewVisitor.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ViewVisitor)
        self.centralwidget.setObjectName("centralwidget")
        self.viewVisitorsLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewVisitorsLabel.setGeometry(QtCore.QRect(290, 60, 211, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.viewVisitorsLabel.setFont(font)
        self.viewVisitorsLabel.setObjectName("viewVisitorsLabel")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(80, 300, 631, 181))
        self.tableView.setObjectName("tableView")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(80, 510, 171, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 91, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(100, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setGeometry(QtCore.QRect(240, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(150, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 210, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(570, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        ViewVisitor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ViewVisitor)
        self.statusbar.setObjectName("statusbar")
        ViewVisitor.setStatusBar(self.statusbar)

        self.retranslateUi(ViewVisitor)
        QtCore.QMetaObject.connectSlotsByName(ViewVisitor)

    def retranslateUi(self, ViewVisitor):
        _translate = QtCore.QCoreApplication.translate
        ViewVisitor.setWindowTitle(_translate("ViewVisitor", "ViewVisitor"))
        self.viewVisitorsLabel.setText(_translate("ViewVisitor", "View Visitors"))
        self.deleteButton.setText(_translate("ViewVisitor", "Delete Visitor"))
        self.homeButton.setText(_translate("ViewVisitor", "HOME"))
        self.usernameLabel.setText(_translate("ViewVisitor", "Username"))
        self.emailLabel.setText(_translate("ViewVisitor", "Email"))
        self.searchButton.setText(_translate("ViewVisitor", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewVisitor = QtWidgets.QMainWindow()
    ui = Ui_ViewVisitor()
    ui.setupUi(ViewVisitor)
    ViewVisitor.show()
    sys.exit(app.exec_())

