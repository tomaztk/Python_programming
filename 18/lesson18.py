"""import matplotlib.pyplot as plt 
import pandas as pd


data = {
    'Model': ['SedanA', 'SUVB', 'SedanC', 'TruckD', 'SUVE'],
    'Type': ['Sedan', 'SUV', 'Sedan', 'Truck', 'SUV'],
    'Price': [20000, 35000, 22000, 40000, 33000],
    'Sales': [150, 100, 180, 80, 120],
    'Rating': [4.5, 4.2, 4.7, 4.0, 4.3]
}

df = pd.DataFrame(data)

# df.to_csv('car_sales.csv', index=False)

plt.plot(df['Price'], df['Sales'])
plt.title('Car Price vs Sales')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.show()


plt.scatter(df['Rating'], df['Sales'])
plt.title('Rating vs Sales')
plt.xlabel('Rating')
plt.ylabel('Sales')
plt.show()


avg_price = df.groupby('Type')['Price'].mean()

avg_price.plot(kind='bar')
plt.title('Average Price by Car Type')
plt.xlabel('Car Type')
plt.ylabel('Average Price')
plt.show()

"""


####

 

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


data = {
    'Month': [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ],
    'Sales': [305, 356, 410, 489, 512, 590, 620, 610, 598, 675, 700, 730],
    'Expenses': [220, 260, 300, 320, 340, 390, 410, 400, 390, 430, 440, 460]
}
df = pd.DataFrame(data)


df['Profit'] = df['Sales'] - df['Expenses']
df['Sales_MA'] = df['Sales'].rolling(window=3).mean()

 
fig, ax = plt.subplots(figsize=(12, 6))

 
ax.plot(df['Month'], df['Sales'], label='Sales', color='blue', marker='o')
ax.plot(df['Month'], df['Expenses'], label='Expenses', color='red', linestyle='--', marker='x')

ax.bar(df['Month'], df['Profit'], label='Profit', color='green', alpha=0.3)
ax.plot(df['Month'], df['Sales_MA'], label='3-Month MA (Sales)', color='orange', linewidth=2, linestyle='-.')

 
max_idx = df['Sales'].idxmax()
ax.annotate(f'Max Sales: {df["Sales"][max_idx]}',
            xy=(df['Month'][max_idx], df['Sales'][max_idx]),
            xytext=(max_idx, df['Sales'][max_idx]+30),
            textcoords="data",
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            ha='center')


ax.set_title('Sales, Expenses, Profit and Trendline (Monthly)')
ax.set_xlabel('Month')
ax.set_ylabel('Amount ($)')
ax.grid(True, linestyle=':', linewidth=0.5)
ax.legend()
plt.tight_layout()
plt.show()

 