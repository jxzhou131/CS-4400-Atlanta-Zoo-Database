
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

headerDict = {
    0: "Name",
    1: "Species"
}

orderDict = {
    0: "ASC",
    1: "DESC"
}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(3, 2, 786, 585))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Homebutton = QtWidgets.QPushButton(self.widget)
        self.Homebutton.setMinimumSize(QtCore.QSize(114, 49))
        self.Homebutton.setMaximumSize(QtCore.QSize(114, 49))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Homebutton.setFont(font)
        self.Homebutton.setObjectName("Homebutton")
        self.gridLayout_2.addWidget(self.Homebutton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(156, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 2)
        self.Heading_exhibit = QtWidgets.QLabel(self.widget)
        self.Heading_exhibit.setMinimumSize(QtCore.QSize(244, 44))
        self.Heading_exhibit.setMaximumSize(QtCore.QSize(244, 44))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.Heading_exhibit.setFont(font)
        self.Heading_exhibit.setObjectName("Heading_exhibit")
        self.gridLayout_2.addWidget(self.Heading_exhibit, 0, 3, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(230, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 6, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setMinimumSize(QtCore.QSize(162, 35))
        self.label_name.setMaximumSize(QtCore.QSize(162, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(200, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_size = QtWidgets.QLabel(self.widget)
        self.label_size.setMinimumSize(QtCore.QSize(136, 31))
        self.label_size.setMaximumSize(QtCore.QSize(136, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.gridLayout.addWidget(self.label_size, 0, 2, 1, 1)
        self.lineEdit_size = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_size.setMinimumSize(QtCore.QSize(199, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_size.setFont(font)
        self.lineEdit_size.setReadOnly(True)
        self.lineEdit_size.setObjectName("lineEdit_size")
        self.gridLayout.addWidget(self.lineEdit_size, 0, 3, 1, 1)
        self.label_numanimal = QtWidgets.QLabel(self.widget)
        self.label_numanimal.setMinimumSize(QtCore.QSize(172, 43))
        self.label_numanimal.setMaximumSize(QtCore.QSize(172, 43))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_numanimal.setFont(font)
        self.label_numanimal.setObjectName("label_numanimal")
        self.gridLayout.addWidget(self.label_numanimal, 1, 0, 1, 1)
        self.lineEdit_numanimals = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_numanimals.setMinimumSize(QtCore.QSize(199, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_numanimals.setFont(font)
        self.lineEdit_numanimals.setReadOnly(True)
        self.lineEdit_numanimals.setObjectName("lineEdit_numanimals")
        self.gridLayout.addWidget(self.lineEdit_numanimals, 1, 1, 1, 1)
        self.label_waterfeature = QtWidgets.QLabel(self.widget)
        self.label_waterfeature.setMinimumSize(QtCore.QSize(136, 38))
        self.label_waterfeature.setMaximumSize(QtCore.QSize(136, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_waterfeature.setFont(font)
        self.label_waterfeature.setObjectName("label_waterfeature")
        self.gridLayout.addWidget(self.label_waterfeature, 1, 2, 1, 1)
        self.lineEdit_water = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_water.setMinimumSize(QtCore.QSize(199, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_water.setFont(font)
        self.lineEdit_water.setReadOnly(True)
        self.lineEdit_water.setObjectName("lineEdit_water")
        self.gridLayout.addWidget(self.lineEdit_water, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 8)
        spacerItem3 = QtWidgets.QSpacerItem(312, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 4)
        self.Logvisit = QtWidgets.QPushButton(self.widget)
        self.Logvisit.setMinimumSize(QtCore.QSize(127, 43))
        self.Logvisit.setMaximumSize(QtCore.QSize(127, 43))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.Logvisit.setFont(font)
        self.Logvisit.setObjectName("Logvisit")
        self.gridLayout_2.addWidget(self.Logvisit, 3, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(289, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 5, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(207, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 4, 0, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMinimumSize(QtCore.QSize(352, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 2, 2, 5)
        spacerItem6 = QtWidgets.QSpacerItem(184, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 5, 7, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem7, 6, 4, 1, 1)
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
        self.Homebutton.setText(_translate("MainWindow", "Home"))
        self.Heading_exhibit.setText(_translate("MainWindow", "Exhibit Details"))
        self.label_name.setText(_translate("MainWindow", "                 Name:"))
        self.label_size.setText(_translate("MainWindow", "              Size:"))
        self.label_numanimal.setText(_translate("MainWindow", "Number of animals:"))
        self.label_waterfeature.setText(_translate("MainWindow", "Water feature:"))
        self.Logvisit.setText(_translate("MainWindow", "Log visit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Species"))


    def userDefinedInitialisation(self):
        self.currentOrder = 0
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.Logvisit.clicked.connect(self.logvisit)
        self.Homebutton.clicked.connect(self.home)
        self.displayText()
        self.displayAnimals()        
        header = self.tableWidget.horizontalHeader()
        header.sectionClicked.connect(self.displayAnimals)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToAnimalDetail)

    def highlightRowOrToAnimalDetail(self, row, column):
                # highlight the row selected
        self.tableWidget.selectRow(row)
        Name = str(self.tableWidget.item(row,column).text())
        # Enter IF statement if the selected column is the exhibit column
        if(column == 0):
            # retrieve the content in the cell
            Name = str(self.tableWidget.item(row,column).text())
            Species = str(self.tableWidget.item(row,column+1).text())
            # store the information into the __main__.arg
            # the information is later passed to the exhibitDetails page
            __main__.arg = [("Name", Name, "str"), ("Species", Species, "str")]
            __main__.status = __main__.statusDef["Normal"]
            __main__.state = __main__.visitorUIs["animalDetails"]
            app.exit()
            # FOR DEBUGGING PURPOSE
            print("row, column, animalName")
            print(str(row) + "," + str(column) + "," + Name)
        print("row, column, animalName")
        print(str(row) + "," + str(column) + "," + Name)

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



    def displayAnimals(self, column = 0):

        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)


        cmd="SELECT Name, Species FROM ANIMAL WHERE Exhibit = \'" + str( __main__.arg[0][1])+ "\' "
        cmd += " order by " + headerDict[column] + " " + orderDict[self.currentOrder]
        if(self.currentOrder == 0):
            self.currentOrder = 1
        else: 
            self.currentOrder = 0

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
