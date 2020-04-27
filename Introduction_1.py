import sqlite3

conn = sqlite3.connect("Our_Data.db")

print("Database opened")

conn.close()

print("Database closed")