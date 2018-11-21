
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Homebutton.setGeometry(QtCore.QRect(40, 20, 113, 32))
        self.Homebutton.setObjectName("Homebutton")
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
        self.label_size.setGeometry(QtCore.QRect(400, 110, 60, 16))
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
        self.label_waterfeature.setGeometry(QtCore.QRect(350, 150, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_waterfeature.setFont(font)
        self.label_waterfeature.setObjectName("label_waterfeature")
        self.Logvisit = QtWidgets.QPushButton(self.centralwidget)
        self.Logvisit.setGeometry(QtCore.QRect(310, 190, 113, 32))
        self.Logvisit.setObjectName("Logvisit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 270, 201, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(220, 110, 113, 21))
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_numanimals = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_numanimals.setGeometry(QtCore.QRect(220, 150, 113, 21))
        self.lineEdit_numanimals.setReadOnly(True)
        self.lineEdit_numanimals.setObjectName("lineEdit_numanimals")
        self.lineEdit_size = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_size.setGeometry(QtCore.QRect(470, 110, 113, 21))
        self.lineEdit_size.setReadOnly(True)
        self.lineEdit_size.setObjectName("lineEdit_size")
        self.lineEdit_water = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_water.setGeometry(QtCore.QRect(470, 150, 113, 21))
        self.lineEdit_water.setReadOnly(True)
        self.lineEdit_water.setObjectName("lineEdit_water")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.userDefinedInitialisation()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Homebutton.setText(_translate("MainWindow", "HOME"))
        self.Heading_exhibit.setText(_translate("MainWindow", "Exhibit Details"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_size.setText(_translate("MainWindow", "Size:"))
        self.label_numanimal.setText(_translate("MainWindow", "Number of animals:"))
        self.label_waterfeature.setText(_translate("MainWindow", "Water feature:"))
        self.Logvisit.setText(_translate("MainWindow", "Log visit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Species"))

    def userDefinedInitialisation(self):
        self.Logvisit.clicked.connect(self.logvisit)
        self.Homebutton.clicked.connect(self.home)


    def display(self):

        cmd =" SELECT Name FROM EXHIBIT"
        cmd = util.addWhere(Cmd, __main__.arg)
        cursor = connection_object.cursor()
        cursor.execute(cmd1)
        record = cursor.fetchall()
        self.lineEdit_name.setObjectName("\'" + record + "\'")
    
    
        self.display_numanimal.setObjectName("display_numanimal")
        self.dislay_size.setObjectName("dislay_size")
        self.display_waterfeature.setObjectName("display_waterfeature")
    

    def logvisit(self):

        cmd1 =" SELECT Name FROM EXHIBIT"
        cmd1 = util.addWhere(Cmd, __main__.arg)
        cursor = connection_object.cursor()
        cursor.execute(cmd1)
        record = cursor.fetchall()
        
        cmd2="insert into VISITEXHIBIT values(‘loginIdentity[0][0]’，\'" + record + "\'，\‘" +  time.strftime("%m/%d/%Y %I:%M:%S %p")+"\')"


    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality'] # visitor
        app.exit()




def render():
    __main__.state = -10
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

    # close the WINDOWS
    MainWindow.close()


    MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
