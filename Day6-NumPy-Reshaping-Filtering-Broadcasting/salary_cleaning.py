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


def main():

    salary_dataset = create_employee_salary_dataset()
    print(salary_dataset)


main()
