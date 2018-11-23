from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__
import sys
app = QtWidgets.QApplication(sys.argv)

import util
import mysql.connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_home = QtWidgets.QPushButton(self.centralwidget)
        self.button_home.setGeometry(QtCore.QRect(20, 10, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.label_header = QtWidgets.QLabel(self.centralwidget)
        self.label_header.setGeometry(QtCore.QRect(360, 20, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(40, 50, 91, 16))
        self.label_title.setObjectName("label_title")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(80, 140, 60, 16))
        self.label_name.setObjectName("label_name")
        self.label_exb = QtWidgets.QLabel(self.centralwidget)
        self.label_exb.setGeometry(QtCore.QRect(80, 200, 60, 16))
        self.label_exb.setObjectName("label_exb")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(400, 140, 60, 16))
        self.label_date.setObjectName("label_date")
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(400, 200, 71, 32))
        self.button_search.setObjectName("button_search")
        self.comboBox_exb = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_exb.setGeometry(QtCore.QRect(130, 190, 111, 41))
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(440, 140, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.button_rmv_show = QtWidgets.QPushButton(self.centralwidget)
        self.button_rmv_show.setGeometry(QtCore.QRect(340, 470, 113, 32))
        self.button_rmv_show.setObjectName("button_rmv_show")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 140, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(180, 240, 361, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(640, 140, 133, 20))
        self.checkBox.setObjectName("checkBox")
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
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.label_header.setText(_translate("MainWindow", "Shows"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit"))
        self.label_date.setText(_translate("MainWindow", "Date"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(5, _translate("MainWindow", "Birds"))
        self.button_rmv_show.setText(_translate("MainWindow", "Remove Show"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Exhibit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        self.checkBox.setText(_translate("MainWindow", "All Date and Time"))



    def userDefinedInitialisation(self):
        self.button_search.clicked.connect(self.searchShows)
        self.button_rmv_show.clicked.connect(self.removeShows)
        self.button_home.clicked.connect(self.home)
        self.tableWidget.cellClicked.connect(self.highlightRow)
    
    
    def searchShows(self):
        Name = self.lineEdit.text()
        Location = self.comboBox_exb.currentText()
        DateTime = self.dateTimeEdit.dateTime().toString("MM/dd/yyyy hh:mm:ss AP")
        
        if(Location == "All"):
            Location = ""
        if(self.checkBox.isChecked()):
            DateTime = ""

        listTuple = [('Name', Name, "str"), ("Location", Location, "str"), ("DateTime", DateTime, "datetime")]
        
        cmd1 = "SELECT Name, Location as Exhibit, DateTime from SHOWS "
        cmd1 = util.addWHERE(cmd1, listTuple)
        cmd1 += ";"

        print(cmd1)

        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
        
        cursor = connection_object.cursor()
        cursor.execute(cmd1)
        record = cursor.fetchall()
        print(record)
        
        self.tableWidget.setRowCount(0)
        for row_num, row_data in enumerate(record):
            # insert a new blank row
            # in other words, expand the table by inserting a new row
            self.tableWidget.insertRow(row_num)
            for column_num, data in enumerate(row_data):
                # IMPORTANT
                DATETIMECOLUMN = 2
                cellContent = None
                if(column_num == DATETIMECOLUMN):
                    cellContent = data.strftime("%m/%d/%Y %I:%M:%S %p")
                if(cellContent == None):
                    cellContent = str(data)
                self.tableWidget.setItem(row_num, column_num,QtWidgets.QTableWidgetItem(cellContent))



        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")


    def removeShows(self):



        rowsSelected = self.tableWidget.selectionModel().selectedRows()
        if(len(rowsSelected) >0):
            connection_object = connection_pool.get_connection()
            if connection_object.is_connected():
                db_Info = connection_object.get_server_info()
                print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
            index = rowsSelected[0]
            # index consist of row() column()
            row = index.row()
            ShowName = self.tableWidget.item(row,0).text()
            ExhibitName = self.tableWidget.item(row,1).text()
            DateTime = self.tableWidget.item(row,2).text()
            try:
               cmd = "DELETE FROM SHOWS WHERE Name = \'" + ShowName + "\' AND DateTime= STR_TO_DATE(\'" + DateTime + "\' , \'%m/%d/%Y %r\');"
                
               cursor = connection_object.cursor()
               cursor.execute(cmd)
               connection_object.commit()
               print("Delete Successfully")
               self.searchShows()
            except mysql.connector.IntegrityError as err:
                print("Error: {}".format(err))
            
            if(connection_object.is_connected()):
                cursor.close()
                connection_object.close()
                print("MySQL connection is closed")
        else:
            print("No row is selected")

                


    def highlightRow(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
    
    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.adminUIs['administratorFunctionality'] # admin
        app.exit()


def render():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
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
    
    table = MyTable(data, 5, 5)
    table.show()
    sys.exit(app.exec_())



