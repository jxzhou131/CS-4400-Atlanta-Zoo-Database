from PyQt5 import QtCore, QtGui, QtWidgets
# import the connection_pool established in the connect.py
from __main__ import connection_pool
# import the __main__ object to access the global variables: status, state, arg, loginIdentity
import __main__
import sys
app = QtWidgets.QApplication(sys.argv)

import util
headerDict = {
    0: "Name",
    1: "WaterFeature",
    2: "Size",
    3: "Num"
}

orderDict = {
    0: "ASC",
    1: "DESC"
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 1, 793, 481))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Homebutton = QtWidgets.QPushButton(self.widget)
        self.Homebutton.setMinimumSize(QtCore.QSize(114, 52))
        self.Homebutton.setMaximumSize(QtCore.QSize(114, 52))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.Homebutton.setFont(font)
        self.Homebutton.setObjectName("Homebutton")
        self.gridLayout_3.addWidget(self.Homebutton, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.Heading_exhibit = QtWidgets.QLabel(self.widget)
        self.Heading_exhibit.setMinimumSize(QtCore.QSize(120, 31))
        self.Heading_exhibit.setMaximumSize(QtCore.QSize(120, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(22)
        self.Heading_exhibit.setFont(font)
        self.Heading_exhibit.setObjectName("Heading_exhibit")
        self.gridLayout_3.addWidget(self.Heading_exhibit, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 4, 1, 2)
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setMinimumSize(QtCore.QSize(175, 23))
        self.label_title.setMaximumSize(QtCore.QSize(175, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.gridLayout_3.addWidget(self.label_title, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(651, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setMinimumSize(QtCore.QSize(83, 37))
        self.label_name.setMaximumSize(QtCore.QSize(83, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(158, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 2)
        self.label_sizemin = QtWidgets.QLabel(self.widget)
        self.label_sizemin.setMinimumSize(QtCore.QSize(37, 16))
        self.label_sizemin.setMaximumSize(QtCore.QSize(37, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_sizemin.setFont(font)
        self.label_sizemin.setObjectName("label_sizemin")
        self.gridLayout.addWidget(self.label_sizemin, 1, 1, 1, 1)
        self.label_sizemax = QtWidgets.QLabel(self.widget)
        self.label_sizemax.setMinimumSize(QtCore.QSize(36, 16))
        self.label_sizemax.setMaximumSize(QtCore.QSize(36, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_sizemax.setFont(font)
        self.label_sizemax.setObjectName("label_sizemax")
        self.gridLayout.addWidget(self.label_sizemax, 1, 2, 1, 1)
        self.label_size = QtWidgets.QLabel(self.widget)
        self.label_size.setMinimumSize(QtCore.QSize(78, 35))
        self.label_size.setMaximumSize(QtCore.QSize(78, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_size.setFont(font)
        self.label_size.setObjectName("label_size")
        self.gridLayout.addWidget(self.label_size, 2, 0, 1, 1)
        self.spinBox_minsize = QtWidgets.QSpinBox(self.widget)
        self.spinBox_minsize.setMinimumSize(QtCore.QSize(66, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.spinBox_minsize.setFont(font)
        self.spinBox_minsize.setObjectName("spinBox_minsize")
        self.gridLayout.addWidget(self.spinBox_minsize, 2, 1, 1, 1)
        self.spinBox_maxsize = QtWidgets.QSpinBox(self.widget)
        self.spinBox_maxsize.setMinimumSize(QtCore.QSize(69, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.spinBox_maxsize.setFont(font)
        self.spinBox_maxsize.setMaximum(10000)
        self.spinBox_maxsize.setObjectName("spinBox_maxsize")
        self.gridLayout.addWidget(self.spinBox_maxsize, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 1, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_nummax = QtWidgets.QLabel(self.widget)
        self.label_nummax.setMinimumSize(QtCore.QSize(42, 23))
        self.label_nummax.setMaximumSize(QtCore.QSize(42, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_nummax.setFont(font)
        self.label_nummax.setObjectName("label_nummax")
        self.gridLayout_2.addWidget(self.label_nummax, 0, 2, 1, 1)
        self.label_nummin = QtWidgets.QLabel(self.widget)
        self.label_nummin.setMinimumSize(QtCore.QSize(38, 28))
        self.label_nummin.setMaximumSize(QtCore.QSize(38, 28))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_nummin.setFont(font)
        self.label_nummin.setObjectName("label_nummin")
        self.gridLayout_2.addWidget(self.label_nummin, 0, 1, 1, 1)
        self.label_numanimals = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_numanimals.sizePolicy().hasHeightForWidth())
        self.label_numanimals.setSizePolicy(sizePolicy)
        self.label_numanimals.setMinimumSize(QtCore.QSize(177, 36))
        self.label_numanimals.setMaximumSize(QtCore.QSize(177, 36))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_numanimals.setFont(font)
        self.label_numanimals.setObjectName("label_numanimals")
        self.gridLayout_2.addWidget(self.label_numanimals, 1, 0, 1, 1)
        self.WaterCombo = QtWidgets.QComboBox(self.widget)
        self.WaterCombo.setMinimumSize(QtCore.QSize(127, 33))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.WaterCombo.setFont(font)
        self.WaterCombo.setObjectName("WaterCombo")
        self.WaterCombo.addItem("")
        self.WaterCombo.addItem("")
        self.WaterCombo.addItem("")
        self.gridLayout_2.addWidget(self.WaterCombo, 2, 1, 1, 2)
        self.spinBox_maxnum = QtWidgets.QSpinBox(self.widget)
        self.spinBox_maxnum.setMinimumSize(QtCore.QSize(51, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.spinBox_maxnum.setFont(font)
        self.spinBox_maxnum.setObjectName("spinBox_maxnum")
        self.gridLayout_2.addWidget(self.spinBox_maxnum, 1, 2, 1, 1)
        self.label_waterfeature = QtWidgets.QLabel(self.widget)
        self.label_waterfeature.setMinimumSize(QtCore.QSize(175, 31))
        self.label_waterfeature.setMaximumSize(QtCore.QSize(175, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.label_waterfeature.setFont(font)
        self.label_waterfeature.setObjectName("label_waterfeature")
        self.gridLayout_2.addWidget(self.label_waterfeature, 2, 0, 1, 1)
        self.spinBox_minnum = QtWidgets.QSpinBox(self.widget)
        self.spinBox_minnum.setMinimumSize(QtCore.QSize(52, 35))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.spinBox_minnum.setFont(font)
        self.spinBox_minnum.setObjectName("spinBox_minnum")
        self.gridLayout_2.addWidget(self.spinBox_minnum, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 3, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(343, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 3, 0, 1, 3)
        self.Searchbutton = QtWidgets.QPushButton(self.widget)
        self.Searchbutton.setMinimumSize(QtCore.QSize(117, 37))
        self.Searchbutton.setMaximumSize(QtCore.QSize(117, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(11)
        self.Searchbutton.setFont(font)
        self.Searchbutton.setObjectName("Searchbutton")
        self.gridLayout_3.addWidget(self.Searchbutton, 3, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(289, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 3, 4, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
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
        self.gridLayout_3.addWidget(self.tableWidget, 4, 1, 2, 4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 5, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 6, 3, 1, 1)
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
        self.Heading_exhibit.setText(_translate("MainWindow", "Exhibit"))
        self.label_title.setText(_translate("MainWindow", "Atlanta Zoo"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_sizemin.setText(_translate("MainWindow", "Min"))
        self.label_sizemax.setText(_translate("MainWindow", "Max"))
        self.label_size.setText(_translate("MainWindow", "Size:"))
        self.label_nummax.setText(_translate("MainWindow", "Max"))
        self.label_nummin.setText(_translate("MainWindow", "Min"))
        self.label_numanimals.setText(_translate("MainWindow", "Number of animals:"))
        self.WaterCombo.setItemText(0, _translate("MainWindow", "All"))
        self.WaterCombo.setItemText(1, _translate("MainWindow", "Yes"))
        self.WaterCombo.setItemText(2, _translate("MainWindow", "No"))
        self.label_waterfeature.setText(_translate("MainWindow", "Water feature:"))
        self.Searchbutton.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "WaterFeature"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "NumAnimals"))



    def userDefinedInitialisation(self):
        self.currentOrder = 0
        self.Searchbutton.clicked.connect(self.searchExhibit)
        self.Homebutton.clicked.connect(self.home)
        self.tableWidget.cellClicked.connect(self.highlightRowOrToExhibit)
        header = self.tableWidget.horizontalHeader()
        header.sectionClicked.connect(self.searchExhibit)
        self.spinBox_minsize.setMaximum(9999)
        self.spinBox_maxsize.setMaximum(9999)
        self.spinBox_minnum.setMaximum(9999)
        self.spinBox_maxnum.setMaximum(9999)
        self.searchExhibit()

    def searchExhibit(self, column = 0):
        Name = self.lineEdit_name.text()
        MaxSize = self.spinBox_maxsize.value()
        MinSize = self.spinBox_minsize.value()
        MaxNum= self.spinBox_maxnum.value()
        MinNum= self.spinBox_minnum.value()
        WaterFeature= self.WaterCombo.currentText()
        
        if(WaterFeature=="All"):
            WaterFeature=""
        if(WaterFeature=="Yes"):
            WaterFeature="True"
        if(WaterFeature=="No"):
            WaterFeature="False"
        if(MaxSize==0 and MinSize==0 ):
            MaxSize=''
            MinSize=''
        if(MaxNum==0 and MinNum==0):
            MaxNum=''
            MinNum=''
        
                

        cmd1= "SELECT * FROM (SELECT E.Name as Name, WaterFeature, Size, COUNT(*) as Num FROM EXHIBIT as E, ANIMAL as A"
        
        AExhibit = "A.Exhibit"
        listTuple1 = [("E.Name", AExhibit, "var"), ("E.name", Name,"str"),("WaterFeature",WaterFeature, "bool"), ("MinSize",MinSize,"int"),("MaxSize", MaxSize, "int")]
        
        cmd1 = util.addWHERE(cmd1, listTuple1)
        
        cmd1 += " GROUP BY E.Name) as t1"
        
        
        listTuple2=[("MinNum", MinNum,"int"),("MaxNum", MaxNum,"int")]
        cmd1 = util.addWHERE(cmd1, listTuple2)
        cmd1 += " order by " + headerDict[column] + " " + orderDict[self.currentOrder] + ";"
        if(self.currentOrder == 0):
            self.currentOrder = 1
        else: 
            self.currentOrder = 0

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
                # first you must determine in which column does the DateTime attribute occur in your
                # query
                
                cellContent = None
                if(column_num == 1):
                    if(data == 0):
                        cellContent = "No"
                    else:
                        cellContent = "Yes"
                if(cellContent is None):
                    cellContent = str(data)
                self.tableWidget.setItem(row_num, column_num, QtWidgets.QTableWidgetItem(cellContent))




        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
            print("MySQL connection is closed")

                
                
    def highlightRowOrToExhibit(self, row, column):
        # highlight the row selected
        self.tableWidget.selectRow(row)
        # Enter IF statement if the selected column is the exhibit column
        if(column == 0):
            # retrieve the content in the cell
            Name = str(self.tableWidget.item(row,column).text())
            # store the information into the __main__.arg
            # the information is later passed to the exhibitDetails page
            __main__.arg = [("Name", Name, "str")]
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



