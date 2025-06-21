###  **I. Introduction to Pandas**

####  What Are Packages in Python?

In Python, **packages** are collections of modules that provide additional functionality. Instead of writing everything from scratch, we can use packages that others have written and shared.

* Think of packages as **toolboxes** — they contain useful tools (functions, classes, methods) for specific types of tasks.
* For data manipulation and analysis, two of the most commonly used packages are **Pandas** and **NumPy**.

#####  Installing Packages

To use a package, you may need to install it first using `pip` (Python’s package installer):

```bash
pip install pandas
pip install numpy
```

In Jupyter notebooks or IPython, use:

```python
!pip install pandas
!pip install numpy
```

#####  Importing Packages

Once installed, import them at the beginning of your script or notebook:

```python
import pandas as pd
import numpy as np
```

>  `pd` and `np` are **aliases** commonly used by the Python community for convenience.

---

####  What is Pandas and Why It's Useful?

**Pandas** is a powerful, open-source Python package used for data manipulation and analysis. It provides flexible data structures that make it easy to clean, transform, explore, and visualize datasets — particularly **tabular data** (like spreadsheets or SQL tables).

##### Why Use Pandas?

* Allows you to **load data** from CSV, Excel, SQL, etc.
* Helps perform **filtering, sorting, grouping, and aggregating** operations easily
* Designed for **fast and intuitive** data exploration
* Seamlessly integrates with **NumPy, Matplotlib**, and other libraries

---

####  Key Data Structures in Pandas

Pandas is built on two main data structures:

---

##### A-> Series: One-dimensional labeled array

* Like a single column of data with labels (index)
* Stores any data type: numbers, strings, booleans, etc.

**Example:**

```python
import pandas as pd

data = [10, 20, 30, 40]
labels = ['a', 'b', 'c', 'd']

s = pd.Series(data, index=labels)
print(s)
```

**Output:**

```
a    10
b    20
c    30
d    40
dtype: int64
```

---

##### B-> DataFrame: Two-dimensional labeled data structure

* Think of it as an **Excel table** or a **SQL table**: rows and columns, with labels
* Each column is a Series
* Most common structure used in Pandas

**Example:**

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
     Name  Age    City
0   Alice   25     NYC
1     Bob   30      LA
2  Charlie   35  Chicago
```

---

####  How is Pandas Different from NumPy?

While **NumPy** is great for numerical arrays and mathematical operations, it is not designed for **labeled** or **heterogeneous** (mixed-type) data.

| Feature             | NumPy (ndarray)    | Pandas (DataFrame/Series)              |
| ------------------- | ------------------ | -------------------------------------- |
| Best For            | Numerical data     | Labeled, structured/tabular data       |
| Supports Labels     | ❌                  | ✅ Row and column labels                |
| Mixed Data Types    | ❌ (same type only) | ✅ Different types in each column       |
| Readability         | Moderate           | High (like spreadsheets)               |
| Data Source Loading | Limited            | ✅ Easy load from CSV, Excel, SQL, etc. |

---

> **Use Pandas when you want to:**
>
> * Handle real-world datasets
> * Work with structured (table-like) data
> * Do analysis or cleaning before feeding data into a model




### I.a Introduction to Polars (an alternative to Pandas) **

Introduction to **Polars** – A Fast Modern Alternative to Pandas

#### What is Polars?

**Polars** is a newer Python library designed for fast, efficient, and parallelized data manipulation. It’s written in **Rust**, which makes it **significantly faster** than Pandas in many cases, especially when handling large datasets.

##### Why Use Polars?

* **Performance:** Built for speed with multi-threaded execution
* **Lazy Evaluation:** Like SQL or Spark, operations are planned and optimized before execution
* **Memory-efficient:** Uses Arrow-based columnar storage
* **Familiar Syntax:** Inspired by Pandas, but with its own approach

---

####  Installing and Importing Polars

```bash
pip install polars
```

```python
import polars as pl
```

---

#### Polars vs. Pandas

| Feature       | Pandas                      | Polars                       |
| ------------- | --------------------------- | ---------------------------- |
| Language Core | Python                      | Rust                         |
| Speed         | Moderate                    | 🚀 Very Fast (multithreaded) |
| Evaluation    | Eager (immediate execution) | Lazy (deferred until needed) |
| API Design    | Broad and flexible          | Minimal and efficient        |
| Memory Usage  | Higher                      | Lower                        |
| Syntax Style  | Pythonic (object-based)     | Functional (method chaining) |

---

####  Example: Creating a DataFrame in Polars

```python
import polars as pl

