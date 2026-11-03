def collect_marks():
    marks = []

    print("Enter 10 student's Marks")

    for i in range(1, 11): 
        while True:
            try:
                mark = float(input(f"Enter student {i} marks: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100")
            except ValueError:
                print("Invalid number. please enter a valid number between 0 and 100")

    return marks

def main():
    marks = collect_marks()
    print("Collected marks:", marks)

main()