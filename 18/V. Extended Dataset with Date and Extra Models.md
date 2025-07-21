
## **V. Extended Dataset with Date and Extra Models**

```python
import pandas as pd

data = {
    'Model': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu'],
    'Price': [15000, 18000, 20000, 22000, 25000, 27000, 30000, 32000, 35000, 40000, 28000, 23000],
    'Sales': [800, 750, 500, 450, 400, 380, 300, 250, 200, 150, 360, 420],
    'Rating': [4.5, 4.2, 4.8, 4.0, 3.9, 3.8, 3.5, 3.4, 3.2, 3.0, 3.6, 4.1],
    'Type': ['Hatchback', 'Hatchback', 'Sedan', 'Sedan', 'SUV', 'SUV', 'SUV', 'Truck', 'Truck', 'Truck', 'SUV', 'Sedan'],
    'Country': ['Japan', 'Japan', 'Germany', 'Germany', 'USA', 'USA', 'USA', 'USA', 'Japan', 'Germany', 'USA', 'Germany'],
    'LaunchDate': pd.to_datetime(['2021-01-01', '2021-03-01', '2021-05-01', '2021-06-01',
                                   '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01',
                                   '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01'])
}

df = pd.DataFrame(data)
```

---

##  **Visual Examples Covering All Graph Types & Layers**

---

### **1) Line Plot — Price over Time**

```python
import matplotlib.pyplot as plt

plt.plot(df['LaunchDate'], df['Price'], marker='o', color='blue', label='Price Trend')
plt.title('Price Over Time')
plt.xlabel('Launch Date')
plt.ylabel('Price')
plt.grid(True)
plt.legend()
plt.show()
```

---

### **2) Scatter Plot with Trend Line — Rating vs Sales**

```python
import numpy as np

plt.scatter(df['Rating'], df['Sales'], color='purple', label='Data Points')

# Trend Line (Linear Fit)
coeff = np.polyfit(df['Rating'], df['Sales'], 1)
poly_eqn = np.poly1d(coeff)
plt.plot(df['Rating'], poly_eqn(df['Rating']), color='red', linewidth=2, label='Trend Line')

plt.title('Rating vs Sales with Trend Line')
plt.xlabel('Rating')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
```

---

### **3) Bar Plot — Average Price by Type**

```python
avg_price_type = df.groupby('Type')['Price'].mean()

plt.bar(avg_price_type.index, avg_price_type.values, color='skyblue')
plt.title('Average Price by Car Type')
plt.xlabel('Car Type')
plt.ylabel('Average Price')
plt.grid(axis='y')
plt.show()
```

---

### **4) Histogram — Sales Distribution**

```python
plt.hist(df['Sales'], bins=5, color='green', edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```

---

### **5) Count Plot (Bar Plot) — Count of Models per Country**

```python
country_counts = df['Country'].value_counts()

plt.bar(country_counts.index, country_counts.values, color='orange')
plt.title('Number of Models by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.grid(axis='y')
plt.show()
```

---

### **6) Box Plot — Price Distribution by Type (Using Seaborn)**

```python
import seaborn as sns

sns.boxplot(x='Type', y='Price', data=df)
plt.title('Price Distribution by Car Type')
plt.grid(True)
plt.show()
```

---

### **7) Time Series Line Chart — Sales over Time with Annotation**

```python
plt.plot(df['LaunchDate'], df['Sales'], marker='o', label='Sales Over Time')
plt.title('Sales Over Time with Highlight')
plt.xlabel('Launch Date')
plt.ylabel('Sales')
plt.grid(True)

# Highlight the highest sales point
best = df[df['Sales'] == df['Sales'].max()]
plt.annotate('Best Sales', xy=(best['LaunchDate'].values[0], best['Sales'].values[0]),
             xytext=(best['LaunchDate'].values[0], best['Sales'].values[0]+100),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.legend()
plt.show()
```

---

### **8) Pie Chart — Market Share by Country**

```python
country_sales = df.groupby('Country')['Sales'].sum()

plt.pie(country_sales.values, labels=country_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Market Share by Country')
plt.show()
```

---

