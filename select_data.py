import sqlite3
conn = sqlite3.connect('PostDB.db')
cur = conn.execute('SELECT * FROM contact')
row = cur.fetchone()
print(row)