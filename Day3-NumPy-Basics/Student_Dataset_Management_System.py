import numpy as np

NUM_STUDENTS = 20
COLUMNS = ["Student_ID", "Age", "Math_Marks", "Science_Marks", "English_Marks", "AI_Marks"]


def main():
    dataset = create_dataset()
    display_dataset(dataset)
    display_properties(dataset)
    compare_list_vs_numpy()

    classrooms = convert_to_3d(dataset)
    print("\n|==== 3D ARRAY (TWO CLASSROOMS) ====|")
    display_properties(classrooms)

    print("\nClassroom 1")
    display_dataset(classrooms[0])
    print("\nClassroom 2")
    display_dataset(classrooms[1])


def create_dataset():
    student_ids = np.arange(1, NUM_STUDENTS + 1)
    ages = np.random.randint(18, 25, NUM_STUDENTS)
    math_marks = np.random.randint(0, 101, NUM_STUDENTS)
    science_marks = np.random.randint(0, 101, NUM_STUDENTS)
    english_marks = np.random.randint(0, 101, NUM_STUDENTS)
    ai_marks = np.random.randint(0, 101, NUM_STUDENTS)

    return np.column_stack(
        (student_ids, ages, math_marks, science_marks, english_marks, ai_marks)
    )


def display_dataset(dataset):
    print("|==== STUDENT DATASET ====|\n")
    print("".join(f"{column:<15}" for column in COLUMNS))
    print("-" * 90)

    for row in dataset:
        print("".join(f"{value:<15}" for value in row))


def display_properties(array):
    print("\n|==== DATASET PROPERTIES ====|\n")
    print(f"Shape      : {array.shape}")
    print(f"Dimensions : {array.ndim}")
    print(f"Size       : {array.size}")
    print(f"Data Type  : {array.dtype}")


def compare_list_vs_numpy():
    print("\n|==== PYTHON LIST VS NUMPY ARRAY ====|")

    py_list = [10, 20, 30, 40]
    np_array = np.array([10, 20, 30, 40])

    # Type
    print("\nList type   :", type(py_list))
    print("NumPy type  :", type(np_array))

    # Multiply by 2
    print("\nList * 2    :", py_list * 2)
    print("NumPy * 2   :", np_array * 2)

    # Add 5 to every value
    print("\nList + 5    : Error (a loop is needed)")
    print("NumPy + 5   :", np_array + 5)

    # Properties
    print("\nNumPy shape :", np_array.shape)
    print("NumPy dtype :", np_array.dtype)
    print("List has no shape or dtype")


def convert_to_3d(dataset):
    # 20 students -> 2 classrooms x 10 students x 6 columns
    return dataset.reshape(2, 10, 6)


main()