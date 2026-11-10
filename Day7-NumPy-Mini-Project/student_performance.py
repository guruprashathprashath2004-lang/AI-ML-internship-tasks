import numpy as np

RECORDS = 100
HEADER = ["Student ID", "Age", "Study_Hours", "Attendance", "Math", "English", "Science"]

VALID_RANGES = {
    1: (15, 60),
    2: (0, 24),
    3: (0, 100),
    4: (0, 100),
    5: (0, 100),
    6: (0, 100),
}

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


def format_value(value, column):
    if column == 0:
        return str(int(value))
    return f"{value:.1f}"


def display_dataset(student_performance, title):
    print(f"|==== {title} ====|\n".center(105))

    if len(student_performance) == 0:
        print("No record found..!")
        return

    print("-" * (15 * len(HEADER)))
    print("" .join(f"{head:<15}" for head in HEADER))
    print("-" * (15 * len(HEADER)))

    for data in student_performance:
        print("" .join(f"{format_value(value, column):<15}" for column,value in enumerate(data)))


def explore_properties(student_performance):

    print()
    print(f"|==== DATASET EXPLORATION ====|\n".center(105))

    if len(student_performance) == 0:
        print("No record found..!")
        return
    
    print(f"---- Properties ----".center(30))
    print(f"Shape     : {student_performance.shape}")
    print(f"Dimention : {student_performance.ndim}")
    print(f"Size      : {student_performance.size}")
    print(f"Data Type : {student_performance.dtype}")

    print()
    print(f"---- Missing Values ----".center(30))
    print(f"Student ID   : {np.sum(np.isnan(student_performance[:,0]))}")
    print(f"Age          : {np.sum(np.isnan(student_performance[:,1]))}")
    print(f"Studey_Hours : {np.sum(np.isnan(student_performance[:,2]))}")
    print(f"Attendence   : {np.sum(np.isnan(student_performance[:,3]))}")
    print(f"Math         : {np.sum(np.isnan(student_performance[:,4]))}")
    print(f"English      : {np.sum(np.isnan(student_performance[:,5]))}")
    print(f"Science      : {np.sum(np.isnan(student_performance[:,6]))}")


def clean_invalid_values(student_performance):

    print()
    print(f"|==== CLEAN INVALID VALUES ====|\n".center(105))

    if len(student_performance) == 0:
        print("No record found..!")
        return

    cleaned = student_performance.copy()

    for column, (low,high) in VALID_RANGES.items():
        values = cleaned[:, column]
        invalid_values = (values < low) | (values > high)
        print(f"{HEADER[column]:<15}: {np.sum(invalid_values)} invalid (valid range {low} - {high})")
        values[invalid_values] = np.nan

    return cleaned

def main():

    student_performance = create_dataset()
    display_dataset(student_performance, "STUDENT PERFORMANCE DATA")
    explore_properties(student_performance)
    clean_invalid_values(student_performance)

main()
