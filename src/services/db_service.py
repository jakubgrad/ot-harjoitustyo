import sqlite3
import os
# db_path = "../db/db_setup.db"


class DbService():
    def __init__(self):
        # self._con = sqlite3.connect("../db/db_setup.db")
        self._con = sqlite3.connect("src/db/house_app.db")

    def destroy_database(self):
        pass


db_service = DbService()
# cur = con.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
