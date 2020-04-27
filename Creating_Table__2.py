import sqlite3

conn = sqlite3.connect("Our_Data.db")

print("Database opened")

conn.execute(''' CREATE TABLE IF NOT EXISTS Employee_Records (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    RATING INT NOT NULL)''')

print("Table Created ")

conn.close()

print("Database closed")