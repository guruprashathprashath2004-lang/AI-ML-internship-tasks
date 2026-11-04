import numpy as np

student = 20
column = ["Student_ID", "Age", "Math_Marks", "Science_marks", "English_marks", "AI_Marks"]



def main():
    dataset = create_dataset()
    display_dataset(dataset)
    display_properties(dataset)
    compare_list_vs_numpy()

def create_dataset():
    id = np.arange(1, student + 1,)
    ages = np.random.randint(15, 17, student)
    math_marks = np.random.randint(0, 101, student)
    sci_marks = np.random.randint(0, 101, student)
    eng_marks = np.random.randint(0, 101, student)
    ai_marks = np.random.randint(0, 101, student)

    return np.column_stack((id, ages, math_marks, sci_marks, eng_marks, ai_marks))

def display_dataset(dataset):
    print("|==== STUDENT DATASET ====|\n")
    print("" .join(f"{col:<15}" for col in column))
    print("-" * 90)

    for row in dataset:
        print("".join(f"{value:<15}" for value in row))


def display_properties(array):
    print("\n|==== DATASET PROPERTIES ====|")
    print(f"\nShape     : {array.shape}")
    print(f"Dimentions: {array.ndim}")
    print(f"Size      : {array.size}")
    print(f"Dtat Type : {array.dtype}")

def compare_list_vs_numpy():
    print("\n|==== PYHTON LIST VS NUMPY ARRAY ====|")

    py_lst = [10, 20, 30, 40]
    np_arr = np.array([10, 20, 30, 40])

    # Type
    print("\nList type  : ", type(py_lst))
    print("Numpy type : ", type(np_arr))

    # Multiply by 2
    print("\nList * 2  :", py_lst * 2)
    print("Numpy * 2 :", np_arr * 2)

    # Add 5 to every value
    print("\nList + 5  : Error(Want a loop to display value)")
    print("Numpy + 5 :", np_arr + 5)

    # Properties
    print("\nNumPy shape:", np_arr.shape)
    print("NumPy dtype:", np_arr.dtype)
    print("List has no shape or dtype")

main()

