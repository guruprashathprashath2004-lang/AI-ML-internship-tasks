pass_marks = 40
high_score = 75
student_count = 10

def collect_marks():
    marks = []

    print(f"Enter {student_count} student's Marks")

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

def caluculate_mean(marks):
    return sum(marks)/len(marks)

def calculate_median(marks):
    sorted_marks = sorted(marks)
    n = len(marks)
    middle = n // 2

    if n % 2 == 1:
        return sorted_marks[middle]
    else:
        return (sorted_marks[middle - 1] + sorted_marks[middle]) / 2

def calculate_variance(marks):
    total = 0
    for mark in marks:
        total += (mark - caluculate_mean(marks)) ** 2

    return total / len(marks)   

def calculate_probability(marks, event):
    count = 0

    for mark in marks:
        if event == "pass" and mark >= pass_marks:
            count += 1
        elif event == "fail" and mark <= pass_marks:
            count += 1
        elif event == "above_80" and mark > high_score:
            count += 1

    return count / len(marks)


def main():
    marks = collect_marks()
    print("Collected marks:", marks)

    mean = caluculate_mean(marks)
    print("Mean Value: ", mean)

    median = calculate_median(marks)
    print("Median Value: ", median)

    variance = calculate_variance(marks)
    print("variance: ", variance)

    print(calculate_probability(marks, "pass"))
    print(calculate_probability(marks, "fail"))
    print(calculate_probability(marks, "above_80"))


main()