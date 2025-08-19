
# Introduction to Matplotlib in Python

##  What is Matplotlib?


[Matplotlib](https://matplotlib.org/) is one of the most popular Python libraries for creating **static**, **animated**, and **interactive** visualizations. It's highly customizable and works well with other Python libraries like NumPy, pandas, and SciPy.

---

##  Installation

If not already installed, you can install Matplotlib via pip:

```bash
pip install matplotlib
```

---

##  Importing Matplotlib

We typically import the `pyplot` submodule for most plotting functions.

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

---


##  Sample Dataset


Let’s create a simple dataset to use across demos:


```python
# Create sample dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [305, 356, 410, 489, 512, 590],
    'Expenses': [220, 260, 300, 320, 340, 390]
}

df = pd.DataFrame(data)
df['Price'] = df['Sales'] - df['Expenses']
```

---

##  Basic Plot Types


### 1. **Line Plot**



```python
plt.plot(df['Month'], df['Sales'], label='Sales')
plt.plot(df['Month'], df['Expenses'], label='Expenses')
plt.title('Monthly Sales vs Expenses')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)
plt.show()
```

---


### 2. **Bar Chart**


```python
plt.bar(df['Month'], df['Sales'], color='skyblue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.show()
```

---

### 3. **Stacked Bar Chart**


```python
plt.bar(df['Month'], df['Sales'], label='Sales')
plt.bar(df['Month'], df['Expenses'], bottom=df['Sales'], label='Expenses')
plt.title('Stacked Sales & Expenses')
plt.legend()
plt.show()
```


---


### 4. **Scatter Plot**

 

```python
plt.scatter(df['Sales'], df['Expenses'], color='red')
plt.title('Sales vs Expenses')
plt.xlabel('Sales')
plt.ylabel('Expenses')
plt.grid(True)
plt.show()
```

---


### 5. **Pie Chart**


```python
plt.pie(df['Sales'], labels=df['Month'], autopct='%1.1f%%')
plt.title('Sales Distribution by Month')
plt.show()

```

---

 

##  Customization Options

 
### Titles, Labels, Legends, and Grids


```python
plt.plot(df['Month'], df['Sales'], color='green', linestyle='--', marker='o')
plt.title('Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(['Sales'])
plt.grid(True, linestyle=':', linewidth=0.5)
plt.show()
```

---


##  Subplots


```python
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].bar(df['Month'], df['Sales'], color='blue')
axs[0].set_title('Sales')
axs[1].bar(df['Month'], df['Expenses'], color='orange')
axs[1].set_title('Expenses')
plt.tight_layout()
plt.show()

```

 

---


##  Styling with `plt.style`


```python
plt.style.use('ggplot')
plt.plot(df['Month'], df['Sales'])
plt.title('Styled Plot')
plt.show()

```

---


##  Advanced Features

### Plotting with NumPy


```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
```

---

### Annotating Points

```python
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales with Annotations')
 
for i, txt in enumerate(df['Sales']):
    plt.annotate(txt, (df['Month'][i], df['Sales'][i]), textcoords="offset points", xytext=(0,5), ha='center')
plt.show()
```

---

### Histogram


```python
np.random.seed(42)
data = np.random.randn(1000)

 
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram of Random Data')
plt.show()
```

---


##  Saving Plots

```python
plt.plot(df['Month'], df['Sales'])
plt.title('Sales')
plt.savefig('sales_plot.png', dpi=300)
plt.show()
```

---

##  Interactive Plots (Optional with `%matplotlib notebook` or `matplotlib.widgets`)

```python
# In a Jupyter Notebook:
%matplotlib notebook

plt.plot(df['Month'], df['Sales'])
plt.title("Interactive Plot")
plt.show()
```

---


##  Resetting the Plot



```python
plt.clf()       # Clears the current figure
plt.cla()       # Clears the current axes
plt.close()     # Closes the figure window
```


---

##  Summary of Key Components


| Feature      | Function                               |
| ------------ | -------------------------------------- |
| Basic Plot   | `plt.plot()`                           |
| Labels       | `plt.xlabel()`, `plt.ylabel()`         |
| Title        | `plt.title()`                          |
| Legend       | `plt.legend()`                         |
| Grid         | `plt.grid()`                           |
| Subplots     | `plt.subplots()`                       |
| Save Plot    | `plt.savefig()`                        |
| Pie/Bar/Hist | `plt.pie()`, `plt.bar()`, `plt.hist()` |