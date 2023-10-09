import sqlite3

conn = sqlite3.connect('PostDB.db')
user_sql = '''
    CREATE TABLE IF NOT EXISTS users
    (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    fullname TEXT
    );
'''
contact_sql = '''
    CREATE TABLE IF NOT EXISTS contact
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    subject TEXT,
    gender INTEGER,
    message TEXT
    );
'''
post_sql = '''
    CREATE TABLE IF NOT EXISTS posts
    (
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_title TEXT,
    post_excerpt TEXT,
    post_content TEXT,
    post_author INTEGER,
    post_category INTEGER,
    tag_id INTEGER,
    create_date TEXT
    );
'''
category_sql = '''
    CREATE TABLE IF NOT EXISTS category
    (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT
    );
'''
conn.execute(user_sql)
conn.execute(post_sql)
conn.execute(category_sql)
conn.execute(contact_sql)
conn.commit()
conn.close()