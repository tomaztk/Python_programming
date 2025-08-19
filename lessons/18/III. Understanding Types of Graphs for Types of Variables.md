
## **III. Understanding Types of Graphs for Types of Variables**

Choosing the right type of graph depends on the nature of the variables you are analyzing.
Here’s a quick summary:

| **Variable Type**         | **Best Graph Type** | **Example**            |
| ------------------------- | ------------------- | ---------------------- |
| Continuous vs Continuous  | Scatter Plot        | Rating vs Sales        |
| Categorical vs Continuous | Bar Plot            | Type vs Average Price  |
| Single Continuous         | Histogram           | Distribution of Prices |
| Single Categorical        | Count Plot          | Count of Car Types     |

---

### **Extended Dataset with Extra Columns**

We will add a `Type` column (car category) and a `Country` column (origin), commonly used for categorical comparisons.

```python
import pandas as pd

data = {
    'Model': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa'],
    'Price': [15000, 18000, 20000, 22000, 25000, 27000, 30000, 32000, 35000, 40000],
    'Sales': [800, 750, 500, 450, 400, 380, 300, 250, 200, 150],
    'Rating': [4.5, 4.2, 4.8, 4.0, 3.9, 3.8, 3.5, 3.4, 3.2, 3.0],
    'Type': ['Hatchback', 'Hatchback', 'Sedan', 'Sedan', 'SUV', 'SUV', 'SUV', 'Truck', 'Truck', 'Truck'],
    'Country': ['Japan', 'Japan', 'Germany', 'Germany', 'USA', 'USA', 'USA', 'USA', 'Japan', 'Germany']
}

df = pd.DataFrame(data)
```

---

### **A) Continuous vs Continuous — Scatter Plot**

Used to explore the relationship between two continuous variables.

```python
import matplotlib.pyplot as plt

plt.scatter(df['Rating'], df['Sales'], color='teal', alpha=0.7)
plt.title('Rating vs Sales')
plt.xlabel('Rating')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
```

**Use When:**

* Both variables are numerical.
* You want to see trends, patterns, or correlations.

---

### **B) Categorical vs Continuous — Bar Plot (Type vs Average Price)**

Compare means or aggregates across categories.

```python
avg_price = df.groupby('Type')['Price'].mean()

avg_price.plot(kind='bar', color='skyblue')
plt.title('Average Price by Car Type')
plt.xlabel('Car Type')
plt.ylabel('Average Price')
plt.grid(axis='y')
plt.show()
```

**Alternative with Matplotlib:**

```python
plt.bar(avg_price.index, avg_price.values, color='coral')
plt.title('Average Price by Car Type')
plt.xlabel('Car Type')
plt.ylabel('Average Price')
plt.grid(axis='y')
plt.show()
```

**Use When:**

* You want to compare numerical summaries (mean, sum) between categories.

---

### **C) Single Continuous Variable — Histogram (Price Distribution)**

Visualize the distribution of a continuous variable.

```python
plt.hist(df['Price'], bins=5, color='purple', edgecolor='black')
plt.title('Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```

**Use When:**

* You want to see the spread and shape of data (e.g., normal distribution, skewness).

---

### **D) Single Categorical Variable — Count Plot (Car Type Frequency)**

Show how many items fall into each category.

```python
counts = df['Type'].value_counts()

plt.bar(counts.index, counts.values, color='orange')
plt.title('Count of Car Types')
plt.xlabel('Car Type')
plt.ylabel('Count')
plt.grid(axis='y')
plt.show()
```

**Use When:**

* You want to show how frequently each category appears in your dataset.

---

### **E) Grouped Bar Plot — Average Sales by Country**

When comparing multiple categories side by side.

```python
avg_sales_country = df.groupby('Country')['Sales'].mean()

plt.bar(avg_sales_country.index, avg_sales_country.values, color='green')
plt.title('Average Sales by Country')
plt.xlabel('Country')
plt.ylabel('Average Sales')
plt.grid(axis='y')
plt.show()
```

---

### **F) Box Plot — Sales Distribution by Type**

Box plots are excellent for visualizing distribution and outliers per category.

```python
types = df['Type'].unique()
types.sort()
data_to_plot = [df[df['Type'] == t]['Price'] for t in types]


plt.figure(figsize=(8, 6))
plt.boxplot(data_to_plot, labels=types)
plt.title("Price Distribution by Vehicle Type")
plt.xlabel("Type")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# of with seaborn
import seaborn as sns

sns.boxplot(x='Type', y='Sales', data=df)
plt.title('Sales Distribution by Car Type')
plt.show()
```

**Use When:**

* You want to check spread, median, and outliers by category.

---

### **Summary of Graph Choices and When to Use Them**

| Graph Type   | Best For                      | Typical Variables         |
| ------------ | ----------------------------- | ------------------------- |
| Scatter Plot | Trends/Correlation            | Continuous vs Continuous  |
| Bar Plot     | Compare Categories            | Categorical vs Continuous |
| Histogram    | Distribution Analysis         | Single Continuous         |
| Count Plot   | Category Frequency            | Single Categorical        |
| Box Plot     | Distribution + Outliers       | Categorical vs Continuous |
| Grouped Bar  | Comparing Categories by Group | Categorical grouped       |

---

