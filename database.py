import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="03062008",
    database="student_db"
)

if conn.is_connected():
    print("Connected Successfully!")