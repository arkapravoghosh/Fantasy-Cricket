# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Open_Team.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

selectedteam = 'Select Team'


class Ui_Dialog(object):
    def TeamChanged(self):
        global selectedteam
        selectedteam = self.select_team.currentText()
        if selectedteam == 'Select Team':
            self.players.clear()
            self.category.clear()
            self.value.clear()
        else:
            self.players.clear()
            self.category.clear()
            self.value.clear()
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            c.execute("SELECT * FROM PlayerDetails")
            playerdetails = c.fetchall()
            c.execute("SELECT * FROM Teams WHERE teamname = ?", (selectedteam,))
            l = c.fetchone()
            teamplayers = []
            for i in range(1,12):
                teamplayers.append(l[i])
            for i in teamplayers:
                name = i
                for j in playerdetails:
                    if j[0] == name:
                        cat = j[1]
                        val = j[2]
                        break
                self.players.addItem("{}".format(name));
                self.category.addItem("{}".format(cat));
                self.value.addItem("{}".format(val));
            c.close()
            conn.close()
            
            
            
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 449)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 30, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(50, 60, 421, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.select_team = QtWidgets.QComboBox(Dialog)
        self.select_team.setGeometry(QtCore.QRect(180, 90, 161, 31))
        self.select_team.setFont(font)
        self.select_team.setObjectName("select_team")
        ''''''
        conn = sqlite3.connect('Matches.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Teams")
        l = c.fetchall()
        list1 = ['Select Team']
        for teamname in l:
            list1.append(teamname[0])
        c.close()
        conn.close()
        self.select_team.addItems(list1)
        self.select_team.activated.connect(self.TeamChanged)
        ''''''
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.players = QtWidgets.QListWidget(Dialog)
        self.players.setGeometry(QtCore.QRect(30, 170, 171, 261))
        self.players.setFont(font)
        self.players.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.players.setObjectName("players")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.category = QtWidgets.QListWidget(Dialog)
        self.category.setGeometry(QtCore.QRect(220, 170, 131, 261))
        self.category.setFont(font)
        self.category.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.category.setObjectName("category")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.value = QtWidgets.QListWidget(Dialog)
        self.value.setGeometry(QtCore.QRect(370, 170, 121, 261))
        self.value.setFont(font)
        self.value.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.value.setObjectName("value")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Open Team"))
        self.label.setText(_translate("Dialog", "Select Team To View Players"))
        self.label_2.setText(_translate("Dialog", "Players"))
        self.label_3.setText(_translate("Dialog", "Category"))
        self.label_4.setText(_translate("Dialog", "Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

