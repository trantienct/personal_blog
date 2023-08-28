import sqlite3
conn = sqlite3.connect('PostDB.db')

add_user = '''
    INSERT INTO users (username, password, fullname) VALUES (?, ?, ?)
'''
conn.execute(add_user, ('admin', '12345', 'Administrator'))
conn.commit()
cur = conn.execute('SELECT * FROM users')
row = cur.fetchall()
print(row)

conn.close()