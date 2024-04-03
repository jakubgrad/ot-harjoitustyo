import sqlite3

con = sqlite3.connect("house_app.db")
cur = con.cursor()
# Create the users table
#cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username VARCHAR UNIQUE, password VARCHAR);")

cur.execute("CREATE TABLE artist( artistid INTEGER PRIMARY KEY, artistname TEXT);")
cur.execute("CREATE TABLE track( trackid     INTEGER, trackname   TEXT, trackartist INTEGER, FOREIGN KEY(trackartist) REFERENCES artist(artistid) );")




cur.execute("CREATE TABLE users( userid INTEGER PRIMARY KEY, username TEXT);")
cur.execute("CREATE TABLE houses( houseid INTEGER, housename TEXT, houseuser INTEGER, FOREIGN KEY(houseuser) REFERENCES users(userid) );")



# Create the houses table with a user_id column
#cur.execute("CREATE TABLE houses(id INTEGER PRIMARY KEY, userid INTEGER, FOREIGN KEY(userid) REFERENCES users(id), statistics VARCHAR);")
#con.commit()
con.close()
