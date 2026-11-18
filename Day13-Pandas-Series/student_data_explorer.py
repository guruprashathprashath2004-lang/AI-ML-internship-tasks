import pandas as pd

names = pd.Series(["Kamal", "Nimal", "Sunil", "Amal", "Ruwan", "Kasun", "Dilani", "Nadeesha", "Saman", "Chamari"])
ages = pd.Series([20, 21, 19, 22, 20, 21, 19, 23, 22, 20])
python_marks = pd.Series([85, 72, 91, 68, 77, 95, 80, 88, 35, 74])
ai_marks = pd.Series([78, 65, 88, 59, 82, 90, 70, 92, 30, 66])

total = python_marks + ai_marks
average = total / 2

def display_all_students():
    print("|==== STUDENTS DATA ====|".center(61))
    print("-" * 61)
    print(f"{'No':<5}{'Names':<10}{'Ages':<6}{'Python Marks':<14}{'AI Marks':<10}{'Total':<7}{'Average':<9}")
    print("-" * 61)

    for i in range(len(names)):
        print(f"{i+1:<5}{names.iloc[i]:<10}{ages.iloc[i]:<6}{python_marks.iloc[i]:<14}{ai_marks.iloc[i]:<10}{total.iloc[i]:<7}{average.iloc[i]:<9}")


def main():
    display_all_students()

main()