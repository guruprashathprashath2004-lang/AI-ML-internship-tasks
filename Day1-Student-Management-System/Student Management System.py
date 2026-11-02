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
        else:
            print("Features coming soon.")

main()
