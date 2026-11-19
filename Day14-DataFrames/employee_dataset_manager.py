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

    print(f"|==== ALL EMPLOYEE DATASET ====|\n".center(80))
    data = pd.DataFrame(DATASET)
    return data


def display_columns(employee_dataset):

    print()
    print(f"|==== SELECTED COLUMNS ====|\n".center(60))
    data = employee_dataset[["Name", "Department", "Experience", "Performance_Score"]]
    print(data)


def first_and_last_5(employee_dataset):

    first_5 = employee_dataset.head(5)
    last_5 = employee_dataset.tail(5)

    print()
    print(f"|==== FIRST 5 EMPLOYEES ====|\n".center(80))
    print(first_5)

    print()
    print(f"|==== LAST 5 EMPLOYEES ====|\n".center(80))
    print(last_5)


def bonus_column(employee_dataset):

    employee_dataset["Bonus"] = employee_dataset["Salary"] * 0.1

    print()
    print(f"|==== ALL EMPLOYEE DATASET (WITH BONUS COLUMN(SALARY * 0.1)) ====|\n".center(90))
    print(employee_dataset)


def rename_column(employee_dataset):

    rename = employee_dataset.rename(columns={"Salary" : "Base_Salary"})
    return rename


def remove_column(renamed_coulmn):
    remove = renamed_coulmn.drop(columns=["Age"])
    return remove


def select_employee(removed_column):

    print()
    loc = removed_column.set_index("Employee_ID")
    print("|==== SELECTED USING 'loc' ====|\n")
    print(loc.loc[1001])

    print()
    iloc = removed_column.iloc[3]
    print("|==== SELECTED USING 'iloc' ====|\n")
    print(iloc)


def bonus_feature(removed_column):

    print()
    print(f"|==== AFTER ADDING Total_Salary COLUMN ====|\n".center(100))
    removed_column["Total_Salary"] = removed_column["Base_Salary"] + removed_column["Bonus"]
    print(removed_column)



def main():

    employee_dataset = display_dataset()
    print(employee_dataset)
    display_columns(employee_dataset)
    first_and_last_5(employee_dataset)
    bonus_column(employee_dataset)

    renamed_coulmn = rename_column(employee_dataset)
    print()
    print(f"|==== AFTER RENAMING Salary TO Base_Salary ====|\n".center(95))
    print(renamed_coulmn.to_string())

    removed_column = remove_column(renamed_coulmn)
    print()
    print(f"|==== AFTER REMOVING THE Age COLUMN ====|\n".center(85))
    print(removed_column)

    select_employee(removed_column)
    bonus_feature(removed_column)

main()