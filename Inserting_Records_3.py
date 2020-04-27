import sqlite3

conn = sqlite3.connect("Our_Data.db")

print("Database opened")

conn.execute(''' INSERT INTO Employee_Records(ID, NAME,DIVISION,RATING)
        VALUES(5,'Joan','Electronics' ,3)
        ''')

conn.execute(''' INSERT INTO Employee_Records(ID, NAME,DIVISION,RATING)
        VALUES(6,'James','Maintenance' ,5)
        ''')

conn.execute(''' INSERT INTO Employee_Records(ID, NAME,DIVISION,RATING)
        VALUES(7,'Sammy','Devops' ,4)
        ''')

conn.commit()

print("Record Inserted ")

conn.close()

print("Database closed")