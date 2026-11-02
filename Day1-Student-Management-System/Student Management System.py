Students = []

def choice_menu():
    print("|====Student Management System====|")
    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student By ID")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Display Grade Report")
    print("7. Exit")
    print("----------------------------------")

def main():
    while True:
        choice_menu()
        choice = input("Enter Your Choice: (1-7)").strip()

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
            print("Features coming soon.")

def add_student():
    print("|===Add Student===|")
    student_ID = get_valid_id()

    name = ""
    while name == "":
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be empty.")

    marks = get_valid_marks()

    Students.append({"id": student_ID, "name": name, "marks": marks})
    print("Student added successfully!")

def view_student():
    print("|====View Students====|")
    if len(Students) == 0:
        print("No Students Found.")
        return

    print(f"{'id':<10}{'name':<20}{'marks':<8}")
    print("-" * 38)
    for Student in Students:
        print(f"{Student['id']:<10}{Student['name']:<20}{Student['marks']:<8}")

def find_student(student_ID):
    for Student in Students:
        if Student['id']  == student_ID:
            return Student
    return None

def search_student():
    print("|====Search Student====|")
    student_ID = input("Enter student ID: ").strip()
    Student = find_student(student_ID)
    if Student:
        print(f"Student Found: {Student['name']} with marks {Student['marks']}")
    else:
        print("Student not found.")

def update_student_marks():
    print("|====Update Student Marks====|")
    student_ID = input("Enter student ID: ").strip()
    Student = find_student(student_ID)
    if Student:
        new_marks = get_valid_marks("Enter new marks (0-100): ")
        Student['marks'] = new_marks
        print("Marks updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    student_ID = input("Enter student ID: ").strip()
    student = find_student(student_ID)

    if student is None:
        print("Student not found.")
        return

    Students.remove(student)
    print("Student deleted successfully!")

def get_valid_id():
    while True:
        student_ID = input("Enter student ID: ").strip()
        if student_ID == "":
            print("Student ID cannot be empty")
        elif find_student(student_ID) is not None:
            print("ID already exists. Try another one")
        else:
            return student_ID

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
    print("\n--- Grade Report ---")
    if len(Students) == 0:
        print("No students found.")
        return

    print(f"{'ID':<10}{'Name':<20}{'Marks':<8}{'Grade':<6}")
    print("-" * 44)
    for s in Students:
        grade = calculate_grade(s["marks"])   # local variable
        print(f"{s['id']:<10}{s['name']:<20}{s['marks']:<8}{grade:<6}")
    
main()
