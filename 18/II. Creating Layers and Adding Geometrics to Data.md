
## **II. Creating Layers and Adding Geometrics to Data**

In Matplotlib, each element you add to a chart — such as points, lines, labels, grids, or shapes — acts like a **layer**. These layers stack together to build the final visual. Understanding how to combine these layers gives you flexibility to create clear, insightful charts.

---

### **Data**

```python
import pandas as pd

data = {
    'Model': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa'],
    'Price': [15000, 18000, 20000, 22000, 25000, 27000, 30000, 32000, 35000, 40000],
    'Sales': [800, 750, 500, 450, 400, 380, 300, 250, 200, 150],
    'Rating': [4.5, 4.2, 4.8, 4.0, 3.9, 3.8, 3.5, 3.4, 3.2, 3.0]
}

df = pd.DataFrame(data)
```

---

### **Basic Line Plot (Price vs Sales)**

A line plot connects data points with straight lines. It is typically used to show trends or relationships between continuous variables.

```python
import matplotlib.pyplot as plt

plt.plot(df['Price'], df['Sales'], label='Sales Trend')
plt.title('Car Price vs Sales')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)  # Adding a grid as a background layer
plt.show()
```

**Explanation:**

* `plt.plot()` adds a **line layer**.
* `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` add **text layers**.
* `plt.legend()` adds a **legend layer** for clarity.
* `plt.grid(True)` adds a **grid layer** beneath the data.

These layers combine to make the chart readable and informative.

---

### **Scatter Plot (Rating vs Sales)**

Scatter plots are used to show the relationship between two numerical variables. Each point is an observation.

```python
plt.scatter(df['Rating'], df['Sales'], color='green', alpha=0.7, label='Data Points')
plt.title('Rating vs Sales')
plt.xlabel('Rating')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
```

**What's Happening Here:**

* `plt.scatter()` adds a **point layer**.
* The `alpha` parameter controls transparency, so overlapping points are visible.
* The legend and grid are layered on top for readability.

---

### **Combining Layers — Scatter with Trend Line**

Often, it's useful to combine a scatter plot with a line of best fit to highlight a trend.

```python
import numpy as np

# Scatter plot
plt.scatter(df['Rating'], df['Sales'], color='blue', alpha=0.6, label='Sales Data')

# Trend line (linear fit)
coefficients = np.polyfit(df['Rating'], df['Sales'], 1)
poly = np.poly1d(coefficients)
plt.plot(df['Rating'], poly(df['Rating']), color='red', linewidth=2, label='Trend Line')

plt.title('Rating vs Sales with Trend Line')
plt.xlabel('Rating')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
```

**Why This Works:**

* The **scatter layer** shows actual data.
* The **trend line layer** highlights the overall relationship.
* Using layers together helps the viewer see both individual points and general trends.

---

### **Highlighting Data — Using Annotations**

Annotations add another layer of meaning to a chart by pointing out key data.

```python
plt.scatter(df['Price'], df['Sales'], color='purple', alpha=0.7)
plt.title('Car Price vs Sales with Annotation')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)

# Annotate a specific point
plt.annotate('Best Seller', xy=(20000, 500), xytext=(22000, 600),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()
```

**Reasoning:**

* `plt.annotate()` adds a **text + arrow layer** that draws attention to important data.
* Use annotations to make insights stand out in presentations or reports.

---

### **Summary of Layering Concepts in Matplotlib**

| Layer Type     | Example Function              | Purpose                       |
| -------------- | ----------------------------- | ----------------------------- |
| Plot Line      | `plt.plot()`                  | Show trends between variables |
| Scatter Points | `plt.scatter()`               | Show individual data points   |
| Title/Labels   | `plt.title()`, `plt.xlabel()` | Add context                   |
| Legend         | `plt.legend()`                | Identify layers               |
| Grid           | `plt.grid(True)`              | Make values easier to read    |
| Annotation     | `plt.annotate()`              | Highlight key insights        |

