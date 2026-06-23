import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="03062008",
    database="student_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()