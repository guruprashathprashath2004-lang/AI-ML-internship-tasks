import pandas as pd
import os

DEFAULT_FILE = "sales_data.csv"
OUTPUT_FILE = "sales_analyzed.csv"
REQUIRED_COLUMNS = ["Order_ID", "Product", "Category", "Quantity", "Price", "Revenue", "City", "Date"]


def load_csv_file(file_name):
    sales_datas = pd.read_csv(file_name)
    print(f"{file_name} loaded successfully.")
    return sales_datas


def missing_columns_check(sales_data):
    all_check = True

    for column in REQUIRED_COLUMNS:
        if column not in sales_data.columns:
            print(f"Missing column: {column}")
            all_check = False

    return all_check

def display_informations(sales_data):

    print("\n|==== DATASET INFORMATION ====|\n")

    print(f"Number of rows    : {len(sales_data)}")
    print(f"Number of columns : {len(sales_data.columns)}")
    print(f"Column names      : {sales_data.columns.to_list()}")

    print("\nData type :")
    print(sales_data.dtypes)

    print("\nMissing values per column :")
    print(sales_data.isnull().sum())

    wrong_revenue = (sales_data["Quantity"] + sales_data["Price"] != sales_data["Revenue"]).sum()
    print(f"\nRows where Revenue is not Price * Quantity : {wrong_revenue}")



def main():
    sales_data = load_csv_file(DEFAULT_FILE)
    print(pd.DataFrame(sales_data))

    if not missing_columns_check(sales_data):
        print("This file does not have the required columns. Program stopped.")
        return
    
    display_informations(sales_data)

main()