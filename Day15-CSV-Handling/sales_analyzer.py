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

    print()
    print("|==== DATASET INFORMATION ====|\n".center(100))

    print(f"Number of rows    : {len(sales_data)}")
    print(f"Number of columns : {len(sales_data.columns)}")
    print(f"Column names      : {sales_data.columns.to_list()}")

    print("\nData type :")
    print(sales_data.dtypes)

    print("\nMissing values per column :")
    print(sales_data.isnull().sum())

    wrong_revenue = (sales_data["Quantity"] + sales_data["Price"] != sales_data["Revenue"]).sum()
    print(f"\nRows where Revenue is not Price * Quantity : {wrong_revenue}")


def first_and_last(sales_data):
    print()
    print("|==== FIRST 5 RECORDS ====|\n".center(100))
    print(sales_data.head(5).to_string())

    print()
    print("|==== LAST 5 RECORDS ====|\n".center(100))
    print(sales_data.tail(5).to_string())


def total_revenue(sales_data):
    total = sales_data["Revenue"].sum()

    print()
    print("|==== TOTAL REVENUE ====|\n".center(100))
    print(f"Total orders  : {len(sales_data)}")
    print(f"Total revenue : {total:,}") 


def highest_value_order(sales_data):
    best = sales_data["Revenue"].idxmax()        
    order = sales_data.loc[best]                 

    print()
    print("|==== HIGHEST-VALUE ORDER ====|\n".center(100))
    for column in order.index:
        print(f"{column:<12}: {order[column]}")


def main():
    sales_data = load_csv_file(DEFAULT_FILE)

    if not missing_columns_check(sales_data):
        print("This file does not have the required columns. Program stopped.")
        return
    
    display_informations(sales_data)
    first_and_last(sales_data)
    total_revenue(sales_data)
    highest_value_order(sales_data)

main()