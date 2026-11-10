import numpy as np

RECORDS = 100
HEADER = ["Student ID", "Age", "Study_Hours", "Attendance", "Math", "English", "Science"]

def create_dataset():
    np.random.seed(42)  # Same data for each and every run

    student_id = np.arange(1, RECORDS + 1)
    age = np.random.randint(18, 25, RECORDS)
    study_hours = np.round(np.random.uniform(1, 10, RECORDS), 1)
    attendance = np.round(np.random.uniform(60, 100, RECORDS), 1)
    math = np.random.randint(30, 101, RECORDS)
    eng = np.random.randint(30, 101, RECORDS)
    sci = np.random.randint(30, 101, RECORDS)

    datas = np.column_stack((student_id, age, study_hours, attendance, math, eng, sci))

    # Invalid values (for cleaning practice)
    datas[[9, 23, 57], 4] = [-10, 141, 105]
    datas[[4, 36, 48], 6] = [-38, 134, 102]
    datas[[8, 43, 78], 1] = [-20, 150, 111]
    datas[[6, 68, 99], 3] = [-12, 104, 145]

    # Missing values (np.nan)
    for column, count in ((2, 6), (5, 5), (3, 4)):
        rows = np.random.choice(RECORDS, count, replace=False)   # same row repeat aagaadhu
        datas[rows, column] = np.nan

    return datas

def main():

    student_performance = create_dataset()
    print(student_performance)

main()
