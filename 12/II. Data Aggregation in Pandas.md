## **II. Data Aggregation in Pandas**

Data aggregation helps condense large datasets into meaningful summaries by computing metrics like totals, averages, counts, medians, etc. It's especially useful in reporting, dashboards, and group-based analysis.

Data:

```python
import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['alice johnson', 'Bob Smith', 'CHARLIE Brown', 'david lee', 'Eve Stone', 'Frank King', 'Grace Li'],
    'Email': [
        'alice@example.com', 'bob@example.org', 'charlie@example.net',
        'david@workplace.com', 'eve@example.com', 'frank@company.org', 'grace@office.net'
    ],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'HR', 'Sales', 'IT'],
    'Location': ['NY', 'NY', 'SF', 'NY', 'SF', 'SF', 'NY'],
    'HireDate': pd.to_datetime(['2020-01-15', '2019-07-10', '2021-03-20', '2022-11-05', '2018-06-25', '2023-09-12', '2020-05-01']),
    'Salary': [52000, 75000, 82000, 58000, 50000, 60000, 79000],
    'ExperienceYears': [2, 5, 6, 3, 7, 1, 4],
    'IsRemote': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)
```

---

###  **Using `groupby()`**

The `groupby()` function splits the data into groups based on one or more columns, applies a function (like `mean()` or `sum()`), and combines the result.

#### **Basic Aggregation**

```python
df.groupby('Department')['Salary'].mean()
```

This shows the average salary per department.

#### **Multiple Aggregations for Multiple Groups**

```python
df.groupby(['Department', 'Location'])['Salary'].agg(['mean', 'count'])
```

* `mean`: average salary
* `count`: number of employees per group

#### **Custom Named Aggregations**

```python
df.groupby('Department').agg(
    Avg_Salary=('Salary', 'mean'),
    Max_Salary=('Salary', 'max'),
    Employee_Count=('EmployeeID', 'count')
)
```

> This syntax (introduced in Pandas 0.25+) allows renaming results directly.

---

### **Using `agg()` for Custom Aggregations**

`agg()` lets you apply multiple functions to one or more columns, especially with groupby.

```python
df.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min'],
    'ExperienceYears': ['median', 'std']
})
```

> The result is a multi-level column index. Use `.reset_index()` and rename columns if needed.

#### **Flattening MultiIndex Columns**

```python
agg_df = df.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'ExperienceYears': ['median']
})

# Flatten column names
agg_df.columns = ['_'.join(col) for col in agg_df.columns]
agg_df.reset_index(inplace=True)
```

---

### **Using `pivot_table()`**

`pivot_table()` is similar to Excel's pivot tables and great for cross-tabulated summaries.

```python
df.pivot_table(values='Salary', index='Department', columns='Location', aggfunc='mean')
```

This creates a matrix where:

* Rows = Departments
* Columns = Locations
* Values = Average Salary

#### **Count of Employees per Department/Location**

```python
df.pivot_table(index='Department', columns='Location', values='EmployeeID', aggfunc='count', fill_value=0)
```

> `fill_value` replaces `NaN` with 0 for better readability.

#### **Multiple Aggregations in Pivot Table**

```python
df.pivot_table(index='Department', values=['Salary', 'ExperienceYears'], aggfunc={'Salary': 'mean', 'ExperienceYears': 'median'})
```

---

### **Merging and Joining DataFrames**

Combining multiple datasets is essential when data is spread across sources or tables.

#### **Some sample data**

```python
import pandas as pd

# Employee information
df1 = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Sales', 'HR']
})

# Performance records
df2 = pd.DataFrame({
    'EmployeeID': [102, 103, 104, 105],
    'PerformanceScore': [88, 92, 79, 85],
    'ReviewDate': ['2024-06-01', '2024-06-01', '2024-06-01', '2024-06-01']
})
```

#### **Basic Merge Example**

```python
combined_df = pd.merge(df1, df2, on='EmployeeID', how='inner')
```

#### **Different Merge Types**

| Type    | Description                       |
| ------- | --------------------------------- |
| `inner` | Only matching records in both     |
| `left`  | All from left, match from right   |
| `right` | All from right, match from left   |
| `outer` | All records, match where possible |

#### **Merge on Multiple Keys**

```python
pd.merge(df1, df2, on=['EmployeeID', 'Date'], how='left')
```

#### **Add Suffixes for Overlapping Columns**

```python
pd.merge(df1, df2, on='EmployeeID', suffixes=('_Emp', '_Perf'))
```

---

### **Demo Dataset for Practice**

Assume the following simplified HR data:

```python
df = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4, 5, 6],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'HR', 'Sales'],
    'Location': ['NY', 'NY', 'SF', 'NY', 'SF', 'SF'],
    'Salary': [50000, 75000, 80000, 55000, 52000, 58000],
    'ExperienceYears': [2, 5, 7, 3, 2, 4]
})
```

**Performance data:**

```python
performance = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 5, 6],
    'PerformanceRating': [3, 4, 5, 2, 4]
})
```

#### **Merge + Group + Aggregate**

```python
merged = pd.merge(df, performance, on='EmployeeID', how='left')

summary = merged.groupby('Department').agg({
    'Salary': 'mean',
    'PerformanceRating': 'mean',
    'EmployeeID': 'count'
}).rename(columns={'Salary': 'AvgSalary', 'PerformanceRating': 'AvgRating', 'EmployeeID': 'Count'})
```

---

###  Summary Table

| Task                         | Code Sample                                            |
| ---------------------------- | ------------------------------------------------------ |
| Group by one column          | `df.groupby('Col')['Target'].mean()`                   |
| Group by multiple columns    | `df.groupby(['Col1', 'Col2'])['Target'].agg(['mean'])` |
| Custom multiple aggregations | `df.groupby('Col').agg({'A': 'mean', 'B': 'sum'})`     |
| Pivot table summary          | `df.pivot_table(values='X', index='Y', columns='Z')`   |
| Merge datasets               | `pd.merge(df1, df2, on='Key', how='left')`             |

