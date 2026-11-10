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

MARKS = [4, 5, 6] 

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


def handle_missing_values(student_performance):

    print()
    print(f"|==== HANDLE MISSING VALUES ====|\n".center(105))

    if len(student_performance) == 0:
        print("No record found..!")
        return

    filled = student_performance.copy()

    for column in range(1, filled.shape[1]):          # 0 = Student ID, skip
        values = filled[:, column]
        missing = np.isnan(values)

        if np.sum(missing) > 0:
            mean_value = np.round(np.nanmean(values), 2)       
            values[missing] = mean_value
            print(f"{HEADER[column]:<15}: {np.sum(missing)} filled with mean {mean_value}")

    print(f"\nMissing values left : {np.sum(np.isnan(filled))}")
    return filled


def filter_records(student_performance):

    average_marks = student_performance[:, MARKS].mean(axis=1)     

    print()
    high_performers = student_performance[average_marks >= 85]
    display_dataset(high_performers[:5], f"HIGH PERFORMERS (AVERAGE >= 85) : {len(high_performers)} students")

    print()
    low_attendance = student_performance[student_performance[:, 3] < 75]
    display_dataset(low_attendance[:5], f"LOW ATTENDANCE (< 75%) : {len(low_attendance)} students (first 5)")

    print()
    hard_workers = student_performance[(student_performance[:, 2] > 6) & (average_marks > 80)]
    display_dataset(hard_workers[:5], f"STUDY HOURS > 6 AND AVERAGE > 80 : {len(hard_workers)} students")


def statistical_analysis(student_performance):

    average_marks = student_performance[:, MARKS].mean(axis=1)
    best = np.argmax(average_marks)
    worst = np.argmin(average_marks)

    print()
    print(f"|==== STATISTICAL ANALYSIS (AVERAGE MARKS) ====|\n".center(105))
    print(f"Mean               : {np.mean(average_marks):.2f}")
    print(f"Median             : {np.median(average_marks):.2f}")
    print(f"Variance           : {np.var(average_marks):.2f}")
    print(f"Standard Deviation : {np.std(average_marks):.2f}")
    print(f"Highest Average    : {average_marks[best]:.2f} (Student {int(student_performance[best, 0])})")
    print(f"Lowest Average     : {average_marks[worst]:.2f} (Student {int(student_performance[worst, 0])})")


def transform_data(student_performance):

    print()
    print(f"|==== DATA TRANSFORMATION ====|\n".center(105))

    batches = student_performance.reshape(4, 25, 7)
    print(f"Reshape      : {student_performance.shape} -> {batches.shape}  (4 batches x 25 students x 7 columns)")

    features = student_performance[:, 1:]               # Student ID skip
    minimum = features.min(axis=0)                      # shape (6,)
    maximum = features.max(axis=0)
    normalized_features = (features - minimum) / (maximum - minimum)      # broadcasting
    print(f"Broadcasting : {features.shape} - {minimum.shape}  (min-max normalization)")
    print(f"Normalized range : {normalized_features.min():.1f} to {normalized_features.max():.1f}")

    return np.column_stack((student_performance[:, 0], normalized_features))


def summary_statistics(student_performance):

    print()
    print(f"|==== SUMMARY STATISTICS ====|\n".center(105))

    columns = ["Column", "Min", "Max", "Mean", "Median", "Std", "Q1", "Q3"]
    print("-" * (15 * len(columns)))
    print("".join(f"{name:<15}" for name in columns))
    print("-" * (15 * len(columns)))

    for column in range(1, student_performance.shape[1]):
        values = student_performance[:, column]
        row = [
            values.min(), values.max(), values.mean(), np.median(values),
            values.std(), np.percentile(values, 25), np.percentile(values, 75),
        ]
        print(f"{HEADER[column]:<15}" + "".join(f"{value:<15.2f}" for value in row))


def save_dataset(student_performance, normalized):

    formats = ["%d", "%.1f", "%.1f", "%.1f", "%.2f", "%.2f", "%.2f"]

    np.savetxt("processed_student_data.csv", student_performance, delimiter=",",
               header=",".join(HEADER), comments="", fmt=formats)
    np.save("processed_student_data.npy", student_performance)
    np.savetxt("normalized_student_data.csv", normalized, delimiter=",",
               header=",".join(HEADER), comments="", fmt="%.4f")

    reloaded = np.load("processed_student_data.npy")

    print()
    print(f"|==== SAVE PROCESSED DATASET ====|\n".center(105))
    print("Saved : processed_student_data.csv")
    print("Saved : processed_student_data.npy")
    print("Saved : normalized_student_data.csv")
    print(f"Reload check (npy) : {np.array_equal(student_performance, reloaded)}")


def main():

    student_performance = create_dataset()
    display_dataset(student_performance, "STUDENT PERFORMANCE DATA")
    explore_properties(student_performance)
    student_performance = clean_invalid_values(student_performance)     
    student_performance = handle_missing_values(student_performance)
    display_dataset(student_performance, "CLEANED DATASET")
    filter_records(student_performance)
    statistical_analysis(student_performance)
    normalized = transform_data(student_performance)
    summary_statistics(student_performance)
    save_dataset(student_performance, normalized)


main()
