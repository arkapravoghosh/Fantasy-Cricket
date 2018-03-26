# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Team_Evaluation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

selectedteam = 'Select Team'
selectedmatch = 'Select Match'



class Ui_evaluate_team(object):
    def CalculatePlayerScore(self, l):
        """
        INPUT: A tuple containing the stats of a player
        OUTPUT: An integer denoting the score of the player
        """
        
        #INITIALIZE ALL THE VARIABLES REQUIRED TO CALCULATE THE SCORE
        score = 0
        name = l[0]
        runsscored = l[1]
        ballsfaced = l[2]
        fours = l[3]
        sixes = l[4]
        bowled = l[5]
        runsgiven = l[6]
        wickets = l[7]
        catches = l[8]
        stumpings = l[9]
        runouts = l[10]
        
        #CALCULATE THE BATTING SCORES
        score += runsscored//2
        if runsscored >= 50:
            score += 5
        if runsscored >= 100:
            score += 10
        if ballsfaced > 0:
            strike_rate = (runsscored / ballsfaced) * 100
            if strike_rate > 100:
                score += 4
            elif strike_rate >= 80:
                score += 2
        score += fours + (2 * sixes)
                        
        #CALCULATE THE BOLWLNG SCORES
        score += (10 * wickets)
        if wickets >= 3:
            score += 5
        if wickets >= 5:
            score += 10
        if bowled > 0:
            economy_rate = (runsgiven / bowled) * 6
            if economy_rate >= 3.5 and economy_rate <= 4.5:
                score += 4
            elif economy_rate >= 2 and economy_rate < 3.5:
                score += 7
            elif economy_rate < 2:
                score += 10
            
        #CALCULATE THE FIELDING SCORES
        score += 10 * (catches + stumpings + runouts)
        
        #DISPLAY THE SCORES OF THE PLAYERS
        self.players.addItem("{}".format(name));
        self.scores.addItem("{}".format(str(score)));
        return score



    def CalculateMatchScore(self):
        """
        INPUT: The Team Name and Match no.
        OUTPUT: The total SCORE of the TEAM in the given MATCH
        """
        _translate = QtCore.QCoreApplication.translate
        global selectedteam
        global selectedmatch
        self.players.clear()
        self.scores.clear()
        conn = sqlite3.connect('Matches.db')
        c = conn.cursor()
        totalscore = 0
        c.execute("SELECT * from Teams WHERE teamname = ?", (selectedteam,))
        t = c.fetchone()
        t = t[1:]
        for i in t:
            c.execute("SELECT * from {} WHERE name = ?".format(selectedmatch), (i,))
            l = c.fetchone()
            totalscore += self.CalculatePlayerScore(l)
        self.points.setText(_translate("evaluate_team", "{}".format(str(totalscore))))
        c.close()
        conn.close()
        
        
        
    def TeamChanged(self):
        global selectedteam
        global selectedmatch
        _translate = QtCore.QCoreApplication.translate
        selectedteam = self.select_team.currentText()
        selectedmatch = self.select_match.currentText()
        if selectedteam != 'Select Team' and selectedmatch != 'Select Match':
            self.Evaluate_btn.setEnabled(True)
            self.players.clear()
            self.scores.clear()
            self.points.setText(_translate("evaluate_team", "0"))
        else:
            self.Evaluate_btn.setEnabled(False)
            
            
            
    def MatchChanged(self):
        global selectedteam
        global selectedmatch
        _translate = QtCore.QCoreApplication.translate
        selectedmatch = self.select_match.currentText()
        selectedteam = self.select_team.currentText()
        if selectedmatch != 'Select Match' and selectedteam != 'Select Team':
            self.Evaluate_btn.setEnabled(True)
            self.players.clear()
            self.scores.clear()
            self.points.setText(_translate("evaluate_team", "0"))
        else:
            self.Evaluate_btn.setEnabled(False)
        
        
        
    def setupUi(self, evaluate_team):
        evaluate_team.setObjectName("evaluate_team")
        evaluate_team.resize(633, 452)
        self.label = QtWidgets.QLabel(evaluate_team)
        self.label.setGeometry(QtCore.QRect(130, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.select_team = QtWidgets.QComboBox(evaluate_team)
        self.select_team.setGeometry(QtCore.QRect(90, 70, 141, 21))
        self.select_team.setFont(font)
        self.select_team.setCurrentText("Select Team")
        self.select_team.setObjectName("select_team")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.select_match = QtWidgets.QComboBox(evaluate_team)
        self.select_match.setGeometry(QtCore.QRect(360, 70, 141, 22))
        self.select_match.setFont(font)
        self.select_match.setCurrentText("Select Match")
        self.select_match.setObjectName("select_match")
        ''''''
        conn = sqlite3.connect('Matches.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Teams")
        l = c.fetchall()
        list1 = ['Select Team']
        for teamname in l:
            list1.append(teamname[0])
        
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        l = c.fetchall()
        list2 = ['Select Match']
        for matchname in l:
            if matchname[0].startswith('Match'):
                list2.append(matchname[0])
        c.close()
        conn.close()
        ''''''
        ''''''
        self.select_team.addItems(list1)
        self.select_match.addItems(list2)
        ''''''
        ''''''
        self.select_team.activated.connect(self.TeamChanged)
        self.select_match.activated.connect(self.MatchChanged)
        ''''''
        self.line = QtWidgets.QFrame(evaluate_team)
        self.line.setGeometry(QtCore.QRect(40, 95, 551, 41))
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(evaluate_team)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(evaluate_team)
        self.label_3.setGeometry(QtCore.QRect(340, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.points = QtWidgets.QLabel(evaluate_team)
        self.points.setGeometry(QtCore.QRect(390, 160, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.points.setFont(font)
        self.points.setStyleSheet("color: rgb(7, 200, 168);")
        self.points.setObjectName("points")
        self.Evaluate_btn = QtWidgets.QPushButton(evaluate_team)
        self.Evaluate_btn.setEnabled(False)
        self.Evaluate_btn.setGeometry(QtCore.QRect(240, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Evaluate_btn.setFont(font)
        self.Evaluate_btn.setObjectName("Evaluate_btn")
        ''''''
        self.Evaluate_btn.clicked.connect(self.CalculateMatchScore)
        ''''''
        self.players = QtWidgets.QListWidget(evaluate_team)
        self.players.setGeometry(QtCore.QRect(80, 180, 191, 221))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.players.setFont(font)
        self.players.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.players.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.players.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.players.setObjectName("players")
        self.scores = QtWidgets.QListWidget(evaluate_team)
        self.scores.setGeometry(QtCore.QRect(340, 180, 191, 221))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scores.setFont(font)
        self.scores.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scores.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.scores.setObjectName("scores")

        self.retranslateUi(evaluate_team)
        QtCore.QMetaObject.connectSlotsByName(evaluate_team)

    def retranslateUi(self, evaluate_team):
        _translate = QtCore.QCoreApplication.translate
        evaluate_team.setWindowTitle(_translate("evaluate_team", "Dialog"))
        self.label.setText(_translate("evaluate_team", "Evaluate the Performance of your Fantasy Team"))
        self.label_2.setText(_translate("evaluate_team", "Players"))
        self.label_3.setText(_translate("evaluate_team", "Points"))
        self.points.setText(_translate("evaluate_team", "####"))
        self.Evaluate_btn.setText(_translate("evaluate_team", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate_team = QtWidgets.QDialog()
    ui = Ui_evaluate_team()
    ui.setupUi(evaluate_team)
    evaluate_team.show()
    sys.exit(app.exec_())

