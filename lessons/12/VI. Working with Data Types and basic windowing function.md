##  **VI. Working with Data Types and basic windowing function**

Understanding data types is important for choosing proper preprocessing methods.

###  **Categorical Data**

```python
df['Department'] = df['Department'].astype('category')
```

* Saves memory and improves performance.
* Categories can be sorted or reordered with `.cat`.

###  **Continuous Data**

These are typically **numerical values** that can take many values within a range.

```python
df['Salary'].describe()
```

* Normalize or standardize:

```python
df['Salary_z'] = (df['Salary'] - df['Salary'].mean()) / df['Salary'].std()
```

###  **Binary Data**

```python
df['IsRemote'].unique()  # e.g., ['Yes', 'No'] or [1, 0]

df['IsRemote'] = df['IsRemote'].map({'Yes': 1, 'No': 0})
```

* Binary columns can be used for classification and filtering.

---

##  **Basic Windowing Functions**

Window functions compute statistics over a sliding or cumulative window.

###  **Rolling Windows**

```python
df['RollingAvg'] = df['Salary'].rolling(window=3).mean()
```

* Good for smoothing out time series trends.
* Use `.std()`, `.sum()`, etc., as well.

###  **Expanding Window**

```python
df['CumulativeSum'] = df['Salary'].expanding().sum()
```

* Keeps growing the window to include all previous rows.

###  **Cumulative Functions**

```python
df['SalaryCumSum'] = df['Salary'].cumsum()
df['SalaryCumMax'] = df['Salary'].cummax()
```

* Ideal for running totals, maximums, or minimums over time.

###  **Ranking and Percentiles**

```python
df['Rank'] = df['Salary'].rank()
df['Percentile'] = df['Salary'].rank(pct=True)
```