import sqlite3

conn = sqlite3.connect("Our_Data.db")

def insert_record(ID,NAME,DIVISION,RATING):
    conn.execute(''' INSERT INTO Employee_Records(ID, NAME,DIVISION,RATING)
                VALUES(?,?,?,?)''',(ID,NAME,DIVISION,RATING))
    conn.commit()
    print("Record inserted")

insert_record(8,"Bob","Networking",4)

conn.close()

print("Database Closed")
