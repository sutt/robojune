import sqlite3

db = sqlite3.connect("db1.db")
c = db.cursor()
#db.execute("CREATE TABLE tablet (id int, val text)")
#c.execute("""INSERT INTO tablet VALUES (1, 'Bad') """)
c.execute("""SELECT * from tablet """)
print c.fetchall()

db.close()