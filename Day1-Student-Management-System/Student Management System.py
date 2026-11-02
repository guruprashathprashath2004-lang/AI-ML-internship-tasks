students = []

def choice_menu():
    print("|====Student Management System====|")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student By ID")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Display Grade Report")
    print("7. Exit")
    print("----------------------------------")

def main():
    while True:
        choice_menu()
        choice = input("Enter Your Choice (1-7): ").strip()

        if choice == "7":
            print("Thank you! Bye.")
            break
        elif choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            grade_report()
        else:
            print("Invalid choice. Please enter 1-7.")

def add_student():
    print("|===Add Student===|")
    student_id = get_valid_id()

    name = ""
    while name == "":
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be empty.")

    marks = get_valid_marks()

    students.append({"id": student_id, "name": name, "marks": marks})
    print("Student added successfully!")

def view_student():
    print("|====View Students====|")
    if len(students) == 0:
        print("No students found.")
        return

    print(f"{'ID':<10}{'Name':<20}{'Marks':<8}")
    print("-" * 38)
    for student in students:
        print(f"{student['id']:<10}{student['name']:<20}{student['marks']:<8}")

def find_student(student_id):
    for student in students:
        if student['id']  == student_id:
            return student
    return None

def search_student():
    print("|====Search Student====|")
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)
    if student:
        print(f"Student found: {student['name']} with marks {student['marks']}")
    else:
        print("Student not found.")

def update_student_marks():
    print("|====Update Student Marks====|")
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)
    if student:
        new_marks = get_valid_marks("Enter new marks (0-100): ")
        student['marks'] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    print("|====Delete Student====|")
    student_id = input("Enter student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    print("Student deleted successfully!")

def get_valid_id():
    while True:
        student_id = input("Enter student ID: ").strip()
        if student_id == "":
            print("Student ID cannot be empty.")
        elif find_student(student_id) is not None:
            print("ID already exists. Try another one")
        else:
            return student_id

def get_valid_marks(prompt="Enter marks (0-100): "):
    while True:
        try:
            marks = float(input(prompt))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


def grade_report():
    print("|====Grade Report====|")
    if len(students) == 0:
        print("No students found.")
        return

    print(f"{'ID':<10}{'Name':<20}{'Marks':<8}{'Grade':<6}")
    print("-" * 44)
    for s in students:
        grade = calculate_grade(s["marks"])   # local variable
        print(f"{s['id']:<10}{s['name']:<20}{s['marks']:<8}{grade:<6}")
    show_statistics()    

def show_statistics():
    total = 0
    top_student = students[0]

    for s in students:
        total += s["marks"]
        if s["marks"] > top_student["marks"]:
            top_student = s

    average = total / len(students)
    print(f"\nAverage Marks : {average:.2f}")
    print(f"Top Performer : {top_student['name']} ({top_student['marks']})")



main()
