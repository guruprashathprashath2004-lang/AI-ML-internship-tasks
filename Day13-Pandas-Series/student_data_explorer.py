import pandas as pd

names = pd.Series(["Kamal", "Nimal", "Sunil", "Amal", "Ruwan", "Kasun", "Dilani", "Nadeesha", "Saman", "Chamari"])
ages = pd.Series([20, 21, 19, 22, 20, 21, 19, 23, 22, 20])
python_marks = pd.Series([55, 32, 91, 68, 77, 95, 80, 38, 91, 74])
ai_marks = pd.Series([98, 65, 88, 39, 82, 70, 70, 92, 91, 36])

total = python_marks + ai_marks
average = total / 2

passed = (python_marks > 40) & (ai_marks > 40)




def display_all_students():
    print("|==== STUDENTS DATA ====|".center(61))
    print("-" * 61)
    print(f"{'No':<5}{'Names':<10}{'Ages':<6}{'Python Marks':<14}{'AI Marks':<10}{'Total':<7}{'Average':<9}")
    print("-" * 61)

    for i in range(len(names)):
        print(f"{i+1:<5}{names.iloc[i]:<10}{ages.iloc[i]:<6}{python_marks.iloc[i]:<14}{ai_marks.iloc[i]:<10}{total.iloc[i]:<7}{average.iloc[i]:<9}")

    print("-" * 61)


def highest_marks():
    highest_python_marks = python_marks.idxmax()
    highest_ai_marks = ai_marks.idxmax()
    highest_total_marks = total.idxmax()
    highest_average_marks =  average.idxmax()

    print()
    print("|==== STUDENT WITH HIGHEST MARKS ====|\n".center(61))
    print(f"{names[highest_python_marks]} -> {python_marks[highest_python_marks]}   (Python Mark)")
    print(f"{names[highest_ai_marks]} -> {ai_marks[highest_ai_marks]}   (AI Mark)")
    print(f"{names[highest_total_marks]} -> {total[highest_total_marks]}  (Total Mark)")
    print(f"{names[highest_average_marks]} -> {average[highest_average_marks]} (Average Mark)")


def lowest_marks():
    lowest_python_marks = python_marks.idxmin()
    lowest_ai_marks = ai_marks.idxmin()
    lowest_total_marks = total.idxmin()
    lowest_average_marks =  average.idxmin()

    print()
    print("|==== STUDENT WITH LOWEST MARKS ====|\n".center(61))
    print(f"{names[lowest_python_marks]} -> {python_marks[lowest_python_marks]}   (Python Mark)")
    print(f"{names[lowest_ai_marks]}  -> {ai_marks[lowest_ai_marks]}   (AI Mark)")
    print(f"{names[lowest_total_marks]}  -> {total[lowest_total_marks]}  (Total Mark)")
    print(f"{names[lowest_average_marks]}  -> {average[lowest_average_marks]} (Average Mark)")


def average_marks():
    print()
    print("|==== AVERAGE MARKS ====|\n".center(61))
    print(f"Average of Python Marks : {python_marks.mean()}")
    print(f"Average of AI Marks     : {ai_marks.mean()}")
    print(f"Overall Average         : {average.mean()}")


def scoring_above_75():

    print()
    print(f"|==== STUDENTS SCORING ABOVE 75 ====|\n".center(61))

    above = average[average > 75]

    if len(above) == 0:
        print("No student found...!")
        return

    for i in above.index:
        print(f"{names[i]:<9} ->  {above[i]}")

    print(f"\nTotal Count : {len(above)}")


def generate_grade():

    grades = []

    for i in range(len(names)):
        if passed.iloc[i]:
            grades.append("Pass")
        else:
            grades.append("Fail")

    return pd.Series(grades)


def passing_students(grade):

    print("|==== STUDENTS GRADE ====|".center(67))
    print("-" * 67)
    print(f"{'No':<5}{'Names':<10}{'Ages':<6}{'Python Marks':<14}{'AI Marks':<10}{'Total':<7}{'Average':<9}{'Grade':<6}")
    print("-" * 67)

    for i in range(len(names)):
        print(f"{i+1:<5}{names.iloc[i]:<10}{ages.iloc[i]:<6}{python_marks.iloc[i]:<14}{ai_marks.iloc[i]:<10}{total.iloc[i]:<7}{average.iloc[i]:<9}{grade.iloc[i]:<6}")

    print("-" * 67)

    print(f"Passed students count : {(grade == "Pass").sum()}")
    print(f"Failed students count : {(grade == "Fail").sum()}")


def main():
    display_all_students()
    highest_marks()
    lowest_marks()
    average_marks()
    scoring_above_75()
    grade = generate_grade()
    passing_students(grade)

main()