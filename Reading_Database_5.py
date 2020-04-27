import sqlite3

conn = sqlite3.connect("Our_Data.db")


def read_data():
    fetch = conn.execute(''' SELECT ID, NAME, DIVISION, RATING FROM Employee_Records ''')
    for record in fetch:
        print('ID : ',record[0])
        print('NAME : ', record[1])
        print('DIVISION : ', record[2])
        print('RATING : ', record[3])
        print("\n")


read_data()

conn.close()

print("Database Closed")