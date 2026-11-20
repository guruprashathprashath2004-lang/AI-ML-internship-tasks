import pandas as pd
import os

DEFAULT_FILE = "sales_data.csv"
OUTPUT_FILE = "sales_analyzed.csv"

def load_csv_file(file_name):
    sales_datas = pd.read_csv(file_name)
    print(f"{file_name} loaded successfully.")
    return sales_datas

def main():
    sales_data = load_csv_file(DEFAULT_FILE)
    print(pd.DataFrame(sales_data))

main()