df = pl.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
})

print(df)
```

**Output:**

```
shape: (3, 3)
┌─────────┬─────┬──────────┐
│ Name    │ Age │ City     │
│ ---     │ --- │ ---      │
│ str     │ i64 │ str      │
├─────────┼─────┼──────────┤
│ Alice   │  25 │ NYC      │
│ Bob     │  30 │ LA       │
│ Charlie │  35 │ Chicago  │
└─────────┴─────┴──────────┘
```

---

#### Selecting and Filtering in Polars

```python
# Select a single column
df.select("Name")

# Filter rows
df.filter(pl.col("Age") > 28)
```

---

####  When to Use Polars

* Working with **very large datasets** where performance is a bottleneck
* When you need **parallel processing** or **lazy evaluation**
* For production environments where **speed and memory efficiency** matter

>  Note: Polars is newer, so while it's powerful, its ecosystem isn't as mature as Pandas yet. It’s ideal for power users or developers who are performance-focused.




###  Pandas vs. Polars: Side-by-Side Cheat Sheet

| **Task**                        | **Pandas**                       | **Polars**                                          |
| ------------------------------- | -------------------------------- | --------------------------------------------------- |
| **Import package**              | `import pandas as pd`            | `import polars as pl`                               |
| **Create DataFrame**            | `pd.DataFrame({...})`            | `pl.DataFrame({...})`                               |
| **Read CSV**                    | `pd.read_csv('file.csv')`        | `pl.read_csv('file.csv')`                           |
| **View top rows**               | `df.head()`                      | `df.head()`                                         |
| **Select column**               | `df['col']` or `df.col`          | `df.select("col")`                                  |
| **Select multiple columns**     | `df[['col1', 'col2']]`           | `df.select(["col1", "col2"])`                       |
| **Filter rows**                 | `df[df['Age'] > 30]`             | `df.filter(pl.col("Age") > 30)`                     |
| **Add new column**              | `df['new'] = df['Age'] + 5`      | `df.with_columns((pl.col("Age") + 5).alias("new"))` |
| **Drop column**                 | `df.drop(columns=['col'])`       | `df.drop("col")`                                    |
| **Group by + aggregation**      | `df.groupby('City').mean()`      | `df.groupby("City").agg(pl.col("Age").mean())`      |
| **Describe data**               | `df.describe()`                  | `df.describe()` *(limited in Polars)*               |
| **Sort values**                 | `df.sort_values('Age')`          | `df.sort("Age")`                                    |
| **Shape of DataFrame**          | `df.shape`                       | `df.shape`                                          |
| **Convert to NumPy**            | `df.to_numpy()`                  | `df.to_numpy()` *(as NumPy-compatible)*             |
| **Lazy execution support**      | ❌ *(Not supported)*              | ✅ `pl.scan_csv()` for lazy pipelines                |
| **Multithreading**              | ❌ *(Single-threaded by default)* | ✅ *(Multithreaded by design)*                       |
| **Performance with large data** | Slower                           | Much faster                                         |

---

###  Summary

| **Aspect**         | **Pandas**                    | **Polars**                          |
| ------------------ | ----------------------------- | ----------------------------------- |
| Language Base      | Python                        | Rust (Python API)                   |
| Evaluation Model   | Eager                         | Lazy (optional)                     |
| Speed/Performance  | Good                          | Excellent for large data            |
| API Style          | Pythonic, imperative          | Functional, method-chaining         |
| Learning Curve     | Easier for beginners          | Slightly steeper                    |
| Ecosystem Maturity | Very mature                   | Rapidly growing                     |
| Best Use Case      | General-purpose data analysis | Large-scale, high-performance tasks |

---

**Tip for Learners**:
If you're just starting out and learning the basics of data analysis, **Pandas** is the best starting point due to its simplicity and community support. As you progress and work with larger datasets or seek higher performance, learning **Polars** will be a powerful asset.



