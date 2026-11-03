import matplotlib.pyplot as plt

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

def generate_graphs(marks):
    student_numbers = list(range(1, len(marks) + 1))
    labels = [f"S{n}" for n in student_numbers]

    plt.figure(figsize=(12, 8))

    # 1. Bar Chart
    plt.subplot(2, 2, 1)
    plt.bar(labels, marks, color="steelblue")
    plt.title("Student vs Marks")
    plt.xlabel("Student")
    plt.ylabel("Marks")

    # 2. Line Chart
    plt.subplot(2, 2, 2)
    plt.plot(student_numbers, marks, marker="o", color="green")
    plt.title("Marks Trend")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    # 3. Histogram
    plt.subplot(2, 2, 3)
    plt.hist(marks, bins=5, color="orange", edgecolor="black")
    plt.title("Score Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")

    # 4. Scatter Plot
    plt.subplot(2, 2, 4)
    plt.scatter(student_numbers, marks, color="red")
    plt.title("Student Number vs Marks")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.tight_layout()
    plt.show()

def main():
    print("|===== STUDENT EXAM SCORE ANALYSIS =====|")
    marks = collect_marks()
    display_statistics(marks)
    generate_graphs(marks)

main()