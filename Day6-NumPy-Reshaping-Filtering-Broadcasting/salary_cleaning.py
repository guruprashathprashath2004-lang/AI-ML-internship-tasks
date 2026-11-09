import numpy as np

EMPLOYEE_NUM = 20
HEADER = ["Employee ID", "Age", "Department", "Salary", "Experience", "Perfomance Score"]
DEPARTMENTS = ["HR", "IT", "Finance", "Sales"]

def create_employee_salary_dataset():

    np.random.seed(42)

    emp_id = np.arange(1, EMPLOYEE_NUM +1).astype(int)
    age = np.random.randint(22, 50, EMPLOYEE_NUM)
    dept_code = np.random.randint(0, len(DEPARTMENTS), EMPLOYEE_NUM)
    salary = np.round(np.random.uniform(30000, 50001, EMPLOYEE_NUM))
    exp = np.random.randint(0, 22, EMPLOYEE_NUM)
    perform = np.random.randint(50, 101, EMPLOYEE_NUM)

    exp = np.minimum(exp, age - 22)

    salary[[3, 9, 14]] = [-45000, -1, -72000]

    return np.column_stack((emp_id, age, dept_code, salary, exp, perform)).astype(object)


def display_dataset(salary_dataset,title):

    if len(salary_dataset) == 0:
        print("No employee records found!")
        return

    print(f"|==== {title} ====|\n".center(90))
    
    print("-" * 90)
    print("" .join(f"{head:<15}" for head in HEADER))
    print("-" * 90)

    for data in salary_dataset:
        print("".join(f"{float(value):<15.2f}" if i == 3 else f"{int(value):<15}" for i, value in enumerate(data)
    ))


def replace_negative_salaries(salary_dataset):

    print(f"\nNegatice Salarie Found : {np.sum(salary_dataset[:, 3] < 0)}")

    valid_avrg = np.mean(salary_dataset[salary_dataset[:, 3] > 0][:, 3])
    print(f"Replaced With Mean     : {valid_avrg:.2f}")

    salary_dataset[salary_dataset[:, 3] < 0, 3] = valid_avrg
    print("\nNegative salaries replaced successfully!\n")


def main():

    salary_dataset = create_employee_salary_dataset()
    display_dataset(salary_dataset, "EMPLOYEE DATA")
    replace_negative_salaries(salary_dataset)
    display_dataset(salary_dataset, "CLEANED EMPLOYEE DATA")


main()
