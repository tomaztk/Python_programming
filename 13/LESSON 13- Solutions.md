
## LESSON 13: Solutions


```python
import pandas as pd

# 1. Load dataset
df = pd.read_csv("sales_data.csv")

# 2. Display first 5 rows and data types
print(df.head())
print(df.dtypes)

# 3. Create TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# 4. Filter Region = 'East'
east_df = df[df['Region'] == 'East']

# 5. Quantity > 3 and UnitPrice < 100
filtered_df = df[(df['Quantity'] > 3) & (df['UnitPrice'] < 100)]

# 6. Sort by TotalPrice descending
sorted_df = df.sort_values(by='TotalPrice', ascending=False)

# 7. Group by Region, total Quantity
region_qty = df.groupby('Region')['Quantity'].sum()

# 8. Group by SalesRep, avg UnitPrice
salesrep_avg_price = df.groupby('SalesRep')['UnitPrice'].mean()

# 9. Top 3 most sold Products
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(3)

# 10. Total revenue by SalesRep
salesrep_revenue = df.groupby('SalesRep')['TotalPrice'].sum()

# 11. Add OrderMonth
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['OrderMonth'] = df['OrderDate'].dt.month

# 12. Monthly total sales
monthly_sales = df.groupby('OrderMonth')['TotalPrice'].sum()

# 13. Product with highest UnitPrice
max_price_product = df.loc[df['UnitPrice'].idxmax(), 'Product']

# 14. HighValue column
df['HighValue'] = df['TotalPrice'].apply(lambda x: x > 500)

# 15. Count HighValue orders
high_value_count = df['HighValue'].sum()

# 16. Unique values
unique_regions = df['Region'].unique()
unique_products = df['Product'].unique()

# 17. Customers with > 1 order
multiple_orders = df['Customer'].value_counts()
repeat_customers = multiple_orders[multiple_orders > 1].index.tolist()

# 18. Replace 'Monitor' with 'LCD Monitor'
df['Product'] = df['Product'].replace('Monitor', 'LCD Monitor')

# 19. Drop OrderID
df.drop(columns=['OrderID'], inplace=True)

# 20. Export to CSV
df.to_csv("processed_sales_data.csv", index=False)
```

---
