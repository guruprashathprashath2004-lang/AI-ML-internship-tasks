import numpy as np

student = 20
column = ["Student_ID", "Age", "Math_Marks", "Science_marks", "English_marks", "AI_Marks"]

def create_dataset():
    id = np.arange(1, student + 1,)
    ages = np.random.randint(15, 17, student)
    math_marks = np.random.randint(0, 101, student)
    sci_marks = np.random.randint(0, 101, student)
    eng_marks = np.random.randint(0, 101, student)
    ai_marks = np.random.randint(0, 101, student)

    return np.column_stack((id, ages, math_marks, sci_marks, eng_marks, ai_marks))

def display_properties(array):
    print("|==== DATASET PROPERTIES ====|")
    print(f"Shape     : {array.shape}")
    print(f"Dimentions: {array.ndim}")
    print(f"Size      : {array.size}")
    print(f"Dtat Type : {array.dtype}")

def main():
    table = create_dataset()
    print("".join(f"{col:<15}" for col in column))
    print("-" * 90)

    for row in table:
        print("".join(f"{value:<15}" for value in row))

    prop = display_properties(table)
    print(prop)


main()
