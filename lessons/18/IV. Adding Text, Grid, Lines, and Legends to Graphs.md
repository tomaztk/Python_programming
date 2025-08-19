

## **IV. Adding Text, Grid, Lines, and Legends to Graphs**

Enhancing your plots with extra elements improves their clarity and visual appeal.
Let's go through them one by one:

---

### **A) Adding Titles and Axis Labels**

These provide context and help the viewer understand what the chart shows.

```python
plt.scatter(df['Price'], df['Sales'], color='green')
plt.title('Car Price vs Sales')  # Title at the top
plt.xlabel('Price (USD)')        # X-axis label
plt.ylabel('Sales (Units)')      # Y-axis label
plt.show()
```

---

### **B) Adding Gridlines**

Grids make reading values easier, especially on scatter plots and bar charts.

```python
plt.scatter(df['Price'], df['Sales'], color='blue')
plt.title('Car Price vs Sales with Grid')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)  # Add default gridlines
plt.show()
```

**Customize Gridlines:**

```python
plt.scatter(df['Price'], df['Sales'], color='blue')
plt.title('Car Price vs Sales with Custom Grid')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Light dashed grid
plt.show()
```

---

### **C) Adding Reference Lines (axhline, axvline)**

Use these to show thresholds, averages, or targets.

```python
plt.scatter(df['Price'], df['Sales'], color='purple')
plt.title('Car Price vs Sales with Reference Line')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)

# Add horizontal line for average sales
avg_sales = df['Sales'].mean()
plt.axhline(y=avg_sales, color='red', linestyle='--', label=f'Average Sales ({avg_sales:.0f})')

plt.legend()
plt.show()
```

**Vertical Line Example (e.g., Median Price):**

```python
plt.scatter(df['Price'], df['Sales'], color='orange')
plt.title('Car Price vs Sales with Median Price Line')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)

median_price = df['Price'].median()
plt.axvline(x=median_price, color='green', linestyle='-.', label=f'Median Price (${median_price:.0f})')

plt.legend()
plt.show()
```

---

### **D) Adding Text Labels on Points**

Annotate each data point for identification.

```python
plt.scatter(df['Price'], df['Sales'], color='navy')
plt.title('Car Price vs Sales with Model Labels')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)

for i in range(len(df)):
    plt.text(df['Price'][i]+200, df['Sales'][i]+5, df['Model'][i], fontsize=9)

plt.show()
```

---

### **E) Adding Annotations with Arrows**

Use `plt.annotate()` to highlight special points with arrows.

```python
plt.scatter(df['Price'], df['Sales'], color='teal')
plt.title('Car Price vs Sales with Highlighted Best Seller')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)

# Annotate "Gamma" model
best_seller = df[df['Model'] == 'Gamma']
plt.annotate('Best Seller',
             xy=(best_seller['Price'].values[0], best_seller['Sales'].values[0]),
             xytext=(best_seller['Price'].values[0]+5000, best_seller['Sales'].values[0]+100),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()
```

---

### **F) Adding Legends**

Legends explain colors, lines, or markers used in the chart.

```python
plt.scatter(df['Price'], df['Sales'], color='blue', label='Sales Data')
plt.axhline(y=avg_sales, color='red', linestyle='--', label='Average Sales')
plt.title('Car Price vs Sales with Legend')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()  # Show the legend box
plt.show()
```

---

### **G) Combining Multiple Elements in One Plot**

```python
plt.scatter(df['Price'], df['Sales'], color='darkgreen', label='Sales Data')
plt.axhline(y=avg_sales, color='red', linestyle='--', label='Average Sales')
plt.axvline(x=median_price, color='orange', linestyle='-.', label='Median Price')

for i in range(len(df)):
    plt.text(df['Price'][i]+200, df['Sales'][i]+5, df['Model'][i], fontsize=8)

plt.title('Car Price vs Sales — Fully Annotated')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
```

---

### **Summary of Elements You Can Add:**

| Element        | Function                         | Command                          |
| -------------- | -------------------------------- | -------------------------------- |
| Title          | Adds chart title                 | `plt.title()`                    |
| Axis Labels    | Names X and Y axes               | `plt.xlabel()`, `plt.ylabel()`   |
| Grid           | Background lines for readability | `plt.grid()`                     |
| Reference Line | Shows thresholds or averages     | `plt.axhline()`, `plt.axvline()` |
| Text Labels    | Adds text to specific points     | `plt.text()`                     |
| Annotations    | Highlights with arrows           | `plt.annotate()`                 |
| Legend         | Explains data elements           | `plt.legend()`                   |

---

