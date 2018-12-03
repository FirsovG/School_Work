# from PyQt5 import uic
from json import dumps, loads
import sqlite3

# uic.compileUiDir("./UI")

db_connection = sqlite3.connect("./database/school_work.db")
db = db_connection.cursor()
config = (True, 'BK_TM', 4, dumps(['Firstname', 'Name', 'Age', 'Class']))


db.execute('''
        CREATE TABLE IF NOT EXISTS tbl_config
        (
            configuration bit,
            name_of_school varchar(100),
            column_count int,
            column_names text
        );
        ''')

# db.execute('''
#         INSERT INTO tbl_config VALUES(?,?,?,?);
#         ''', config)

for row in db.execute('SELECT * FROM tbl_config'):
    print(row)

db_connection.commit()
db_connection.close()
