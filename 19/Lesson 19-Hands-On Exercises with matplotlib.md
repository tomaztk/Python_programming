### Lesson 19 — Hands-On Exercises with **Matplotlib**

---
#### Data:

```Python
import numpy as np
import pandas as pd

# Define the number of synthetic rows to generate
num_rows = 1000

# Possible values to sample from
models = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu',
          'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega']
types = ['Hatchback', 'Sedan', 'SUV', 'Truck']
countries = ['Japan', 'Germany', 'USA']

# Random data generation
np.random.seed(42)
extended_data = {
    'Model': np.random.choice(models, num_rows),
    'Price': np.random.randint(15000, 40000, num_rows),
    'Sales': np.random.randint(100, 1000, num_rows),
    'Rating': np.round(np.random.uniform(2.5, 5.0, num_rows), 1),
    'Type': np.random.choice(types, num_rows),
    'Country': np.random.choice(countries, num_rows),
    'LaunchDate': pd.to_datetime(np.random.choice(pd.date_range('2021-01-01', '2025-01-01'), num_rows))
}

df_large = pd.DataFrame(extended_data)
df_large.head()
```

---

### **Assignments with Titles & Purposes**

1. **Line Plot of Sales Over Models**
   Plot a simple line chart to visualize how sales vary across different vehicle models.

2. **Bar Chart of Price per Model**
   Create a vertical bar chart showing the price of each vehicle model.

3. **Horizontal Bar Chart of Sales per Model**
   Use a horizontal bar chart to represent sales data per model — ideal for longer model names.

4. **Scatter Plot of Price vs Sales**
   Visualize the relationship between vehicle price and sales with a scatter plot.

5. **Histogram of Ratings**
   Display the distribution of customer ratings using a histogram.

6. **Boxplot of Prices**
   Plot a boxplot to detect outliers and visualize the spread of vehicle prices.

7. **Pie Chart of Vehicle Type Distribution**
   Show the proportion of different vehicle types in the dataset with a pie chart.

8. **Bar Chart of Average Price per Vehicle Type**
   Calculate the average price for each type of vehicle and display it in a bar chart.

9. **Line Chart of Sales Over Launch Dates**
   Visualize sales over time using a line chart with launch dates on the x-axis.

10. **Bar Chart of Model Count per Country**
    Plot the number of models produced per country using a bar chart.

11. **Scatter Plot with Color-Coded Vehicle Types**
    Add a color-coded category to a scatter plot to distinguish vehicle types visually.

12. **Grouped Bar Chart of Sales by Country and Type**
    Use a grouped bar chart to compare sales by country and vehicle type.

13. **Stacked Bar Chart of Sales by Type within Each Country**
    Represent cumulative sales per country with a stacked bar chart showing vehicle types.

14. **Multiple Line Charts of Sales Trends per Vehicle Type**
    Plot individual sales trends over time for each vehicle type on the same chart.

15. **Create "Total Revenue" Column and Scatter Plot with Marker Size**
    Add a column calculating total revenue (Price × Sales) and plot a scatter chart with marker sizes representing revenue.

16. **Pie Chart of Market Share by Country**
    Aggregate data to display each country’s share of total models in a pie chart.

17. **Histogram of Prices with Custom Bin Size**
    Adjust the number of bins in a histogram to control grouping of price values.

18. **Boxplot of Ratings Grouped by Vehicle Type**
    Compare distributions of ratings for each vehicle type using grouped boxplots.

19. **Create "Profit Margin" Column and Scatter Plot with Color Encoding**
    After creating a new column for profit margin (e.g., Revenue divided by Price), visualize it on a scatter plot using color to encode margin.

20. **Cumulative Sales Over Time Line Plot**
    Calculate cumulative sales and plot them over time to analyze growth trends.

21. **Bar Chart with Data Labels (Annotations)**
    Enhance a bar chart by adding labels directly on top of each bar for better readability.

22. **Rolling Average of Sales with Line Chart**
    Compute a rolling average of sales (e.g., over 3 models) and plot both the original and smoothed data.

23. **Dual Axis Line Plot of Price and Sales Over Time**
    Plot price and sales on the same chart using two y-axes for clear comparison.

24. **Time Series of Total Revenue with Cumulative Sum**
    Plot a cumulative sum of total revenue over time to visualize income growth.

25. **Subplots with Mixed Chart Types in One Figure**
    Practice using subplots to display multiple chart types (e.g., bar chart, scatter plot, histogram, pie chart) in a single figure.

