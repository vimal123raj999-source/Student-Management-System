import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="03062008",   # Your MySQL password
    database="student_db"
)

cursor = conn.cursor()

sid = int(input("Enter Student ID: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
dept = input("Enter Department: ")
cgpa = float(input("Enter CGPA: "))

query = """
INSERT INTO students(student_id, name, age, department, cgpa)
VALUES (%s, %s, %s, %s, %s)
"""

values = (sid, name, age, dept, cgpa)

cursor.execute(query, values)
conn.commit()

print("Student Added Successfully!")

cursor.close()
conn.close()