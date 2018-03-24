# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantasy_Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from New_Team import Ui_NewTeam
from Open_Team import Ui_Dialog
from Team_Evaluation import Ui_evaluate_team
import sqlite3

Team_name = 'Enter name here'
PointsAvailable = 1000
PointsUsed = 0
no_of_bat = 0
no_of_bwl = 0
no_of_ar = 0
no_of_wk = 0
AllPlayers = []
AvailablePlayers = []
SelectedPlayers = []
CurrentPlayers = []
CurrentCategory = ''


conn = sqlite3.connect('Matches.db')
c = conn.cursor()
c.execute("SELECT * from PlayerDetails")
AllPlayers = c.fetchall()
'''
for i in AllPlayers:
    name = i[0]
    AllPlayerNames.append(name)
'''
c.close()
conn.close()

class Ui_MainWindow(object):
    def New_Team(self):
        self.window = QtWidgets.QMainWindow()
        self.new = Ui_NewTeam()
        self.new.setupUi(self.window)
        self.window.show()
        self.EnableButtons()
        self.Initialize()
        self.DisplayAll()
        self.ClearDB()
        
    def EnableButtons(self):
        self.bat_btn.setEnabled(True)
        self.bow_btn.setEnabled(True)
        self.ar_btn.setEnabled(True)
        self.wk_btn.setEnabled(True)
        
    def Initialize(self):
        global Team_name
        global PointsAvailable
        global PointsUsed
        global no_of_bat
        global no_of_bwl
        global no_of_ar
        global no_of_wk
        global CurrentPlayers
        global SelectedPlayers
        global AvailablePlayers
        Team_name = 'Enter name here'
        PointsAvailable = 1000
        PointsUsed = 0
        no_of_bat = 0
        no_of_bwl = 0
        no_of_ar = 0
        no_of_wk = 0
        SelectedPlayers = []
        AvailablePlayers = []
        CurrentPlayers = []
        for i in AllPlayers:
            name = i[0]
            AvailablePlayers.append(name)
            CurrentPlayers.append(name)
        _translate = QtCore.QCoreApplication.translate
        self.batsmen.setText(_translate("MainWindow", "0"))
        self.bowlers.setText(_translate("MainWindow", "0"))
        self.allrounders.setText(_translate("MainWindow", "0"))
        self.wicketkeeper.setText(_translate("MainWindow", "0"))
        self.points_available.setText(_translate("MainWindow", "1000"))
        self.points_used.setText(_translate("MainWindow", "0"))
        

    def DisplayAll(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget.addItem("")
        self.listWidget.addItem("")
        self.listWidget_2.addItem("")
        self.listWidget_2.addItem("")
        for i in AllPlayers:
                s = i[0]
                ls = len(s)
                t = str(i[2]).rjust(35 - ls)
                s = s + t
                self.listWidget.addItem("{}".format(s));


        '''
        conn = sqlite3.connect('Matches.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Teams")
        print(c.fetchall())
        c.execute("SELECT teamname FROM Teams WHERE player1 = ''")
        Team_name = c.fetchone()
        Team_name = Team_name[0]
        print(Team_name)
        c.execute("SELECT * FROM Teams")
        print(c.fetchall())
        #c.execute("DELETE FROM Teams WHERE teamname = ?", (Team_name,))
        c.execute("SELECT * FROM Teams")
        print(c.fetchall())
        conn.commit()
        c.close()
        conn.close()
        self.team_name.setText(_translate("MainWindow", Team_name))
        '''
        '''
    def mousePressEvent(self, QMouseEvent):
        global Team_name
        try:
            if Team_name == 'Enter name here':
                _translate = QtCore.QCoreApplication.translate
                conn = sqlite3.connect('Matches.db')
                c = conn.cursor()
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                conn.commit()
        except:
            Team_name = 'Enter name here'
        finally:
            c.close()
            conn.close()
        '''
        
    def ClearDB(self):
        conn = sqlite3.connect('Matches.db')
        c = conn.cursor()
        c.execute("DELETE FROM Teams WHERE player1 = ''")
        conn.commit()
        c.close()
        conn.commit()
        
    def Open_Team(self):
        self.ClearDB()
        self.window = QtWidgets.QMainWindow()
        self.new = Ui_Dialog()
        self.new.setupUi(self.window)
        self.window.show()
    
    def DisableButtons(self):
        self.bat_btn.setEnabled(False)
        self.bow_btn.setEnabled(False)
        self.ar_btn.setEnabled(False)
        self.wk_btn.setEnabled(False)
        
        
    def Save_Team(self):
        global Team_name
        if Team_name == 'Enter name here':
            self.Reinitialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Create a new team first!!")
            msg.setWindowTitle("Create Team First")
            msg.exec_()
        elif(len(SelectedPlayers) > 11):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You can select atmost 11 players!!")
            msg.setWindowTitle("Team formation error")
            msg.exec_()
        elif(len(SelectedPlayers) < 11):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Select atleast 11 players.")
            msg.setWindowTitle("Team formation error")
            msg.exec_()
        else:
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            Team = ()
            Team += (Team_name,)
            for i in SelectedPlayers:
                Team += (i,)
            c.execute("INSERT INTO Teams VALUES {}".format(Team))
            conn.commit()
            c.close()
            conn.close()
            self.Reinitialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Team saved successfully!!")
            msg.setWindowTitle("Team Creation Successful")
            msg.exec_()
        
    def Reinitialize(self):
        global Team_name
        Team_name = 'Enter name here'
        self.DisableButtons()
        self.listWidget.clear()
        self.listWidget_2.clear()
        _translate = QtCore.QCoreApplication.translate
        self.batsmen.setText(_translate("MainWindow", "##"))
        self.bowlers.setText(_translate("MainWindow", "##"))
        self.allrounders.setText(_translate("MainWindow", "##"))
        self.wicketkeeper.setText(_translate("MainWindow", "##"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.team_name.setText(_translate("MainWindow", "Displayed Here"))

            
    def Evaluate_Team(self):
        self.ClearDB()
        self.window = QtWidgets.QMainWindow()
        self.new = Ui_evaluate_team()
        self.new.setupUi(self.window)
        self.window.show()
        

    def bat(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Reinitialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please create a new team first.")
            msg.setWindowTitle("Team Not Created")
            msg.exec_()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'BAT'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'BAT' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()
            
    
    def bwl(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Reinitialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please create a new team first.")
            msg.setWindowTitle("Team Not Created")
            msg.exec_()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'BWL'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'BWL' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()
            
    def ar(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Reinitialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please create a new team first.")
            msg.setWindowTitle("Team Not Created")
            msg.exec_()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'AR'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'AR' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()
            
    def wk(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Reinitialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please create a new team first.")
            msg.setWindowTitle("Team Not Created")
            msg.exec_()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'WK'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'WK' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()


    def AddPlayer(self, item):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Reinitialize()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please create a new team first.")
            msg.setWindowTitle("Team Not Created")
            msg.exec_()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            global CurrentPlayers
            global SelectedPlayers
            global AvailablePlayers
            global PointsAvailable
            global PointsUsed
            global no_of_bat
            global no_of_bwl
            global no_of_ar
            global no_of_wk
            t = item.text()
            t = t.rstrip("1234567890 ")
            if(t == ''):
                return
            for i in AllPlayers:
                if t == i[0]:
                    category = i[1]
                    value = i[2]
                    break
            total_no_of_players = no_of_bat + no_of_bwl + no_of_ar + no_of_wk
            if total_no_of_players == 11:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have already selected 11 players!!!\nNow save your team.")
                msg.setWindowTitle("All Players Selected")
                msg.exec_()
                return
            if total_no_of_players == 10:
                if no_of_bat == 0:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("You must select atleast 1 batsman!!!")
                    msg.setWindowTitle("Not Enough Batsmen")
                    msg.exec_()
                    return
                if no_of_bwl == 0:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("You must select atleast 1 bowler!!!")
                    msg.setWindowTitle("Not Enough Bowlers")
                    msg.exec_()
                    return
                if no_of_ar == 0:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("You must select atleast 1 allrounder!!!")
                    msg.setWindowTitle("Not Enough Allrounders")
                    msg.exec_()
                    return
                if no_of_wk == 0:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("You must select atleast 1 wicket-keeper!!!")
                    msg.setWindowTitle("Not Enough Wicket-keepers")
                    msg.exec_()
                    return
            if PointsAvailable - value < 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You dont have enough points to buy this player!!!")
                msg.setWindowTitle("Not Enough Points")
                msg.exec_()
                return
            if category == 'BAT' and no_of_bat == 4:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 4 batsmen!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'BWL' and no_of_bwl == 4:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 4 bowlers!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'AR' and no_of_ar == 4:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 4 allrounders!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'WK' and no_of_wk == 1:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 1 wicket-keeper!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'BAT':
                no_of_bat += 1
            elif category == 'BWL':
                no_of_bwl +=1
            elif category == 'AR':
                no_of_ar += 1
            elif category == 'WK':
                no_of_wk += 1
            PointsAvailable -= value
            PointsUsed += value
            CurrentPlayers.remove(t)
            AvailablePlayers.remove(t)
            SelectedPlayers.append(t)
            self.listWidget_2.addItem(t)
            r = self.listWidget.row(item)
            self.listWidget.takeItem(r)
            _translate = QtCore.QCoreApplication.translate
            self.batsmen.setText(_translate("MainWindow", "{}".format(no_of_bat)))
            self.bowlers.setText(_translate("MainWindow", "{}".format(no_of_bwl)))
            self.allrounders.setText(_translate("MainWindow", "{}".format(no_of_ar)))
            self.wicketkeeper.setText(_translate("MainWindow", "{}".format(no_of_wk)))
            self.points_available.setText(_translate("MainWindow", "{}".format(PointsAvailable)))
            self.points_used.setText(_translate("MainWindow", "{}".format(PointsUsed)))
        finally:
            conn.commit()
            c.close()
            conn.close()

        
        
        
    def RemovePlayer(self, item):
        global CurrentPlayers
        global SelectedPlayers
        global AvailablePlayers
        global PointsAvailable
        global CurrentCategory
        global PointsUsed
        global no_of_bat
        global no_of_bwl
        global no_of_ar
        global no_of_wk
        t = item.text()
        t = t.rstrip("1234567890 ")
        if(t == ''):
            return
        for i in AllPlayers:
            if t == i[0]:
                category = i[1]
                value = i[2]
                break
        if category == 'BAT':
            no_of_bat -= 1
        elif category == 'BWL':
            no_of_bwl -=1
        elif category == 'AR':
            no_of_ar -= 1
        elif category == 'WK':
            no_of_wk -= 1
        PointsAvailable += value
        PointsUsed -= value
        if category == CurrentCategory:
            CurrentPlayers.append(t)
            for i in AllPlayers:
                if i[0] == t:
                    lt = len(t)
                    s = str(i[2]).rjust(35 - lt)
                    s = t + s
                    self.listWidget.addItem("{}".format(s))
                    break
        AvailablePlayers.append(t)
        SelectedPlayers.remove(t)
        lt = len(t)
        t = t + str(value).rjust(35 - lt)
        r = self.listWidget_2.row(item)
        self.listWidget_2.takeItem(r)
        _translate = QtCore.QCoreApplication.translate
        self.batsmen.setText(_translate("MainWindow", "{}".format(no_of_bat)))
        self.bowlers.setText(_translate("MainWindow", "{}".format(no_of_bwl)))
        self.allrounders.setText(_translate("MainWindow", "{}".format(no_of_ar)))
        self.wicketkeeper.setText(_translate("MainWindow", "{}".format(no_of_wk)))
        self.points_available.setText(_translate("MainWindow", "{}".format(PointsAvailable)))
        self.points_used.setText(_translate("MainWindow", "{}".format(PointsUsed)))
        '''
        self.listWidget.clear()
        self.listWidget.addItem("")
        self.listWidget.addItem("")
        for i in CurrentPlayers:
                s = i[0]
                self.listWidget_2.addItem("{}".format(s));
        self.listWidget_2.clear()
        self.listWidget_2.addItem("")
        self.listWidget_2.addItem("")
        for i in SelectedPlayers:
                s = i[0]
                self.listWidget_2.addItem("{}".format(s));
        '''
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 50, 731, 111))
        self.label_11.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.batsmen = QtWidgets.QLabel(self.centralwidget)
        self.batsmen.setGeometry(QtCore.QRect(160, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batsmen.setFont(font)
        self.batsmen.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.batsmen.setObjectName("batsmen")
        self.bowlers = QtWidgets.QLabel(self.centralwidget)
        self.bowlers.setGeometry(QtCore.QRect(320, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowlers.setFont(font)
        self.bowlers.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.bowlers.setObjectName("bowlers")
        self.allrounders = QtWidgets.QLabel(self.centralwidget)
        self.allrounders.setGeometry(QtCore.QRect(510, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.allrounders.setFont(font)
        self.allrounders.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.allrounders.setObjectName("allrounders")
        self.wicketkeeper = QtWidgets.QLabel(self.centralwidget)
        self.wicketkeeper.setGeometry(QtCore.QRect(720, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wicketkeeper.setFont(font)
        self.wicketkeeper.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.wicketkeeper.setObjectName("wicketkeeper")
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        self.points_available.setGeometry(QtCore.QRect(210, 210, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.points_available.setFont(font)
        self.points_available.setStyleSheet("color: rgb(3, 190, 159);")
        self.points_available.setObjectName("points_available")
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        self.points_used.setGeometry(QtCore.QRect(550, 210, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.points_used.setFont(font)
        self.points_used.setStyleSheet("color: rgb(3, 190, 159);")
        self.points_used.setObjectName("points_used")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 240, 261, 311))
        self.listWidget.setLineWidth(1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color: rgb(3, 190, 159);")
        self.listWidget.setObjectName("listWidget")
        
        ''''''
        self.listWidget.itemDoubleClicked.connect(self.AddPlayer)
        ''''''
        
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(460, 240, 261, 311))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("color: rgb(3, 190, 159);")
        self.listWidget_2.setObjectName("listWidget_2")

        ''''''
        self.listWidget_2.itemDoubleClicked.connect(self.RemovePlayer)
        ''''''
        
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(570, 250, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setStyleSheet("color: rgb(3, 190, 159);")
        self.team_name.setObjectName("team_name")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(220, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(580, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(90, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(460, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(480, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(400, 370, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.bat_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.bat_btn.setEnabled(False)
        self.bat_btn.setGeometry(QtCore.QRect(100, 250, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.bat_btn.setFont(font)
        self.bat_btn.setObjectName("bat_btn")
        ''''''
        self.bat_btn.toggled.connect(self.bat)
        ''''''
        self.bow_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.bow_btn.setEnabled(False)
        self.bow_btn.setGeometry(QtCore.QRect(160, 250, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.bow_btn.setFont(font)
        self.bow_btn.setObjectName("bow_btn")
        ''''''
        self.bow_btn.toggled.connect(self.bwl)
        ''''''
        self.ar_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.ar_btn.setEnabled(False)
        self.ar_btn.setGeometry(QtCore.QRect(230, 250, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.ar_btn.setFont(font)
        self.ar_btn.setObjectName("ar_btn")
        ''''''
        self.ar_btn.toggled.connect(self.ar)
        ''''''
        self.wk_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.wk_btn.setEnabled(False)
        self.wk_btn.setGeometry(QtCore.QRect(290, 250, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.wk_btn.setFont(font)
        self.wk_btn.setObjectName("wk_btn")
        ''''''
        self.wk_btn.toggled.connect(self.wk)
        ''''''
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.menuBar.setFont(font)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")
        self.manage_teams = QtWidgets.QMenu(self.menuBar)
        self.manage_teams.setGeometry(QtCore.QRect(273, 110, 192, 138))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.manage_teams.setFont(font)
        self.manage_teams.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.manage_teams.setObjectName("manage_teams")
        MainWindow.setMenuBar(self.menuBar)
        self.new_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.new_team.setFont(font)
        self.new_team.setObjectName("new_team")
        
        
        ''''''
        self.new_team.triggered.connect(self.New_Team)
        ''''''
        
        
        self.open_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_team.setFont(font)
        self.open_team.setObjectName("open_team")
        
        ''''''
        self.open_team.triggered.connect(self.Open_Team)
        ''''''
        
        self.save_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.save_team.setFont(font)
        self.save_team.setObjectName("save_team")
        
        ''''''
        self.save_team.triggered.connect(self.Save_Team)
        ''''''
        
        self.evaluate_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.evaluate_team.setFont(font)
        self.evaluate_team.setObjectName("evaluate_team")
        
        ''''''
        self.evaluate_team.triggered.connect(self.Evaluate_Team)
        ''''''
        
        self.manage_teams.addAction(self.new_team)
        self.manage_teams.addAction(self.open_team)
        self.manage_teams.addAction(self.save_team)
        self.manage_teams.addAction(self.evaluate_team)
        self.menuBar.addAction(self.manage_teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.batsmen.setText(_translate("MainWindow", "##"))
        self.bowlers.setText(_translate("MainWindow", "##"))
        self.allrounders.setText(_translate("MainWindow", "##"))
        self.wicketkeeper.setText(_translate("MainWindow", "##"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.team_name.setText(_translate("MainWindow", "Displayed Here"))
        self.label_8.setText(_translate("MainWindow", "Your Selections"))
        self.label_9.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.label_10.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_12.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label_13.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_14.setText(_translate("MainWindow", "Points Available"))
        self.label_15.setText(_translate("MainWindow", "Points Used"))
        self.label_16.setText(_translate("MainWindow", "Team Name"))
        self.label_17.setText(_translate("MainWindow", ">"))
        self.bat_btn.setText(_translate("MainWindow", "BAT"))
        self.bow_btn.setText(_translate("MainWindow", "BOW"))
        self.ar_btn.setText(_translate("MainWindow", "AR"))
        self.wk_btn.setText(_translate("MainWindow", "WK"))
        self.manage_teams.setTitle(_translate("MainWindow", "&     Manage Teams     "))
        self.new_team.setText(_translate("MainWindow", "&       NEW Team"))
        self.open_team.setText(_translate("MainWindow", "  &     OPEN Team"))
        self.save_team.setText(_translate("MainWindow", "&       SAVE Team"))
        self.evaluate_team.setText(_translate("MainWindow", "&       EVALUATE Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

