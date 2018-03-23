# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 01:44:09 2018

@author: principal
"""

import sqlite3

conn = sqlite3.connect('Matches.db')
c = conn.cursor()
c.execute("SELECT * FROM Teams")
print(c.fetchall())
c.execute("DELETE FROM Teams WHERE player1 = ''")
#c.execute("SELECT * FROM Teams")
#print(c.fetchall())
#conn.commit()
c.close()
conn.close()