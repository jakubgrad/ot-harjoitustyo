import sqlite3

con = sqlite3.connect("house_app.db")
cur = con.cursor()

cur.execute("CREATE TABLE users( id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
cur.execute("CREATE TABLE houses( id INTEGER, user_id INTEGER, parameters TEXT, statistics TEXT, FOREIGN KEY(user_id) REFERENCES users(id));")

con.close()
