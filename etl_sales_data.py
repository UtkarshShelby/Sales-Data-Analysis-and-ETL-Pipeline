import pandas as pd
import mysql.connector

# Step 1: Load CSV data
df = pd.read_csv("sales_data.csv")
df['order_date'] = pd.to_datetime(df['order_date'])
df['category'] = df['category'].astype('category')
print(df.dtypes)
# Step 2: Database connection config
conn = mysql.connector.connect(
    host="localhost",
    user="root",
password="SQL@123",  # <-- Replace with your actual MySQL password
    database="sales_project"
)
cursor = conn.cursor()

# Step 3: Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales_data (order_id, product_name, category, price, quantity, order_date, customer_region, payment_method)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

# Step 4: Commit and close
conn.commit()
cursor.close()
conn.close()

print(" Data loaded successfully into MySQL!")
