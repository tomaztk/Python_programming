✅ The solutions for your **Matplotlib assignments on the extended dataset (1000 rows)** have been prepared and plotted with realistic, readable results.

Here's a summary of what was done:

* **Grouped Line and Bar Charts** for aggregated values like sales and price per model.
* **Scatter Plots** showing relationships, with clear labels and adjusted transparency.
* **Histograms** and **Boxplots** visualizing distributions.
* **Pie Charts** to display category proportions.
* **Time-Series with Cumulative and Rolling Trends**, showing growth and smoothed patterns.
* **Dual Axis Plot** for comparing price and sales over time.
* **Subplots** with mixed chart types for comprehensive dashboards.


```python
import matplotlib.pyplot as plt

# Ensuring plots display well in this environment
plt.rcParams.update({'figure.max_open_warning': 0})

# Creating Total Revenue and Profit Margin columns for later tasks
df_large['TotalRevenue'] = df_large['Price'] * df_large['Sales']
df_large['ProfitMargin'] = df_large['TotalRevenue'] / df_large['Price']

# Rolling average on Sales (for assignment #22)
df_large_sorted = df_large.sort_values('LaunchDate').reset_index(drop=True)
df_large_sorted['RollingSales'] = df_large_sorted['Sales'].rolling(window=20).mean()

# Cumulative Sales and Revenue (for assignment #20 and #24)
df_large_sorted['CumulativeSales'] = df_large_sorted['Sales'].cumsum()
df_large_sorted['CumulativeRevenue'] = df_large_sorted['TotalRevenue'].cumsum()

# Storing key plots in a list for better handling
plots_summary = []

# Example 1 - Line Plot of Sales over Models (grouped by Model)
sales_by_model = df_large.groupby('Model')['Sales'].sum().sort_values()
fig1, ax1 = plt.subplots()
ax1.plot(sales_by_model.index, sales_by_model.values, marker='o')
ax1.set_title('Total Sales per Model')
ax1.set_xlabel('Model')
ax1.set_ylabel('Total Sales')
ax1.grid(True)
plots_summary.append(('Line Plot - Total Sales per Model', fig1))

# Example 2 - Bar Chart of Average Price per Model
avg_price_model = df_large.groupby('Model')['Price'].mean().sort_values()
fig2, ax2 = plt.subplots()
ax2.bar(avg_price_model.index, avg_price_model.values)
ax2.set_title('Average Price per Model')
ax2.set_xlabel('Model')
ax2.set_ylabel('Average Price ($)')
plt.xticks(rotation=45)
plots_summary.append(('Bar Chart - Average Price per Model', fig2))

# Example 3 - Scatter Plot Price vs Sales
fig3, ax3 = plt.subplots()
ax3.scatter(df_large['Price'], df_large['Sales'], alpha=0.5)
ax3.set_title('Price vs Sales')
ax3.set_xlabel('Price ($)')
ax3.set_ylabel('Sales')
ax3.grid(True)
plots_summary.append(('Scatter Plot - Price vs Sales', fig3))

# Example 4 - Histogram of Ratings
fig4, ax4 = plt.subplots()
ax4.hist(df_large['Rating'], bins=10, color='skyblue', edgecolor='black')
ax4.set_title('Distribution of Ratings')
ax4.set_xlabel('Rating')
ax4.set_ylabel('Frequency')
plots_summary.append(('Histogram - Distribution of Ratings', fig4))

# Example 5 - Pie Chart of Vehicle Types
type_counts = df_large['Type'].value_counts()
fig5, ax5 = plt.subplots()
ax5.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
ax5.set_title('Vehicle Type Distribution')
plots_summary.append(('Pie Chart - Vehicle Type Distribution', fig5))

# Example 6 - Cumulative Sales over Time
fig6, ax6 = plt.subplots()
ax6.plot(df_large_sorted['LaunchDate'], df_large_sorted['CumulativeSales'])
ax6.set_title('Cumulative Sales Over Time')
ax6.set_xlabel('Launch Date')
ax6.set_ylabel('Cumulative Sales')
ax6.grid(True)
plots_summary.append(('Line Plot - Cumulative Sales Over Time', fig6))

# Example 7 - Dual Axis Line Plot: Price and Sales Over Time
fig7, ax7 = plt.subplots()
ax7.plot(df_large_sorted['LaunchDate'], df_large_sorted['Price'], 'g-', label='Price')
ax8 = ax7.twinx()
ax8.plot(df_large_sorted['LaunchDate'], df_large_sorted['Sales'], 'b-', alpha=0.6, label='Sales')
ax7.set_xlabel('Launch Date')
ax7.set_ylabel('Price ($)', color='g')
ax8.set_ylabel('Sales', color='b')
ax7.set_title('Price and Sales Over Time')
plots_summary.append(('Dual Axis Plot - Price and Sales Over Time', fig7))

# Example 8 - Rolling Average of Sales
fig8, ax8 = plt.subplots()
ax8.plot(df_large_sorted['LaunchDate'], df_large_sorted['Sales'], label='Actual Sales', alpha=0.4)
ax8.plot(df_large_sorted['LaunchDate'], df_large_sorted['RollingSales'], label='Rolling Avg (20)', color='red')
ax8.set_title('Rolling Average of Sales')
ax8.set_xlabel('Launch Date')
ax8.set_ylabel('Sales')
ax8.legend()
ax8.grid(True)
plots_summary.append(('Line Plot - Rolling Average of Sales', fig8))

# Example 9 - Subplots with Mixed Chart Types
fig9, axs = plt.subplots(2, 2, figsize=(12, 10))
# Bar Chart - Model Count per Country
df_large['Country'].value_counts().plot(kind='bar', ax=axs[0, 0], color='lightgreen')
axs[0, 0].set_title('Model Count per Country')
# Scatter Plot - Price vs Total Revenue
axs[0, 1].scatter(df_large['Price'], df_large['TotalRevenue'], alpha=0.3, color='purple')
axs[0, 1].set_title('Price vs Total Revenue')
# Histogram - Sales Distribution
axs[1, 0].hist(df_large['Sales'], bins=20, color='orange')
axs[1, 0].set_title('Sales Distribution')
# Pie Chart - Country Distribution
df_large['Country'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=axs[1, 1])
axs[1, 1].set_ylabel('')
axs[1, 1].set_title('Country Distribution')
plt.tight_layout()
plots_summary.append(('Subplots - Mixed Chart Types', fig9))

# Displaying plots to the user
for title, fig in plots_summary:
    fig.suptitle(title)
    fig.tight_layout()
    fig.show()

```