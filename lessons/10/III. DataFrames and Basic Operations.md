##  **III. DataFrames and Basic Operations**

Once your data is loaded into a **Pandas DataFrame**, the next step is to explore, understand, and manipulate it. This section walks through the **most common operations** you'll use in real-world data analysis.

---

###  1. **Exploring a DataFrame**

Understanding the structure of your data is the first step in working with it effectively.

####  `df.head(n)`

Displays the **first n rows** of the DataFrame (default is 5).

```python
df.head()
df.head(10)  # First 10 rows
```

####  `df.info()`

Gives a **summary of the DataFrame**, including:

* Number of rows and columns
* Column data types
* Memory usage
* Count of non-null values

```python
df.info()
```

####  `df.describe()`

Provides **statistical summary** for numeric columns:

* Count, mean, std, min, max, and quartiles

```python
df.describe()
```

---

###  Example:

```python
import pandas as pd

df = pd.read_csv("students_scores.csv")
print(df.head())
print(df.info())
print(df.describe())
```

##### Sample `students_scores.csv`:

```
Name,Math,Science,English
Alice,85,90,78
Bob,72,80,69
Charlie,88,85,95
David,91,87,89
Eva,76,90,84
```

---

###  2. **Selecting Data**

Pandas makes it easy to select specific rows or columns using different indexing methods.

---

#### Select Columns

* **Single column**:

```python
df['Math']
```

* **Multiple columns**:

```python
df[['Math', 'English']]
```

---

####  Select Rows

* **By label (index) using `.loc[]`**:

```python
df.loc[0]          # First row
df.loc[0:2]        # Rows with labels 0 to 2 inclusive
df.loc[:, 'Math']  # All rows, only 'Math' column
```

* **By position using `.iloc[]`**:

```python
df.iloc[0]          # First row
df.iloc[0:3]        # First three rows
df.iloc[:, 1]       # All rows, second column
```

---

###  3. **Sorting Data**

Sorting helps to quickly analyze trends or rank values.

####  Sort by a single column:

```python
df.sort_values(by='Math')
```

####  Sort in descending order:

```python
df.sort_values(by='English', ascending=False)
```

---

###  4. **Filtering with Conditions (Boolean Indexing)**

Use **logical expressions** to filter rows.

```python
df[df['Math'] > 80]
```

Combine multiple conditions:

```python
df[(df['Math'] > 80) & (df['Science'] > 85)]
```

---

###  5. **Adding and Removing Columns**

####  Add a new column:

```python
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
```

####  Remove a column:

```python
df.drop('English', axis=1, inplace=True)  # inplace modifies the DataFrame
```

---

###  Demo: Combined Operations

```python
import pandas as pd

# Load dataset
df = pd.read_csv("students_scores.csv")

# Explore data
print(df.head())
print(df.info())
print(df.describe())

# Select data
print(df[['Name', 'Math']])
print(df.iloc[0:2])

# Sort data
sorted_df = df.sort_values(by='Science', ascending=False)
print(sorted_df)

# Filter data
high_scorers = df[df['Math'] > 80]
print(high_scorers)

# Add average score column
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Drop a column
df = df.drop('English', axis=1)

print(df)
```

---

### Sample Dataset (CSV): `students_scores.csv`

```
Name,Math,Science,English
Alice,85,90,78
Bob,72,80,69
Charlie,88,85,95
David,91,87,89
Eva,76,90,84
```

---

###  Summary Table: Common DataFrame Operations

| **Operation**           | **Syntax**                 |
| ----------------------- | -------------------------- |
| View first rows         | `df.head()`                |
| View structure/info     | `df.info()`                |
| View statistics         | `df.describe()`            |
| Select one column       | `df['Column']`             |
| Select multiple columns | `df[['Col1', 'Col2']]`     |
| Select by label         | `df.loc[0:2]`              |
| Select by index         | `df.iloc[0:2]`             |
| Sort by column          | `df.sort_values(by='Col')` |
| Filter by condition     | `df[df['Col'] > value]`    |
| Add column              | `df['New'] = ...`          |
| Remove column           | `df.drop('Col', axis=1)`   |


