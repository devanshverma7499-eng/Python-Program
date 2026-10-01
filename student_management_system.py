students = []


def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    marks = []
    subjects = ["Python", "HTML", "C"]

    for subject in subjects:
        mark = float(input(f"Enter marks in {subject}: "))
        marks.append(mark)

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("\nStudent added successfully!")


def display_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        total = sum(student["marks"])
        percentage = total / len(student["marks"])

        print("\nRoll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", total)
        print("Percentage:", round(percentage, 2))

        if percentage >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


def search_student():
    roll_no = input("\nEnter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\n===== STUDENT FOUND =====")
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])

            total = sum(student["marks"])
            percentage = total / len(student["marks"])

            print("Total:", total)
            print("Percentage:", round(percentage, 2))
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Try again.")


main()