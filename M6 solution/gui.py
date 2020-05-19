# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 350)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(192, 61, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setGeometry(QtCore.QRect(190, 190, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t3.setFont(font)
        self.t3.setObjectName("t3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 230, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(190, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t2.setFont(font)
        self.t2.setStyleSheet("color:blue;\n"
"border:none")
        self.t2.setObjectName("t2")
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setGeometry(QtCore.QRect(190, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.t4.setFont(font)
        self.t4.setStyleSheet("color:blue;\n"
"border:none")
        self.t4.setObjectName("t4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 140, 411, 20))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(450, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("border:1px solid black;\n"
"background-color:#D3D3D3")
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.FindPrice)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(450, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("border:1px solid black;\n"
"background-color:#D3D3D3")
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.FindTotal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Window Title"))
        self.label.setText(_translate("MainWindow", "Book Title:"))
        self.label_3.setText(_translate("MainWindow", "Quantity:"))
        self.label_2.setText(_translate("MainWindow", "Price :"))
        self.t1.setPlaceholderText(_translate("MainWindow", "text"))
        self.t3.setPlaceholderText(_translate("MainWindow", "text"))
        self.label_4.setText(_translate("MainWindow", "Total :"))
        self.t2.setText(_translate("MainWindow", "Rs. 0"))
        self.t2.setPlaceholderText(_translate("MainWindow", "text"))
        self.t4.setText(_translate("MainWindow", "Rs. 0"))
        self.t4.setPlaceholderText(_translate("MainWindow", "text"))
        self.btn1.setText(_translate("MainWindow", "Find Price"))
        self.btn2.setText(_translate("MainWindow", "Find Total"))
        
    def FindPrice(self):
        book=sqlite3.connect('bookstore.db')
        curbook=book.cursor()
        title=self.t1.text()
        sql="select * from books where book_name='"+title+"';"
        x=curbook.execute(sql)

        if x!=None:
            #curbook.execute(sql)
            y=curbook.fetchone()
            
            price=(y[3])
            self.t2.setText(str(price))
        else:
            self.t2.setText("Book not found")

    def FindTotal(self):
        book=sqlite3.connect('bookstore.db')
        curbook=book.cursor()        
        qnty=int(self.t3.text())
        title=self.t1.text()
        sql="select * from books where book_name='"+title+"';"
        curbook.execute(sql)
        y=curbook.fetchone()
            
        price=(y[3])        
        self.t4.setText(str(price*qnty))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

