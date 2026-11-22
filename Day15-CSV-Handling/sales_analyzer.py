import pandas as pd
import os

DEFAULT_FILE = "sales_data.csv"
OUTPUT_FILE = "sales_analyzed.csv"
REQUIRED_COLUMNS = ["Order_ID", "Product", "Category", "Quantity", "Price", "Revenue", "City", "Date"]

HIGH_ORDER = 200000      
MEDIUM_ORDER = 30000   

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


def save_analyzed_csv(sales_data):
    levels = []

    for i in range(len(sales_data)):
        revenue = sales_data["Revenue"].iloc[i]

        if revenue >= HIGH_ORDER:
            levels.append("High")
        elif revenue >= MEDIUM_ORDER:
            levels.append("Medium")
        else:
            levels.append("Low")

    sales_data["Order_Level"] = levels
    sales_data.to_csv(OUTPUT_FILE, index=False)

    print("\n|==== ANALYZED CSV ====|\n")
    print(f"Saved to {OUTPUT_FILE}")
    print(f"High orders   (Revenue >= {HIGH_ORDER}) : {(sales_data['Order_Level'] == 'High').sum()}")
    print(f"Medium orders (Revenue >= {MEDIUM_ORDER}) : {(sales_data['Order_Level'] == 'Medium').sum()}")
    print(f"Low orders                      : {(sales_data['Order_Level'] == 'Low').sum()}")

    check = pd.read_csv(OUTPUT_FILE)       
    print(f"\nCheck: {OUTPUT_FILE} has {len(check)} rows and {len(check.columns)} columns")


def get_filename():
    while True:
        filename = input(f"Enter CSV filename (press Enter for {DEFAULT_FILE}): ").strip()

        if filename == "":
            filename = DEFAULT_FILE

        if not filename.endswith(".csv"):
            print("Please enter a .csv file.")
        elif not os.path.exists(filename):
            print("File not found. Try again.")
        else:
            return filename

        
def main():
    filename = get_filename()
    sales_data = load_csv_file(filename)

    if not missing_columns_check(sales_data):
        print("This file does not have the required columns. Program stopped.")
        return
    
    display_informations(sales_data)
    first_and_last(sales_data)
    total_revenue(sales_data)
    highest_value_order(sales_data)
    save_analyzed_csv(sales_data)

main()