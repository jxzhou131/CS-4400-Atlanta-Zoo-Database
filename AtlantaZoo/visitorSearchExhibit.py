from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__
import sys
app = QtWidgets.QApplication(sys.argv)

import util


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading_exhibit = QtWidgets.QLabel(self.centralwidget)
        self.Heading_exhibit.setGeometry(QtCore.QRect(250, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_exhibit.setFont(font)
        self.Heading_exhibit.setObjectName("Heading_exhibit")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(60, 100, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_numanimals = QtWidgets.QLabel(self.centralwidget)
        self.label_numanimals.setGeometry(QtCore.QRect(270, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_numanimals.setFont(font)
        self.label_numanimals.setObjectName("label_numanimals")
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setGeometry(QtCore.QRect(60, 170, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.label_waterfeature = QtWidgets.QLabel(self.centralwidget)
        self.label_waterfeature.setGeometry(QtCore.QRect(280, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_waterfeature.setFont(font)
        self.label_waterfeature.setObjectName("label_waterfeature")
        self.label_sizemin = QtWidgets.QLabel(self.centralwidget)
        self.label_sizemin.setGeometry(QtCore.QRect(120, 150, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_sizemin.setFont(font)
        self.label_sizemin.setObjectName("label_sizemin")
        self.label_sizemax = QtWidgets.QLabel(self.centralwidget)
        self.label_sizemax.setGeometry(QtCore.QRect(180, 150, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_sizemax.setFont(font)
        self.label_sizemax.setObjectName("label_sizemax")
        self.label_nummin = QtWidgets.QLabel(self.centralwidget)
        self.label_nummin.setGeometry(QtCore.QRect(420, 70, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_nummin.setFont(font)
        self.label_nummin.setObjectName("label_nummin")
        self.label_nummax = QtWidgets.QLabel(self.centralwidget)
        self.label_nummax.setGeometry(QtCore.QRect(470, 70, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_nummax.setFont(font)
        self.label_nummax.setObjectName("label_nummax")
        self.spinBox_minnum = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_minnum.setGeometry(QtCore.QRect(410, 90, 48, 24))
        self.spinBox_minnum.setObjectName("spinBox_minnum")
        self.spinBox_maxnum = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_maxnum.setGeometry(QtCore.QRect(470, 90, 48, 24))
        self.spinBox_maxnum.setObjectName("spinBox_maxnum")
        self.spinBox_maxsize = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_maxsize.setGeometry(QtCore.QRect(170, 170, 48, 24))
        self.spinBox_maxsize.setObjectName("spinBox_maxsize")
        self.spinBox_minsize = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_minsize.setGeometry(QtCore.QRect(110, 170, 48, 24))
        self.spinBox_minsize.setObjectName("spinBox_minsize")
        self.WaterCombo = QtWidgets.QComboBox(self.centralwidget)
        self.WaterCombo.setGeometry(QtCore.QRect(380, 170, 104, 26))
        self.WaterCombo.setObjectName("WaterCombo")
        self.WaterCombo.addItem("")
        self.WaterCombo.addItem("")
        self.WaterCombo.addItem("")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 90, 121, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.Searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Searchbutton.setGeometry(QtCore.QRect(220, 210, 113, 32))
        self.Searchbutton.setObjectName("Searchbutton")
        self.Homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Homebutton.setGeometry(QtCore.QRect(0, 0, 113, 32))
        self.Homebutton.setObjectName("Homebutton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 260, 401, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
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
        self.Heading_exhibit.setText(_translate("MainWindow", "Exhibit"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_numanimals.setText(_translate("MainWindow", "Number of animals:"))
        self.label_size.setText(_translate("MainWindow", "Size:"))
        self.label_waterfeature.setText(_translate("MainWindow", "Water feature:"))
        self.label_sizemin.setText(_translate("MainWindow", "Min"))
        self.label_sizemax.setText(_translate("MainWindow", "Max"))
        self.label_nummin.setText(_translate("MainWindow", "Min"))
        self.label_nummax.setText(_translate("MainWindow", "Max"))
        self.WaterCombo.setItemText(0, _translate("MainWindow", "All"))
        self.WaterCombo.setItemText(1, _translate("MainWindow", "Yes"))
        self.WaterCombo.setItemText(2, _translate("MainWindow", "No"))
        self.Searchbutton.setText(_translate("MainWindow", "Search"))
        self.Homebutton.setText(_translate("MainWindow", "HOME"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NumAnimals"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "WaterFeature"))


    def userDefinedInitialisation(self):
        self.Searchbutton.clicked.connect(self.searchExhibit)
        self.Homebutton.clicked.connect(self.home)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)

    def searchExhibit(self):
        Name = self.lineEdit_name.text()
        MaxSize = self.spinBox_maxsize.value()
        MinSize = self.spinBox_minsize.value()
        MaxNum= self.spinBox_maxnum.value()
        MinNum= self.spinBox_minnum.value()
        WaterFeature= self.WaterCombo.currentText()
        
        if(WaterFeature=="All"):
            WaterFeature=''
        if(WaterFeature=="Yes"):
            WaterFeature="True"
        if(WaterFeature=="No"):
            WaterFeature="False"
        if(MaxSize==0 and MinSize==0):
            MaxSize=''
            MinSize=''
        if(MaxNum==0 and MinSize==0):
            MaxNum=''
            MinNum=''
                

        cmd1= "SELECT E.Name, WaterFeature, Size, COUNT(*) FROM EXHIBIT as E, ANIMAL as A"
        
        AExhibit = "A.Exhibit"
        listTuple = [("E.Name", AExhibit), ("E.name", Name),("MinSize",MinSize),("WaterFeature",WaterFeature),("MaxSize", MaxSize),("MinCOUNT(*)", MinNum),("MaxCOUNT(*)", MaxNum)]
        
        cmd1 = util.addWHERE(cmd1, listTuple)
        
        cmd1 += "GROUP BY E.Name"

        print(cmd1)
        

        connection_object = connection_pool.get_connection()
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)
        
        cursor = connection_object.cursor()

        cursor.execute(cmd1)
        record = cursor.fetchall()


        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

                
                
    def highlightRowOrToExhibit(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
        # Enter IF statement if the selected column is the exhibit column
        if(column == 2):
            # retrieve the content in the cell
            Name = str(self.tableWidget.item(row,column).text())
            # store the information into the __main__.arg
            # the information is later passed to the exhibitDetails page
            __main__.arg = [("Name", Name)]
            __main__.status = __main__.statusDef["Normal"]
            __main__.state = __main__.visitorUIs["exhibitDetails"]
            app.exit()
            # FOR DEBUGGING PURPOSE
            print("row, column, ExhibitName")
            print(str(row) + "," + str(column) + "," + Name)


            
    def home(self):
        __main__.status = __main__.statusDef['Normal']
        __main__.state = __main__.visitorUIs['visitorFunctionality'] # visitor
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
    sys.exit(app.exec_())



