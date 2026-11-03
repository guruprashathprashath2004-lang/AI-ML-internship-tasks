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

def display_statistics(marks):
    pass_probability = calculate_probability(marks, "pass")
    fail_probability = calculate_probability(marks, "fail")
    above_80_probability = calculate_probability(marks, "above_80")

    print("\n|==== STATISTICAL ANALYSIS ====|")
    print(f"Mean            : {caluculate_mean(marks):.2f}")
    print(f"Median          : {calculate_median(marks):.2f}")
    print(f"Maximum Score   : {max(marks)}")
    print(f"Minimum Score   : {min(marks)}")
    print(f"Variance        : {calculate_variance(marks):.2f}")
    print(f"Pass Percentage : {pass_probability * 100:.1f}%")
    print(f"Fail Percentage : {fail_probability * 100:.1f}%")

    print("\n|==== PROBABILITY ANALYSIS ====|")
    print(f"Probability(Passed)     : {pass_probability:.2f}")
    print(f"Probability(Score > 80) : {above_80_probability:.2f}")
    print(f"Probability(Failed)     : {fail_probability:.2f}")

def main():
    print("===== STUDENT EXAM SCORE ANALYSIS =====")
    marks = collect_marks()
    display_statistics(marks)

main()