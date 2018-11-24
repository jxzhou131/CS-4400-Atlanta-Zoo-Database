
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Homebutton.setGeometry(QtCore.QRect(3, 2, 114, 49))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Homebutton.setFont(font)
        self.Homebutton.setObjectName("Homebutton")
        self.Heading_exhibit = QtWidgets.QLabel(self.centralwidget)
        self.Heading_exhibit.setGeometry(QtCore.QRect(277, 28, 244, 44))
        self.Heading_exhibit.setMinimumSize(QtCore.QSize(151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_exhibit.setFont(font)
        self.Heading_exhibit.setObjectName("Heading_exhibit")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(160, 99, 83, 35))
        self.label_name.setMinimumSize(QtCore.QSize(60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setGeometry(QtCore.QRect(552, 107, 64, 25))
        self.label_size.setMinimumSize(QtCore.QSize(60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.label_numanimal = QtWidgets.QLabel(self.centralwidget)
        self.label_numanimal.setGeometry(QtCore.QRect(14, 134, 228, 43))
        self.label_numanimal.setMinimumSize(QtCore.QSize(141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_numanimal.setFont(font)
        self.label_numanimal.setObjectName("label_numanimal")
        self.label_waterfeature = QtWidgets.QLabel(self.centralwidget)
        self.label_waterfeature.setGeometry(QtCore.QRect(452, 134, 166, 38))
        self.label_waterfeature.setMinimumSize(QtCore.QSize(101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_waterfeature.setFont(font)
        self.label_waterfeature.setObjectName("label_waterfeature")
        self.Logvisit = QtWidgets.QPushButton(self.centralwidget)
        self.Logvisit.setGeometry(QtCore.QRect(301, 223, 127, 43))
        self.Logvisit.setMinimumSize(QtCore.QSize(113, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Logvisit.setFont(font)
        self.Logvisit.setObjectName("Logvisit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(203, 283, 352, 281))
        self.tableWidget.setMinimumSize(QtCore.QSize(352, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(244, 104, 200, 31))
        self.lineEdit_name.setMinimumSize(QtCore.QSize(113, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_numanimals = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_numanimals.setGeometry(QtCore.QRect(244, 140, 199, 33))
        self.lineEdit_numanimals.setMinimumSize(QtCore.QSize(113, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_numanimals.setFont(font)
        self.lineEdit_numanimals.setReadOnly(True)
        self.lineEdit_numanimals.setObjectName("lineEdit_numanimals")
        self.lineEdit_size = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_size.setGeometry(QtCore.QRect(618, 105, 114, 31))
        self.lineEdit_size.setMinimumSize(QtCore.QSize(113, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_size.setFont(font)
        self.lineEdit_size.setReadOnly(True)
        self.lineEdit_size.setObjectName("lineEdit_size")
        self.lineEdit_water = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_water.setGeometry(QtCore.QRect(617, 141, 115, 28))
        self.lineEdit_water.setMinimumSize(QtCore.QSize(113, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.lineEdit_water.setFont(font)
        self.lineEdit_water.setReadOnly(True)
        self.lineEdit_water.setObjectName("lineEdit_water")
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.Logvisit.clicked.connect(self.logvisit)
        self.Homebutton.clicked.connect(self.home)
        self.displayText()
        self.displayAnimals()


    def displayText(self):

        print(__main__.arg[0][1])

        self.lineEdit_name.setText(str( __main__.arg[0][1]))
        

        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
                
        #display Size
        cmd =" SELECT Size FROM EXHIBIT WHERE Name = \'" + str( __main__.arg[0][1])+ "\' ;"
        # get cursor
        cursor = connection_object.cursor()
        cursor.execute(cmd)
        record = cursor.fetchall()
        self.lineEdit_size.setText(str(record[0][0]))
        
        #display WaterFeature
        cmd2 =" SELECT WaterFeature FROM EXHIBIT WHERE Name = \'" + str( __main__.arg[0][1])+ "\' ;"
        cursor.execute(cmd2)
        record = cursor.fetchall()
        if(record[0][0] is 1):
            self.lineEdit_water.setText("Yes")
        elif(record[0][0] is 0):
            self.lineEdit_water.setText("No")

        #display number of animals
        cmd3 = "SELECT COUNT(*) FROM EXHIBIT as E, ANIMAL as A WHERE E.Name=A.Exhibit AND E.Name = \'" + str( __main__.arg[0][1])+ "\' GROUP BY E.Name"

        cursor.execute(cmd3)
        record = cursor.fetchall()
        self.lineEdit_numanimals.setText(str(record[0][0]))

        
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

    
            

    def logvisit(self):

        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
        
        Visitor = __main__.loginIdentity[0][0]
        DateTime=time.strftime("%m/%d/%Y %I:%M:%S %p");
        try:
            cmd="insert into VISITEXHIBIT values(\'" + Visitor + "\',\'" + str( __main__.arg[0][1])+ "\',STR_TO_DATE(\'" + DateTime + "\' , \'%m/%d/%Y %r\'))"
            cursor = connection_object.cursor()
            cursor.execute(cmd)
            connection_object.commit()
            print("Insert Successfully")
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")



    def displayAnimals(self):

        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)


        cmd="SELECT Name, Species FROM ANIMAL WHERE Exhibit = \'" + str( __main__.arg[0][1])+ "\'"

        cursor = connection_object.cursor()
        cursor.execute(cmd)
        record = cursor.fetchall()
    
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(record):
            # insert a new blank row
            # in other words, expand the table by inserting a new row
            self.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                # IMPORTANT
                # first you must determine in which column does the DateTime attribute occur in your
                # query
                cellContent = None
                if(cellContent is None):
                    cellContent = str(data)
                self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(cellContent))

        # close the cursor and connection                  
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
