# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staffFuntionality.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_staffFunctionality(object):
    def setupUi(self, staffFunctionality):
        staffFunctionality.setObjectName("staffFunctionality")
        staffFunctionality.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(staffFunctionality)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.AtlantaZoo = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.AtlantaZoo.setFont(font)
        self.AtlantaZoo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AtlantaZoo.setAlignment(QtCore.Qt.AlignCenter)
        self.AtlantaZoo.setObjectName("AtlantaZoo")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 7)
        spacerItem = QtWidgets.QSpacerItem(20, 209, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 209, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 209, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.SearchAnimalsPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.SearchAnimalsPushButton.setFont(font)
        self.SearchAnimalsPushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SearchAnimalsPushButton.setObjectName("SearchAnimalsPushButton")
        self.gridLayout.addWidget(self.SearchAnimalsPushButton, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        self.ViewShowsPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.ViewShowsPushButton.setFont(font)
        self.ViewShowsPushButton.setObjectName("ViewShowsPushButton")
        self.gridLayout.addWidget(self.ViewShowsPushButton, 2, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 4, 1, 1)
        self.LogoutPushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.LogoutPushButton.setFont(font)
        self.LogoutPushButton.setObjectName("LogoutPushButton")
        self.gridLayout.addWidget(self.LogoutPushButton, 2, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 3, 5, 1, 1)
        staffFunctionality.setCentralWidget(self.centralwidget)

        self.retranslateUi(staffFunctionality)
        QtCore.QMetaObject.connectSlotsByName(staffFunctionality)

    def retranslateUi(self, staffFunctionality):
        _translate = QtCore.QCoreApplication.translate
        staffFunctionality.setWindowTitle(_translate("staffFunctionality", "Staff Funtionality"))
        self.AtlantaZoo.setText(_translate("staffFunctionality", "Atlanta Zoo"))
        self.SearchAnimalsPushButton.setText(_translate("staffFunctionality", "Search Animals"))
        self.ViewShowsPushButton.setText(_translate("staffFunctionality", "View Shows"))
        self.LogoutPushButton.setText(_translate("staffFunctionality", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    staffFunctionality = QtWidgets.QMainWindow()
    ui = Ui_staffFunctionality()
    ui.setupUi(staffFunctionality)
    staffFunctionality.show()
    sys.exit(app.exec_())

