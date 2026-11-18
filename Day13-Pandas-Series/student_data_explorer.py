import pandas as pd

names = pd.Series(["Kamal", "Nimal", "Sunil", "Amal", "Ruwan", "Kasun", "Dilani", "Nadeesha", "Saman", "Chamari"])
ages = pd.Series([20, 21, 19, 22, 20, 21, 19, 23, 22, 20])
python_marks = pd.Series([85, 72, 91, 68, 77, 95, 80, 88, 35, 74])
ai_marks = pd.Series([78, 65, 88, 59, 82, 90, 70, 92, 30, 66])

total = python_marks + ai_marks
average = total / 2

