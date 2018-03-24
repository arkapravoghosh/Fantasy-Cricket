# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:44:09 2018

@author: principal
"""

import sqlite3

selectedteam = 'Fantasy11'

conn = sqlite3.connect('Matches.db')
c = conn.cursor()
c.execute("SELECT * FROM Teams")
print(c.fetchall())
#c.execute("SELECT * FROM Teams WHERE teamname = ?", (selectedteam,))
#print(c.fetchone())
#c.execute("SELECT * FROM PlayerDetails")
#print(c.fetchall())
#c.execute("DELETE FROM Teams WHERE teamname = 'KKR'")
#c.execute("SELECT * FROM Teams")
#print(c.fetchall())


#Team_name = 'Fantasy11'
'''
c.execute("SELECT * FROM Teams")
l = c.fetchall()
flag = 0
for i in l:
    if i[0] == Team_name:
        flag = 1
        break
if flag == 0:
    Team = ('Fantasy11', 'Virat Kohli', 'Yuvraj Singh', 'Ajinkya Rahane', 'Shikhar Dhawan', 'M.S.Dhoni', 'Axar Patel', 'Hardik Pandya', 'Ravindra Jadeja', 'Kedar Jadhav', 'Ravichandran Ashwin', 'Umesh Yadav')
    c.execute("INSERT INTO Teams VALUES {}".format(Team))
else:
    print("Teamname already exists")
'''

'''
Team = ('MightyLions', '', '', '', '', '', '', '', '', '', '', '')
c.execute("INSERT INTO Teams VALUES {}".format(Team))
'''

'''
c.execute("SELECT * FROM Teams")
print(c.fetchall())
'''

#conn.commit()
c.close()
conn.close()