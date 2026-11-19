import pandas as pd

DATASET = {
    "Employee_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "Name": ["Kamal", "Nimal", "Sunil", "Amal", "Ruwan", "Kasun", "Dilani", "Nadeesha", "Saman", "Chamari"],
    "Age": [28, 34, 41, 25, 30, 37, 29, 45, 33, 26],
    "Department": ["IT", "HR", "Finance", "Sales", "IT", "Marketing", "HR", "Finance", "Sales", "IT"],
    "Salary": [85000, 72000, 120000, 55000, 95000, 88000, 68000, 135000, 76000, 60000],
    "Experience": [5, 9, 15, 2, 7, 11, 4, 20, 8, 3],
    "Performance_Score": [88, 76, 91, 65, 84, 79, 90, 95, 72, 81],
    }


def display_dataset():
    data = pd.DataFrame(DATASET)
    return data


def main():
    employee_dataset = display_dataset()
    print(employee_dataset)

main()