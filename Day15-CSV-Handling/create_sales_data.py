import pandas as pd
import random

random.seed(42)

TOTAL_ORDERS = 100
OUTPUT_FILE = "sales_data.csv"

HEADER = ["Order_ID", "Product", "Category", "Quantity", "Price", "Revenue", "City", "Date"]

# [product, category, unit price]
PRODUCTS = [
    ["Laptop", "Electronics", 150000],
    ["Smartphone", "Electronics", 90000],
    ["Headphones", "Electronics", 12000],
    ["Rice 5kg", "Groceries", 1500],
    ["Tea Packet", "Groceries", 650],
    ["Coconut Oil", "Groceries", 900],
    ["T-Shirt", "Clothing", 2500],
    ["Jeans", "Clothing", 6500],
    ["Sarong", "Clothing", 3200],
    ["Notebook", "Stationery", 350],
    ["Pen Box", "Stationery", 450],
    ["Backpack", "Stationery", 5500],
]

CITIES = ["Badulla", "Colombo", "Kandy", "Galle", "Jaffna", "Matara", "Kurunegala"]

def create_sales_dataset():
    datas = []

    for i in range(TOTAL_ORDERS):
        order_id = f"ORD {1001 + i}"

        item = random.choice(PRODUCTS)
        product = item[0]
        category = item[1]
        price = item[2]

        quantity = random.randint(1, 20)
        revenue = quantity * price

        city = random.choice(CITIES)

        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date = f"2026-{month:02d}-{day:02d}"

        datas.append([order_id, product, category, quantity, price, revenue, city, date])

    return datas


def savedataset(sales_dataset):

    sales_dataset = pd.DataFrame(sales_dataset, columns=HEADER)
    sales_dataset.to_csv(OUTPUT_FILE, index=False)

    print(f"{OUTPUT_FILE} created with 100 records.")

def main():
    sales_dataset = create_sales_dataset()
    savedataset(sales_dataset)

main()

