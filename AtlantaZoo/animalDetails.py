# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'animalDetail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#################### MUST HAVE #################################################################
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__
import sys
app = QtWidgets.QApplication(sys.argv)
import time
import util
import mysql.connector
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 500, 464))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_home = QtWidgets.QPushButton(self.widget)
        self.button_home.setMinimumSize(QtCore.QSize(118, 53))
        self.button_home.setMaximumSize(QtCore.QSize(118, 53))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.gridLayout_2.addWidget(self.button_home, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(228, 45))
        self.label.setMaximumSize(QtCore.QSize(228, 45))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(106, 30))
        self.label_2.setMaximumSize(QtCore.QSize(106, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(335, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 2, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameLabel = QtWidgets.QLabel(self.widget)
        self.nameLabel.setMinimumSize(QtCore.QSize(81, 28))
        self.nameLabel.setMaximumSize(QtCore.QSize(81, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(148, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)
        self.exhibitLabel = QtWidgets.QLabel(self.widget)
        self.exhibitLabel.setMinimumSize(QtCore.QSize(82, 25))
        self.exhibitLabel.setMaximumSize(QtCore.QSize(82, 25))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.gridLayout.addWidget(self.exhibitLabel, 1, 0, 1, 1)
        self.exhibitLineEdit = QtWidgets.QLineEdit(self.widget)
        self.exhibitLineEdit.setMinimumSize(QtCore.QSize(148, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.exhibitLineEdit.setFont(font)
        self.exhibitLineEdit.setObjectName("exhibitLineEdit")
        self.gridLayout.addWidget(self.exhibitLineEdit, 1, 1, 1, 1)
        self.speciesLabel = QtWidgets.QLabel(self.widget)
        self.speciesLabel.setMinimumSize(QtCore.QSize(79, 28))
        self.speciesLabel.setMaximumSize(QtCore.QSize(79, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.speciesLabel.setFont(font)
        self.speciesLabel.setObjectName("speciesLabel")
        self.gridLayout.addWidget(self.speciesLabel, 2, 0, 1, 1)
        self.speciesLineEdit = QtWidgets.QLineEdit(self.widget)
        self.speciesLineEdit.setMinimumSize(QtCore.QSize(183, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.speciesLineEdit.setFont(font)
        self.speciesLineEdit.setObjectName("speciesLineEdit")
        self.gridLayout.addWidget(self.speciesLineEdit, 2, 1, 1, 1)
        self.typeLabel = QtWidgets.QLabel(self.widget)
        self.typeLabel.setMinimumSize(QtCore.QSize(79, 29))
        self.typeLabel.setMaximumSize(QtCore.QSize(79, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout.addWidget(self.typeLabel, 3, 0, 1, 1)
        self.typeLineEdit = QtWidgets.QLineEdit(self.widget)
        self.typeLineEdit.setMinimumSize(QtCore.QSize(184, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.typeLineEdit.setFont(font)
        self.typeLineEdit.setObjectName("typeLineEdit")
        self.gridLayout.addWidget(self.typeLineEdit, 3, 1, 1, 1)
        self.ageLabel = QtWidgets.QLabel(self.widget)
        self.ageLabel.setMinimumSize(QtCore.QSize(79, 34))
        self.ageLabel.setMaximumSize(QtCore.QSize(79, 34))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.ageLabel.setFont(font)
        self.ageLabel.setObjectName("ageLabel")
        self.gridLayout.addWidget(self.ageLabel, 4, 0, 1, 1)
        self.ageLineEdit = QtWidgets.QLineEdit(self.widget)
        self.ageLineEdit.setMinimumSize(QtCore.QSize(113, 30))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.ageLineEdit.setFont(font)
        self.ageLineEdit.setObjectName("ageLineEdit")
        self.gridLayout.addWidget(self.ageLineEdit, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 2, 4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 4, 3, 1, 1)
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
        self.label.setText(_translate("MainWindow", "Animal Detail"))
        self.label_2.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.exhibitLabel.setText(_translate("MainWindow", "Exhibit:"))
        self.speciesLabel.setText(_translate("MainWindow", "Species:"))
        self.typeLabel.setText(_translate("MainWindow", "Type:"))
        self.ageLabel.setText(_translate("MainWindow", "Age:"))

    def userDefinedInitialization(self):
        self.currentOrder = 0
        self.button_home.clicked.connect(self.home)
        self.loadAnimalDetails()


    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality']
        app.exit()

    def loadAnimalDetails(self):
        # construct the query command
        cmd = "SELECT Name, Species, Type, Age, Exhibit FROM ANIMAL "
        cmd = util.addWHERE(cmd, __main__.arg)
        cmd += ";"

        # DEBUG OUTPUT
        print("cmd")
        print(cmd)
        # obtain the connection_object
        connection_object = connection_pool.get_connection()
        # these three lines of code is used for debugging: CHECK FOR CONNECTIONS
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
        print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
        # get cursor
        cursor = connection_object.cursor()
        try:
            # use cursor to execute sql command
            cursor.execute(cmd)
            # there could have multiple lines of sql command
            # after all the command, retrieve the queries
            record = cursor.fetchall()
            # for DEBUGGING purpose
            print(record)

            self.nameLineEdit.setText(str(record[0][0]))
            self.speciesLineEdit.setText(str(record[0][1]))
            self.typeLineEdit.setText(str(record[0][2]))
            self.ageLineEdit.setText(str(record[0][3]))
            self.exhibitLineEdit.setText(str(record[0][4]))

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        # close the cursor and connection
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

def render():
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    #close the MainWindow
    MainWindow.close()  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

