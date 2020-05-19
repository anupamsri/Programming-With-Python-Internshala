# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(900, 675)
		MainWindow.move(100,10)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		MainWindow.setAutoFillBackground(False)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_5.addItem(spacerItem)
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setEnabled(False)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_5.addWidget(self.label_4)
		self.e1 = QtWidgets.QLineEdit(self.centralwidget)
		self.e1.setEnabled(False)
		self.e1.setObjectName("e1")
		self.horizontalLayout_5.addWidget(self.e1)
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setEnabled(False)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.horizontalLayout_5.addWidget(self.label_6)
		self.e2 = QtWidgets.QLineEdit(self.centralwidget)
		self.e2.setEnabled(False)
		self.e2.setObjectName("e2")
		self.horizontalLayout_5.addWidget(self.e2)
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setEnabled(False)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_7.setFont(font)
		self.label_7.setObjectName("label_7")
		self.horizontalLayout_5.addWidget(self.label_7)
		self.e3 = QtWidgets.QLineEdit(self.centralwidget)
		self.e3.setEnabled(False)
		self.e3.setObjectName("e3")
		self.horizontalLayout_5.addWidget(self.e3)
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setEnabled(False)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_8.setFont(font)
		self.label_8.setObjectName("label_8")
		self.horizontalLayout_5.addWidget(self.label_8)
		self.e4 = QtWidgets.QLineEdit(self.centralwidget)
		self.e4.setEnabled(False)
		self.e4.setObjectName("e4")
		self.horizontalLayout_5.addWidget(self.e4)
		spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_5.addItem(spacerItem1)
		self.horizontalLayout.addLayout(self.horizontalLayout_5)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayout.addWidget(self.line)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem2)
		self.verticalLayout_8 = QtWidgets.QVBoxLayout()
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.label = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.verticalLayout_8.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setTitle("")
		self.groupBox.setFlat(False)
		self.groupBox.setCheckable(False)
		self.groupBox.setObjectName("groupBox")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.rb1 = QtWidgets.QRadioButton(self.groupBox)
		self.rb1.setObjectName("rb1")
		self.horizontalLayout_4.addWidget(self.rb1)
		self.rb2 = QtWidgets.QRadioButton(self.groupBox)
		self.rb2.setObjectName("rb2")
		self.horizontalLayout_4.addWidget(self.rb2)
		self.rb3 = QtWidgets.QRadioButton(self.groupBox)
		self.rb3.setObjectName("rb3")
		self.horizontalLayout_4.addWidget(self.rb3)
		self.rb4 = QtWidgets.QRadioButton(self.groupBox)
		self.rb4.setObjectName("rb4")
		self.horizontalLayout_4.addWidget(self.rb4)		
		self.rb1.toggled.connect(self.ctg)
		self.rb2.toggled.connect(self.ctg)
		self.rb3.toggled.connect(self.ctg)
		self.rb4.toggled.connect(self.ctg) 
		self.verticalLayout_8.addWidget(self.groupBox)
		self.list1 = QtWidgets.QListWidget(self.centralwidget)
		self.list1.setAutoFillBackground(True)
		self.list1.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
		self.list1.setAutoScroll(True)
		self.list1.setObjectName("list1")
		self.list1.itemDoubleClicked.connect(self.removelist1)
		self.verticalLayout_8.addWidget(self.list1)
		self.btn1 = QtWidgets.QPushButton(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.btn1.setFont(font)
		self.btn1.setObjectName("btn1")
		self.verticalLayout_8.addWidget(self.btn1)
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setText("")
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.verticalLayout_8.addWidget(self.label_5)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout_2.addLayout(self.verticalLayout_2)
		self.verticalLayout_8.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_3.addLayout(self.verticalLayout_8)
		spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem3)
		self.verticalLayout_9 = QtWidgets.QVBoxLayout()
		self.verticalLayout_9.setObjectName("verticalLayout_9")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_9.addWidget(self.label_2)
		self.l1 = QtWidgets.QLabel(self.centralwidget)
		self.l1.setEnabled(True)
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(9)
		self.l1.setFont(font)
		self.l1.setAlignment(QtCore.Qt.AlignCenter)
		self.l1.setObjectName("l1")
		self.verticalLayout_9.addWidget(self.l1)
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.verticalLayout_9.addWidget(self.line_2)
		spacerItem4 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		self.verticalLayout_9.addItem(spacerItem4)
		self.list2 = QtWidgets.QListWidget(self.centralwidget)
		self.list2.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
		self.list2.setObjectName("list2")
		self.list2.itemDoubleClicked.connect(self.removelist2)        
		self.verticalLayout_9.addWidget(self.list2)
		self.btn2 = QtWidgets.QPushButton(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.btn2.setFont(font)
		self.btn2.setObjectName("btn2")
		self.verticalLayout_9.addWidget(self.btn2)
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setText("")
		self.label_3.setPixmap(QtGui.QPixmap("dream1.png"))
		self.label_3.setObjectName("label_3")
		self.verticalLayout_9.addWidget(self.label_3)
		self.horizontalLayout_3.addLayout(self.verticalLayout_9)
		spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem5)
		self.verticalLayout.addLayout(self.horizontalLayout_3)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionNew = QtWidgets.QAction(MainWindow)
		self.actionNew.setObjectName("actionNew")
		self.actionOpen = QtWidgets.QAction(MainWindow)
		self.actionOpen.setObjectName("actionOpen")
		self.actionSave_Team = QtWidgets.QAction(MainWindow)
		self.actionSave_Team.setObjectName("actionSave_Team")
		self.actionRules = QtWidgets.QAction(MainWindow)
		self.actionRules.setObjectName("actionRules")
		self.actionInstructions = QtWidgets.QAction(MainWindow)
		self.actionInstructions.setObjectName("actionInstructions")
		self.actionQuit = QtWidgets.QAction(MainWindow)
		self.actionQuit.setObjectName("actionQuit")
		self.menuFile.addAction(self.actionNew)
		self.menuFile.addAction(self.actionOpen)
		self.menuFile.addAction(self.actionSave_Team)
		self.menuFile.addAction(self.actionQuit)
		self.menuFile.triggered[QtWidgets.QAction].connect(self.menufunction)
		self.menubar.addAction(self.menuFile.menuAction())
		self.bat=0
		self.bwl=0
		self.ar=0
		self.wk=0
		self.avl=1000
		self.used=0
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		MainWindow.customContextMenuRequested.connect(self.context_menu)
	
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket Game"))
		self.label_4.setText(_translate("MainWindow", "Batsmen"))
		self.label_6.setText(_translate("MainWindow", "Bowlers"))
		self.label_7.setText(_translate("MainWindow", "All Rounders"))
		self.label_8.setText(_translate("MainWindow", "Wicketkeepers"))
		self.label.setText(_translate("MainWindow", "Player Categories"))
		self.rb1.setText(_translate("MainWindow", "BAT"))
		self.rb2.setText(_translate("MainWindow", "BOWL"))
		self.rb3.setText(_translate("MainWindow", "AR"))
		self.rb4.setText(_translate("MainWindow", "WK"))
		self.btn1.setText(_translate("MainWindow", "Available Points : 1000"))
		self.label_2.setText(_translate("MainWindow", "Selected Players"))
		self.l1.setText(_translate("MainWindow", "Team_name"))
		self.btn2.setText(_translate("MainWindow", "Points used : "))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.actionNew.setText(_translate("MainWindow", "NEW Team"))
		self.actionOpen.setText(_translate("MainWindow", "OPEN Team"))
		self.actionSave_Team.setText(_translate("MainWindow", "SAVE Team"))
		self.actionQuit.setText(_translate("MainWindow", "EVALUATE Team"))
	
	def menufunction(self, action):
		txt=action.text()
		if txt=="NEW Team":
			self.bat=0
			self.bwl=0
			self.ar=0
			self.wk=0
			self.avl=1000
			self.used=0
			self.list1.clear()
			self.list2.clear()
			self.l1.setText("Team_name")
			self.showstatus()
			text, ok = QtWidgets.QInputDialog.getText(MainWindow, 'Fantasy Cricket Game', 'Enter name of team:')
			if ok:
				self.l1.setText(str(text))
		if txt=='SAVE Team':
			selected=""
			count=self.list2.count()
			for i in range(count):
				selected=selected+self.list2.item(i).text()
				if i<count-1:
					selected=selected+","
			self.save_Team(self.l1.text(),selected,self.used)
		if txt=="OPEN Team":
			self.bat=0
			self.bwl=0
			self.ar=0
			self.wk=0
			self.avl=1000
			self.used=0
			self.list1.clear()
			self.list2.clear()
			self.l1.setText("Team_name")
			self.showstatus()
			self.open_Team()
		if txt=="EVALUATE Team":
			from evaluateTeam import Mini_Ui
			Dialog = QtWidgets.QDialog()
			ui = Mini_Ui()
			ui.setupUi(Dialog)
			ret=Dialog.exec()

	def save_Team(self,nm,string,val):
		if self.bat+self.bwl+self.ar+self.wk!=11:
			self.showdlg("Insufficient players")
			return
		sql="INSERT INTO teams (name, players, value) VALUES ('"+nm+"','"+string+"','"+str(val)+"');"
		try:
			cur=conn.execute(sql)
			conn.commit()
			self.showdlg ("Team Saved successfully")
		except:
			self.showdlg ("error in operation")
			conn.rollback()

	def open_Team(self):
		sql="select name from teams"
		cur=conn.execute(sql)
		teams=[]
		for row in cur:
			teams.append(row[0])
		team, ok = QtWidgets.QInputDialog.getItem(MainWindow, "Fantasy Cricket Game",
				"Choose a team", teams, 0, False)
		if ok and team:
			self.l1.setText(team)
		sql1="select players, value from teams where name='"+team+"'"
		cur=conn.execute(sql1)
		row=cur.fetchone()
		selected=row[0].split(',')
		self.list2.addItems(selected)
		self.used=row[1]
		self.avl=1000-row[1]
		count=self.list2.count()
		for i in range(count):
			player=self.list2.item(i).text()
			sql="select ctg from stats where player='"+player+"'"
			cur=conn.execute(sql)
			row=cur.fetchone()
			ctgr=row[0]
			if ctgr=="BAT":self.bat+=1
			if ctgr=="BWL":self.bwl+=1
			if ctgr=="AR":self.ar+=1
			if ctgr=="WK":self.wk+=1            			
		self.showstatus()

	def context_menu(MainWindow):
		MainWindow.menu = QtWidgets.QMenu()
		

	def fillList(self,ctgr):
		if self.l1.text()=='Team_name':
			self.showdlg("Enter name of team")
			return
		self.list1.clear()
		cursor = conn.execute("SELECT player from stats where ctg='"+ctgr+"'")
		for row in cursor:
			selected=[]
			for i in range(self.list2.count()):
				selected.append(self.list2.item(i).text())
			if row[0] not in selected:self.list1.addItem(row[0])

	def ctg(self):
		ctgr=''
		if self.rb1.isChecked()==True:ctgr='BAT'
		if self.rb2.isChecked()==True:ctgr='BWL'
		if self.rb3.isChecked()==True:ctgr='AR'
		if self.rb4.isChecked()==True:ctgr='WK'
		self.fillList(ctgr)
	
	def criteria(self,ctgr, item):
		msg=''
		if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"
		if ctgr=="BWL" and self.bwl>=5:msg="bowlers not more than 5"
		if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
		if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
		if msg!='' or self.avl<=0:
			msg = 'You have exhausted your points'
			self.showdlg(msg)
			return False
		if ctgr=="BAT":self.bat+=1
		if ctgr=="BWL":self.bwl+=1
		if ctgr=="AR":self.ar+=1
		if ctgr=="WK":self.wk+=1
		cursor = conn.execute("SELECT player,value from stats where player='"+item.text()+"'")
		row=cursor.fetchone()
		self.avl=self.avl-int(row[1])
		self.used=self.used+int(row[1])
		return True
			
	def showstatus(self):
		self.e1.setText(str(self.bat))
		self.e2.setText(str(self.bwl))
		self.e3.setText(str(self.ar))
		self.e4.setText(str(self.wk))
		self.btn1.setText("Available Points : {}".format(self.avl))
		self.btn2.setText("Points used : {}".format(self.used))
		
	def removelist1(self, item):
		ctgr=''
		if self.rb1.isChecked()==True:ctgr='BAT'
		if self.rb2.isChecked()==True:ctgr='BWL'
		if self.rb3.isChecked()==True:ctgr='AR'
		if self.rb4.isChecked()==True:ctgr='WK'
		ret=self.criteria(ctgr, item)
		if ret==True:                         
			self.list1.takeItem(self.list1.row(item))
			self.list2.addItem(item.text())
			self.showstatus()
						 
	def showdlg(self, msg):
		Dialog = QtWidgets.QMessageBox()
		Dialog.setText(msg)
		Dialog.setWindowTitle("Fantasy Cricket Game")
		ret=Dialog.exec()                         

	def removelist2(self, item):
		self.list2.takeItem(self.list2.row(item))
		cursor = conn.execute("SELECT player,value, ctg from stats where player='"+item.text()+"'")
		row=cursor.fetchone()
		self.avl=self.avl+int(row[1])
		self.used=self.used-int(row[1])
		ctgr=row[2]
		if ctgr=="BAT":
			self.bat-=1
			if self.rb1.isChecked()==True:self.list1.addItem(item.text())
		if ctgr=="BWL":
			self.bwl-=1
			if self.rb2.isChecked()==True:self.list1.addItem(item.text())
		if ctgr=="AR":
			self.ar-=1
			if self.rb3.isChecked()==True:self.list1.addItem(item.text())
		if ctgr=="WK":
			self.wk-=1
			if self.rb4.isChecked()==True:self.list1.addItem(item.text())
		self.showstatus()
	
if __name__ == "__main__":
	import sqlite3
	conn = sqlite3.connect('fantasy.db')    
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
	conn.close()