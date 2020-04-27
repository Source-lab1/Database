import sqlite3

conn = sqlite3.connect("Our_Data.db")

def update_record():
    conn.execute(''' UPDATE Employee_Records set DIVISION = 'Hardware' WHERE ID = 2''')
    conn.commit()
    print("Updated")

update_record()
conn.close()