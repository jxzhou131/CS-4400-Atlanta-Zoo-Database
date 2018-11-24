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
        MainWindow.resize(868, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(5, 3, 842, 522))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_home = QtWidgets.QPushButton(self.widget)
        self.button_home.setMinimumSize(QtCore.QSize(112, 49))
        self.button_home.setMaximumSize(QtCore.QSize(112, 49))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.button_home.setFont(font)
        self.button_home.setObjectName("button_home")
        self.gridLayout_3.addWidget(self.button_home, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(182, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 2)
        self.label_header = QtWidgets.QLabel(self.widget)
        self.label_header.setMinimumSize(QtCore.QSize(123, 57))
        self.label_header.setMaximumSize(QtCore.QSize(123, 57))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label_header.setFont(font)
        self.label_header.setObjectName("label_header")
        self.gridLayout_3.addWidget(self.label_header, 0, 4, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(327, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 6, 1, 2)
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setMinimumSize(QtCore.QSize(109, 32))
        self.label_title.setMaximumSize(QtCore.QSize(109, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_3.addWidget(self.label_title, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(651, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 6)
        spacerItem3 = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setMinimumSize(QtCore.QSize(61, 32))
        self.label_name.setMaximumSize(QtCore.QSize(61, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(194, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_exb = QtWidgets.QLabel(self.widget)
        self.label_exb.setMinimumSize(QtCore.QSize(64, 29))
        self.label_exb.setMaximumSize(QtCore.QSize(64, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_exb.setFont(font)
        self.label_exb.setObjectName("label_exb")
        self.gridLayout.addWidget(self.label_exb, 1, 0, 1, 1)
        self.comboBox_exb = QtWidgets.QComboBox(self.widget)
        self.comboBox_exb.setMinimumSize(QtCore.QSize(194, 36))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.comboBox_exb.setFont(font)
        self.comboBox_exb.setObjectName("comboBox_exb")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.comboBox_exb.addItem("")
        self.gridLayout.addWidget(self.comboBox_exb, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 1, 1, 4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_date = QtWidgets.QLabel(self.widget)
        self.label_date.setMinimumSize(QtCore.QSize(53, 28))
        self.label_date.setMaximumSize(QtCore.QSize(53, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.gridLayout_2.addWidget(self.label_date, 0, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(227, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 0, 1, 1, 3)
        self.button_search = QtWidgets.QPushButton(self.widget)
        self.button_search.setMinimumSize(QtCore.QSize(117, 39))
        self.button_search.setMaximumSize(QtCore.QSize(117, 39))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.button_search.setFont(font)
        self.button_search.setObjectName("button_search")
        self.gridLayout_2.addWidget(self.button_search, 1, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setMinimumSize(QtCore.QSize(100, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 5, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(83, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 2, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(53, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMinimumSize(QtCore.QSize(602, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_3.addWidget(self.tableWidget, 3, 1, 1, 6)
        spacerItem7 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 3, 7, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(277, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 4, 0, 1, 3)
        self.button_rmv_show = QtWidgets.QPushButton(self.widget)
        self.button_rmv_show.setMinimumSize(QtCore.QSize(153, 38))
        self.button_rmv_show.setMaximumSize(QtCore.QSize(153, 38))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.button_rmv_show.setFont(font)
        self.button_rmv_show.setObjectName("button_rmv_show")
        self.gridLayout_3.addWidget(self.button_rmv_show, 4, 3, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(317, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 4, 6, 1, 2)
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
        self.button_home.setText(_translate("MainWindow", "Home"))
        self.label_header.setText(_translate("MainWindow", "Shows"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_exb.setText(_translate("MainWindow", "Exhibit:"))
        self.comboBox_exb.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_exb.setItemText(1, _translate("MainWindow", "Pacific"))
        self.comboBox_exb.setItemText(2, _translate("MainWindow", "Jungle"))
        self.comboBox_exb.setItemText(3, _translate("MainWindow", "Sahara"))
        self.comboBox_exb.setItemText(4, _translate("MainWindow", "Mountainous"))
        self.comboBox_exb.setItemText(5, _translate("MainWindow", "Birds"))
        self.label_date.setText(_translate("MainWindow", "Date:"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "M/d/yyyy h:mm AP"))
        self.button_search.setText(_translate("MainWindow", "Search"))
        self.checkBox.setText(_translate("MainWindow", "All Time"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Exhibit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        self.button_rmv_show.setText(_translate("MainWindow", "Remove Show"))



    def userDefinedInitialisation(self):
        self.button_search.clicked.connect(self.searchShows)
        self.button_rmv_show.clicked.connect(self.removeShows)
        self.button_home.clicked.connect(self.home)
        self.tableWidget.cellClicked.connect(self.highlightRow)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    
    
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



