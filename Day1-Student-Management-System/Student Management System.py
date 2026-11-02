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
        else:
            print("Features coming soon.")

def add_student():
    print("|===Add Student===|")
    student_ID = input("Enter student ID: ").strip()
    name = input("Enter your name: ").strip()
    marks = float(input("Enter your marks: "))

    Student = {"id": student_ID, "name": name, "marks": marks }
    Students.append(Student)
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

main()
