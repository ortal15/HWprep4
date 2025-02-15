import sqlite3
from prep4_def import create_table, insert_into, menu, option_1, option_2, option_3, option_4

create_table()
insert_into()
menu()

conn = sqlite3.connect('prep4.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM garage ;")

rows = cursor.fetchall()
for row in rows:
    print(dict(row))
