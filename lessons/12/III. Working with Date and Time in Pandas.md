## **III. Working with Date and Time in Pandas**

Handling datetime data is essential for time series analysis, scheduling, and trends over time.


Dataset:

```python
import pandas as pd

# Sample Employee Data
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

### **Converting to Datetime**

```python
df['HireDate'] = pd.to_datetime(df['HireDate'])
```

* Ensures consistent format for time-based operations.
* Converts string or object columns to proper datetime types.

###  **Extracting Date Components**

```python
df['Year'] = df['HireDate'].dt.year
df['Month'] = df['HireDate'].dt.month
df['Weekday'] = df['HireDate'].dt.day_name()
```

* Useful for grouping and filtering by month, year, day of week, etc.

###  **Filtering by Date**

```python
df[df['HireDate'] >= '2023-01-01']
```

* Enables selecting rows from a specific time window.

###  **Creating Date Ranges**

```python
pd.date_range(start='2024-01-01', periods=5, freq='D')
```

* Generate a sequence of dates for simulation or filling data.

>  Use `.dt` accessor to pull time parts (like `.hour`, `.dayofyear`, etc.).


