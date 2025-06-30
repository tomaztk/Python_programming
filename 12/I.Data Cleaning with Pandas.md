

## **I. Data Cleaning with Pandas**

Data cleaning is a critical step in any data analysis or machine learning workflow. It involves detecting and correcting (or removing) corrupt or inaccurate records, missing values, duplicate data, and outliers in a dataset.

---
 
 ### **Get Sample data**
 
```python
import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Alice'],
    'Age': [25, np.nan, 35, 45, np.nan, 29, 33, 22, 39, 25],
    'Salary': [50000, 60000, 70000, 80000, 90000, 1000000, 65000, np.nan, 72000, 50000],
    'Gender': ['F', 'M', 'M', 'M', 'F', np.nan, 'F', 'M', 'F', 'F'],
    'Email': [
        'alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com',
        'eva@example.com', 'frank@example.com', 'grace@example.com', 'henry@example.com',
        'ivy@example.com', 'alice@example.com'  # duplicate email
    ]
}

df = pd.DataFrame(data)
print(df)
```

and optional, if you want to save it to CSV:

```python
df.to_csv('sample_dirty_data.csv', index=False)
```


###  **Handling Missing Data**

Missing values can significantly affect the quality of insights or model performance. Pandas provides intuitive functions to detect, remove, or impute missing values.

#### ** Detect Missing Values**

```python
df.isnull().sum()
```

This returns the number of missing (NaN) entries for each column.

```python
print(df.isnull().sum())
```

#### ** Drop Missing Values**

Drop rows or columns with missing values:

```python
df.dropna(inplace=True)  # Drops any rows with at least one NaN
```

Optional parameters:

* `axis=1` – drop columns instead of rows.
* `how='all'` – drop only if **all** values are missing.
* `subset=['Col1', 'Col2']` – check specific columns only.

```python
df.dropna(subset=['Age', 'Salary'], how='any', inplace=True)
```

#### ** Fill Missing Values (Imputation)**

Impute missing values with a fixed value or a statistic (mean, median, mode):

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)
```

For categorical data:

```python
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
```

Fill with a custom value:

```python
df['Country'].fillna('Unknown', inplace=True)
```

Forward-fill and back-fill:

```python
df.fillna(method='ffill', inplace=True)  # forward fill
df.fillna(method='bfill', inplace=True)  # backward fill
```

>  **Tip**: Use `SimpleImputer` from `sklearn.impute` for more advanced strategies (like constant, most\_frequent, or strategy-specific per column).

---

###  **Handling Duplicates**

Duplicate entries can skew analysis, especially in count-based operations.

#### **Check for Duplicates**

```python
df.duplicated().sum()
```

Returns the number of duplicate rows (first occurrence is considered unique).

```python
df[df.duplicated()]
```

#### **Drop Duplicates**

```python
df.drop_duplicates(inplace=True)
```

You can also drop duplicates based on specific columns:

```python
df.drop_duplicates(subset=['Name', 'Email'], keep='first', inplace=True)
```

>  `keep='last'` or `keep=False` to control which duplicates are retained.

---

###  **Detecting and Handling Outliers**

Outliers can distort statistical measures and models. Common methods for detecting them include the IQR method and Z-score.

#### **Using IQR (Interquartile Range)**

```python
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

# Find outliers
outliers = df[(df['Salary'] < Q1 - 1.5 * IQR) | (df['Salary'] > Q3 + 1.5 * IQR)]
```

#### **Remove or Cap/Floor Outliers**

Remove:

```python
df = df[(df['Salary'] >= Q1 - 1.5 * IQR) & (df['Salary'] <= Q3 + 1.5 * IQR)]
```

Cap/floor (Winsorizing):

```python
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['Salary'] = df['Salary'].clip(lower=lower_bound, upper=upper_bound)
```

#### **Z-Score Method (Standard Score)**

Use for normally distributed data:

```python
from scipy import stats

z_scores = stats.zscore(df['Salary'])
abs_z_scores = np.abs(z_scores)
df = df[abs_z_scores < 3]  # Keep rows with z-score less than 3
```

>  Tip: Use boxplots to visually identify outliers.

```python
import matplotlib.pyplot as plt

plt.boxplot(df['Salary'])
plt.title('Boxplot of Salary')
plt.show()
```

---

### Summary Table

| Task                  | Function Used                    | Notes                                   |
| --------------------- | -------------------------------- | --------------------------------------- |
| Detect Missing Values | `df.isnull().sum()`              | Per column                              |
| Drop Missing Values   | `df.dropna()`                    | Use `subset` to target specific columns |
| Fill Missing Values   | `df.fillna()`                    | Mean/Median/Mode/Custom                 |
| Detect Duplicates     | `df.duplicated()`                | Use `subset` to focus on columns        |
| Drop Duplicates       | `df.drop_duplicates()`           | Use `keep` to control removal           |
| Detect Outliers (IQR) | `quantile()`                     | Good for skewed data                    |
| Handle Outliers       | `clip()` or filter conditionally | Optionally use Z-score                  |

-
