class Student:
    def __init__(self, sid, name, age, dept, cgpa):
        self.sid = sid
        self.name = name
        self.age = age
        self.dept = dept
        self.cgpa = cgpa



students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD STUDENT
    if choice == "1":
        sid = int(input("Enter Student ID: "))

        # Check for duplicate ID
        duplicate = False

        for s in students:
            if s.sid == sid:
                duplicate = True
                break

        if duplicate:
            print("Student ID already exists!")

        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            dept = input("Enter Department: ")
            cgpa = float(input("Enter CGPA: "))

            s = Student(sid, name, age, dept, cgpa)
            students.append(s)

            print("Student Added Successfully!")

    # VIEW STUDENTS
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")

        else:
            print("\n===== STUDENT RECORDS =====")

            for s in students:
                print(f"ID: {s.sid}")
                print(f"Name: {s.name}")
                print(f"Age: {s.age}")
                print(f"Department: {s.dept}")
                print(f"CGPA: {s.cgpa}")
                print("---------------------------")

    # SEARCH STUDENT
    elif choice == "3":
        sid = int(input("Enter Student ID to Search: "))

        found = False

        for s in students:
            if s.sid == sid:
                print("\nStudent Found")
                print(f"ID: {s.sid}")
                print(f"Name: {s.name}")
                print(f"Age: {s.age}")
                print(f"Department: {s.dept}")
                print(f"CGPA: {s.cgpa}")

                found = True
                break

        if not found:
            print("Student Not Found")

    # UPDATE STUDENT
    elif choice == "4":
        sid = int(input("Enter Student ID to Update: "))

        found = False

        for s in students:
            if s.sid == sid:
                s.name = input("Enter New Name: ")
                s.age = int(input("Enter New Age: "))
                s.dept = input("Enter New Department: ")
                s.cgpa = float(input("Enter New CGPA: "))

                print("Student Updated Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found")

    # DELETE STUDENT
    elif choice == "5":
        sid = int(input("Enter Student ID to Delete: "))

        found = False

        for s in students:
            if s.sid == sid:
                students.remove(s)
                print("Student Deleted Successfully!")
                found = True
                break

        if not found:
            print("Student Not Found")

    # EXIT
    elif choice == "6":
        print("Thank You!")


        break

    # INVALID CHOICE
    else:
        print("Invalid Choice!")