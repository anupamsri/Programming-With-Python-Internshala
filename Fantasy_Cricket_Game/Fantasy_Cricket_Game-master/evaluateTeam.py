# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluateTeam.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Mini_Ui(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Fantasy Cricket Game")
		Dialog.resize(500, 400)
		self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
		self.verticalLayout.setContentsMargins(25, -1, 25, -1)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_2 = QtWidgets.QLabel(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout.addWidget(self.label_2)
		self.cb0 = QtWidgets.QComboBox(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.cb0.setFont(font)
		self.cb0.setObjectName("cb0")
		import sqlite3
		conn = sqlite3.connect('fantasy.db')
		self.horizontalLayout.addWidget(self.cb0)
		sql="select name from teams"
		cur=conn.execute(sql)
		teams=[]
		for row in cur:
			self.cb0.addItem(row[0])        
		conn.close()
		self.label = QtWidgets.QLabel(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.cb1 = QtWidgets.QComboBox(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.cb1.setFont(font)
		self.cb1.setObjectName("cb1")
		self.cb1.addItem("")
		self.cb1.addItem("")
		self.cb1.addItem("")
		self.cb1.addItem("")
		self.cb1.addItem("")
		self.horizontalLayout.addWidget(self.cb1)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.line = QtWidgets.QFrame(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.line.setFont(font)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayout.addWidget(self.line)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label_5 = QtWidgets.QLabel(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_5.setFont(font)
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout_4.addWidget(self.label_5)
		self.label_4 = QtWidgets.QLabel(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_4.addWidget(self.label_4)
		self.verticalLayout.addLayout(self.horizontalLayout_4)
		self.line_2 = QtWidgets.QFrame(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.line_2.setFont(font)
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.verticalLayout.addWidget(self.line_2)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.lw1 = QtWidgets.QListWidget(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.lw1.setFont(font)
		self.lw1.setObjectName("lw1")
		self.horizontalLayout_2.addWidget(self.lw1)
		spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem)
		self.lw2 = QtWidgets.QListWidget(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.lw2.setFont(font)
		self.lw2.setObjectName("lw2")
		self.horizontalLayout_2.addWidget(self.lw2)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.line_3 = QtWidgets.QFrame(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.line_3.setFont(font)
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.verticalLayout.addWidget(self.line_3)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.pushButton = QtWidgets.QPushButton(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.evaluate)
		self.horizontalLayout_3.addWidget(self.pushButton)
		spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem1)
		self.scorelabel = QtWidgets.QLabel(Dialog)
		font = QtGui.QFont()
		font.setFamily("Tahoma")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.scorelabel.setFont(font)
		self.scorelabel.setObjectName("scorelabel")
		self.horizontalLayout_3.addWidget(self.scorelabel)
		self.verticalLayout.addLayout(self.horizontalLayout_3)
		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def evaluate(self):
		import sqlite3
		conn = sqlite3.connect('fantasy.db')
		team=self.cb0.currentText()
		self.lw1.clear()
		sql1="select players, value from teams where name='"+team+"'"
		cur=conn.execute(sql1)
		row=cur.fetchone()
		selected=row[0].split(',')
		self.lw1.addItems(selected)
		teamttl=0
		self.lw2.clear()
		match=self.cb1.currentText()
		for i in range(self.lw1.count()):
			ttl, batscore, bowlscore, fieldscore=0,0,0,0
			nm=self.lw1.item(i).text()
			cursor=conn.execute("select * from "+match+" where player='"+nm+"'")
			row=cursor.fetchone()
			batscore=int(row[1]/2)
			if batscore>=50: batscore+=5
			if batscore>=100: batscore+=10
			if row[1]>0:
				sr=row[1]/row[2]
				if sr>=80 and sr<100: batscore+=2
				if sr>=100:batscore+=4
			batscore=batscore+row[3]
			batscore=batscore+2*row[4]
			bowlscore=row[8]*10
			if row[8]>=3: bowlscore=bowlscore+5
			if row[8]>=5: bowlscore=bowlscore=bowlscore+10
			if row[7]>0:
				er=6*row[7]/row[5]
				if er<=2: bowlscore=bowlscore+10
				if er>2 and er<=3.5: bowlscore=bowlscore+7
				if er>3.5 and er<=4.5: bowlscore=bowlscore+4
			fieldscore=(row[9]+row[10]+row[11])*10            
			ttl=batscore+bowlscore+fieldscore
			self.lw2.addItem(str(ttl))
			teamttl=teamttl+ttl
		self.scorelabel.setText(str(teamttl))

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Fantasy Cricket Game"))
		self.label_2.setText(_translate("Dialog", "Choose Team"))
		self.label.setText(_translate("Dialog", "Choose Match"))
		self.cb1.setItemText(0, _translate("Dialog", "Match1"))
		self.label_5.setText(_translate("Dialog", "Players"))
		self.label_4.setText(_translate("Dialog", "Score"))
		self.pushButton.setText(_translate("Dialog", "Evaluate Score"))
		self.scorelabel.setText(_translate("Dialog", "---"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Dialog = QtWidgets.QDialog()
	ui = Mini_Ui()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())