### **9) Multi-Layer Plot — Sales vs Price Colored by Type**

```python
colors = {'Hatchback':'blue', 'Sedan':'green', 'SUV':'red', 'Truck':'purple'}

plt.figure(figsize=(8,6))
for t in df['Type'].unique():
    subset = df[df['Type'] == t]
    plt.scatter(subset['Price'], subset['Sales'], color=colors[t], label=t)

plt.title('Sales vs Price by Car Type')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
```

---

### **10) Correlation Heatmap — Numeric Variables**

```python
sns.heatmap(df[['Price', 'Sales', 'Rating']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
```

---

## **Reusable Plotting Function Example**

```python
def plot_with_reference(df, x, y, title='', xlabel='', ylabel='', reference=None, annotate=False):
    plt.scatter(df[x], df[y], color='teal', label='Data Points')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    if reference == 'mean':
        mean_val = df[y].mean()
        plt.axhline(y=mean_val, color='red', linestyle='--', label=f'Mean {y}: {mean_val:.2f}')
    
    if annotate:
        for i in range(len(df)):
            plt.text(df[x].iloc[i], df[y].iloc[i]+10, df['Model'].iloc[i], fontsize=8)

    plt.legend()
    plt.show()
```

### Example Use:

```python
plot_with_reference(df, 'Price', 'Sales', 
                    title='Price vs Sales with Mean Line and Annotations', 
                    xlabel='Price', ylabel='Sales',
                    reference='mean', annotate=True)
```

---

### **Modified Multi-Scatter Plot with Reference and Annotations**

```python
def multi_plot_with_reference(df, x_vars, y, colors, title='', xlabel='', ylabel='', reference=None, annotate=False):
    plt.figure(figsize=(8,6))
    
    for i, x in enumerate(x_vars):
        plt.scatter(df[x], df[y], color=colors[i], label=f'{x} vs {y}')
        
        if reference == 'mean':
            mean_val = df[y].mean()
            plt.axhline(y=mean_val, color='red', linestyle='--', label=f'Mean {y}: {mean_val:.2f}')
        
        if annotate:
            for j in range(len(df)):
                plt.text(df[x].iloc[j], df[y].iloc[j]+10, df['Model'].iloc[j], fontsize=8, color=colors[i])

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()
```

---

### **Plotting Both — Price vs Sales and Rating vs Sales Together**

```python
multi_plot_with_reference(
    df,
    x_vars=['Price', 'Rating'],
    y='Sales',
    colors=['blue', 'green'],
    title='Price & Rating vs Sales with Mean Line and Annotations',
    xlabel='Price / Rating',
    ylabel='Sales',
    reference='mean',
    annotate=True
)
```

---

### What This Does:

* Plots **Price vs Sales** in **blue**
* Plots **Rating vs Sales** in **green**
* Adds the **mean Sales reference line** in **red**
* Annotates all points with model names in corresponding colors
* Includes a legend to differentiate the two series

---

### Please note:

* Because **Price** and **Rating** have different scales, this works as an **exploratory visual**,
  but if you want a more accurate comparison, you may consider:

  * Scaling variables (e.g., min-max normalization)
  * Using twin axes with `plt.twinx()`
  * Creating separate subplots


---


## **Summary of What’s Covered**

| Graph Type               | Example                      |
| ------------------------ | ---------------------------- |
| Line Plot                | Price Over Time              |
| Scatter Plot + Trend     | Rating vs Sales              |
| Bar Plot                 | Average Price by Type        |
| Histogram                | Sales Distribution           |
| Count Plot               | Models per Country           |
| Box Plot                 | Price by Type                |
| Time Series + Annotation | Sales Over Time              |
| Pie Chart                | Market Share by Country      |
| Multi-Layer Scatter      | Sales vs Price by Type       |
| Heatmap                  | Correlation Matrix           |
| Custom Function          | Reusable Scatter + Reference |

---

## **Conclusion**

With this extended dataset and examples, you’ve got:

*  Different variable combinations
* Visual layering (trend lines, annotations, reference lines)
* Statistical plots and summaries
* Time series and categorical data handling
* Reusable plotting patterns for your lessons




