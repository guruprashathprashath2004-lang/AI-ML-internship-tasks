import numpy as np

PRODUCTS_NUM = 20
HEADER = ["Product ID", "Monthly Sales", "Revenue", "Profit"]

def create_dataset():
    np.random.seed(42)                                         # Get same datas for every run

    ids = np.arange(101, 101 + PRODUCTS_NUM)                   # PRODUCT IDS
    monthly_sales = np.random.randint(50, 201, PRODUCTS_NUM)   # MONTHLY SALES
    unit_price = np.random.randint(100, 501, PRODUCTS_NUM)     # PER UNIT PRICE

    revenue = monthly_sales * unit_price                       # REVENUE

    profit_margin = np.random.randint(10, 31, PRODUCTS_NUM)    # PORFIT MARGIN
    profit = revenue * profit_margin // 100                    # //100 -> WHOLE NUMBER PROFIT

    return np.column_stack((ids, monthly_sales, revenue, profit))

def display_dataset(sales_dataset):

    print("|==== MONTHLY SALES DATA ====|\n".center(60))

    print("-" * 60)
    print("" .join(f"{head:<15}" for head in HEADER))
    print("-" * 60)

    for row in sales_dataset:
        print("" .join(f"{value:<15}" for value in row))

def main():

    sales_dataset = create_dataset()
    display_dataset(sales_dataset)

main()


