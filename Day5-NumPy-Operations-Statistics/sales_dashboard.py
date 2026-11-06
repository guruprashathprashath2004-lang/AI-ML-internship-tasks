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


def total_revenue(sales_dataset):

    print()
    print("|==== CALCULATIONS ====|\n".center(60))

    total_rev = np.sum(sales_dataset[:,2])
    print("1. TOTAL REVENUE   : ", total_rev)


def average_revenue(sales_dataset):

    avg_revenue =  np.mean(sales_dataset[:,2])
    print("2. AVERAGE REVENUE : ", avg_revenue)


def highest_and_lowest(sales_dataset):

    highest_sales = np.max(sales_dataset[:, 1])
    lowest_sales = np.min(sales_dataset[:, 1])
    print(f"3. HIGHEST SALES : {highest_sales} units")
    print(f"4. LOWEST SALES  : {lowest_sales} units")


def profit(sales_dataset):

    total_profit = np.sum(sales_dataset[:, 3])
    total_revenue = np.sum(sales_dataset[:, 2].astype(float))

    profit_percentage = (total_profit / total_revenue) * 100

    print("5. TOTAL PROFIT      : ", total_profit)
    print(f"6. PROFIT PERCENTAGE : {profit_percentage:.2f} %")


def best_and_worst_selling(sales_dataset):

    best = sales_dataset[np.argmax(sales_dataset[:, 1])]
    worst = sales_dataset[np.argmin(sales_dataset[:, 1])]

    print(f"7. BEST SELLING PRODUCT  : Product ID {best[0]} -> {best[1]} units")
    print(f"8. WORST SELLING PRODUCT : Product ID {worst[0]} -> {worst[1]} units")


def top_5_products(sales_dataset):
    
    print()
    print("|==== TOP 5 BY REVENUE ====|\n".center(60))
    
    print("-" * 60)
    print("" .join(f"{head:<15}" for head in HEADER))
    print("-" * 60)
    
    products = np.argsort(sales_dataset[:, 2])[::-1]
    full_details = sales_dataset[products[:5]]

    for data in full_details:
        print("" .join(f"{value:<15}" for value in data))


def main():

    sales_dataset = create_dataset()
    display_dataset(sales_dataset)
    total_revenue(sales_dataset)
    average_revenue(sales_dataset)
    highest_and_lowest(sales_dataset)
    profit(sales_dataset)
    best_and_worst_selling(sales_dataset)
    top_5_products(sales_dataset)

main()


