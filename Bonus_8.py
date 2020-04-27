import sqlite3

conn = sqlite3.connect("Our_Data.db")

cursor = conn.cursor()
print("Cursor Created")

def read_data():
    fetch = cursor.execute(''' SELECT ID, NAME, DIVISION, RATING FROM Employee_Records ''')
    for record in fetch:
        print('ID : ',record[0])
        print('NAME : ', record[1])
        print('DIVISION : ', record[2])
        print('RATING : ', record[3])
        print("\n")

# read_data()

def check_data():
    data = cursor.execute(''' SELECT NAME, DIVISION, RATING FROM Employee_Records WHERE ID = 2  ''')
    x = data.fetchall()
    if x == []:
        print("Does not exist")
    else:
        print(x[0][0])

    # for record in data:
    #     print('NAME : ',record[0])
    #     # print('NAME : ', record[1])
    #     # print('DIVISION : ', record[2])
    #     # print('RATING : ', record[3])
    #     # print("\n")


check_data()

conn.close()