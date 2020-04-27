import sqlite3

conn = sqlite3.connect("Our_Data.db")


def delete_record():
    conn.execute(''' DELETE FROM Employee_Records WHERE ID = 1 ''')
    conn.commit()
    print("Record Deleted")

delete_record()
conn.close()