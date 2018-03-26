# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_Team.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3



class Ui_NewTeam(object):
    def CheckName(self):
        teamname = self.team_name.text()
        teamname = teamname.strip()
        conn = sqlite3.connect('Matches.db')
        c = conn.cursor()
        c.execute("DELETE FROM Teams WHERE player1 = ''")
        conn.commit()
        c.close()
        conn.close()
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
        elif teamname == 'Enter name here':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a teamname!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
        else:
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            c.execute("SELECT * FROM Teams")
            l = c.fetchall()
            flag = 0
            for i in l:
                if i[0] == teamname:
                    flag = 1
                    break
            if flag == 0:
                c.execute("""INSERT INTO Teams VALUES (?, '', '', '', '', '', '', '', '', '', '', '')""", (teamname,))
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team Created Successfully!!!\nNow go back to the previous window and select the players.")
                msg.setWindowTitle("Team Created")
                msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name aleady exists!!\nPlease choose another name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
            conn.commit()
            c.close()
            conn.close()


    
    def setupUi(self, NewTeam):
        NewTeam.setObjectName("NewTeam")
        NewTeam.resize(400, 300)
        self.label = QtWidgets.QLabel(NewTeam)
        self.label.setGeometry(QtCore.QRect(100, 30, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(NewTeam)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.team_name = QtWidgets.QLineEdit(NewTeam)
        self.team_name.setGeometry(QtCore.QRect(140, 150, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.team_name.setFont(font)
        self.team_name.setObjectName("team_name")
        self.pushButton = QtWidgets.QPushButton(NewTeam)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        ''''''
        self.pushButton.clicked.connect(self.CheckName)
        ''''''
        
        self.retranslateUi(NewTeam)
        QtCore.QMetaObject.connectSlotsByName(NewTeam)

    def retranslateUi(self, NewTeam):
        _translate = QtCore.QCoreApplication.translate
        NewTeam.setWindowTitle(_translate("NewTeam", "Create New Team"))
        self.label.setText(_translate("NewTeam", "New Team"))
        self.label_2.setText(_translate("NewTeam", "Team Name"))
        self.team_name.setText(_translate("NewTeam", "Enter name here"))
        self.pushButton.setText(_translate("NewTeam", "Create Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewTeam = QtWidgets.QDialog()
    ui = Ui_NewTeam()
    ui.setupUi(NewTeam)
    NewTeam.show()
    sys.exit(app.exec_())

