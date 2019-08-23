# -*- coding: utf-8 -*-

import sqlite3

selectedteam = 'Fantasy11'

conn = sqlite3.connect('Matches.db')
c = conn.cursor()

'''
c.execute('drop table if exists Match1')

c.execute("""CREATE TABLE Match1 (
                name text,
                runsscored integer,
                ballsfaced integer,
                fours integer,
                sixes integer,
                bowled integer,
                runsgiven integer,
                wickets integer,
                catches integer,
                stumpings integer,
                runouts integer
            )""")
'''

'''
c.execute("""INSERT INTO Match5 VALUES 
          ('Virat Kohli', 36, 54, 2, 0, 0, 0, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Yuvraj Singh', 12, 20, 1, 0, 48, 36, 1, 0, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Ajinkya Rahane', 8, 18, 0, 0, 0, 0, 0, 0, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Shikhar Dhawan', 34, 23, 8, 0, 0, 0, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('M.S.Dhoni', 13, 17, 1, 0, 0, 0, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Axar Patel', 8, 4, 2, 0, 48, 35, 1, 0, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Hardik Pandya', 0, 1, 0, 0, 54, 30, 2, 0, 0, 1)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Ravindra Jadeja', 18, 10, 1, 1, 60, 50, 2, 1, 0, 1)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Kedar Jadhav', 2, 4, 0, 0, 60, 57, 4, 0, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Ravichandran Ashwin', 23, 42, 3, 0, 56, 43, 2, 0, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Umesh Yadav', 50, 28, 5, 1, 0, 0, 0, 0, 2, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Jasprit Bumrah', 0, 0, 0, 0, 42, 22, 1, 0, 1, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Bhuwaneshwar Kumar', 19, 20, 2, 0, 42, 43, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Rohit Sharma', 115, 126, 11, 4, 0, 0, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match5 VALUES 
          ('Dinesh Kartick', 29, 42, 3, 0, 0, 0, 0, 2, 0, 1)""")
'''

'''
c.execute("""INSERT INTO Match6 VALUES 
          ('Virat Kohli', 102, 98, 8, 2, 0, 0, 0, 0, 0, 1)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Yuvraj Singh', 12, 20, 1, 0, 48, 36, 1, 0, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Ajinkya Rahane', 49, 75, 3, 0, 0, 0, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Shikhar Dhawan', 32, 35, 4, 0, 0, 0, 0, 0, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('M.S.Dhoni', 56, 45, 3, 1, 0, 0, 0, 3, 2, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Axar Patel', 8, 4, 2, 0, 48, 35, 1, 0, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Hardik Pandya', 42, 36, 3, 3, 30, 25, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Ravindra Jadeja', 18, 10, 1, 1, 60, 50, 2, 1, 0, 1)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Kedar Jadhav', 65, 60, 7, 0, 24, 24, 0, 0, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Ravichandran Ashwin', 23, 42, 3, 0, 60, 45, 6, 0, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Umesh Yadav', 0, 0, 0, 0, 54, 50, 4, 1, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Jasprit Bumrah', 0, 0, 0, 0, 60, 49, 1, 0, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Bhuwaneshwar Kumar', 15, 12, 2, 0, 60, 46, 2, 0, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Rohit Sharma', 46, 65, 5, 1, 0, 0, 0, 1, 0, 0)""")
c.execute("""INSERT INTO Match6 VALUES 
          ('Dinesh Kartick', 29, 42, 3, 0, 0, 0, 0, 2, 0, 1)""")
'''

'''
c.execute("SELECT * FROM Match5")
l = c.fetchall()
for i in l:
    print(i)
'''

'''
c.execute("SELECT * FROM PlayerDetails")
l = c.fetchall()
for i in l:
    print(i)

c.execute("SELECT * FROM Teams")
l = c.fetchall()
for i in l:
    print(i)
'''
'''
c.execute("SELECT * FROM sqlite_master WHERE type='table';")
l = c.fetchall()
#for i in l:
#    print(i)
for i in l:
    if i[1].startswith('Match'):
        print(i)
'''
'''
for name in res:
    if name[0].startswith('Match'):
        print(name[0])
'''

#c.execute("SELECT * FROM Teams WHERE teamname = ?", (selectedteam,))
#print(c.fetchone())
#c.execute("SELECT * FROM PlayerDetails")
#print(c.fetchall())
#c.execute("DELETE FROM Match6")
#c.execute('drop table if exists Match6')
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
