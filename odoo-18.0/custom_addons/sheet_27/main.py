import psycopg2
import pandas as pd

# Read CSV file
csv_file = r"/home/madhuvanksi277/Desktop/Training/sheet_27/orders.csv"
df = pd.read_csv(csv_file)

# PostgreSQL connection details
conn = psycopg2.connect(
    dbname="store_db",
    user="postgres",      
    password="ksolves",  
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS store_order (
        order_id INT PRIMARY KEY,
        customer_name VARCHAR(100),
        product VARCHAR(100),
        quantity INT,
        price NUMERIC(10,2),
        order_date DATE
    )
""")
print("✅ Table verified or created successfully!")


# Insert CSV data into PostgreSQL
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO store_order (order_id, customer_name, product, quantity, price, order_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO NOTHING
    """, tuple(row))

conn.commit()
print("CSV data inserted successfully!")

# Fetch & display inserted data
cursor.execute("SELECT * FROM store_order")
rows = cursor.fetchall()
print("\nInserted Data:")
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
