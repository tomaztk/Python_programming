
##  **V. Homework Assignment: Exploring a CSV Dataset with Pandas**

###  Task

Load a dataset using **Pandas** and perform **basic data exploration and cleaning**.

---

###  Dataset: `employee_data.csv`

This dataset contains fictional employee records. Here's a preview:

```
ID,Name,Department,Gender,Age,Salary,Experience,Location
101,Alice,HR,Female,29,52000,4,New York
102,Bob,Finance,Male,34,61000,7,Chicago
103,Charlie,IT,Male,41,72000,10,San Francisco
104,Daisy,Finance,Female,28,59000,,Boston
105,Edward,IT,Male,36,73000,9,Chicago
106,Fiona,HR,Female,26,51000,3,New York
107,George,Marketing,Male,30,56000,5,Los Angeles
108,Helen,Finance,Female,38,64000,8,Chicago
109,Ian,Marketing,Male,45,58000,12,Los Angeles
110,Jane,IT,Female,32,70000,6,San Francisco
```

> Save this content to a file named `employee_data.csv`.

---

###  Homework Steps

1. Load the dataset using `pd.read_csv()`
2. Display the first 5 rows with `.head()`
3. Show structure using `.info()` and statistics with `.describe()`
4. Select and print specific columns: `'Name'`, `'Department'`, `'Salary'`
5. Filter employees with **salary > 60,000** and **experience ≥ 5 years**
6. Fill missing values in the `Experience` column with `0`
7. Save the cleaned DataFrame to a new file: `employee_data_cleaned.csv`

---
---
---
---
---
---

##  Solution Code (with steps)

```python
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("employee_data.csv")

# 2. Display the first few rows
print("First 5 rows:")
print(df.head())

# 3. Show structure and summary statistics
print("\nDataFrame Info:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

# 4. Select specific columns
print("\nSelected Columns:")
print(df[['Name', 'Department', 'Salary']])

# 5. Filter based on conditions
filtered_df = df[(df['Salary'] > 60000) & (df['Experience'] >= 5)]
print("\nFiltered Employees (Salary > 60000 and Experience >= 5):")
print(filtered_df)

# 6. Fill missing values
df['Experience'] = df['Experience'].fillna(0)

# 7. Save cleaned dataset
df.to_csv("employee_data_cleaned.csv", index=False)
print("\nCleaned dataset saved to 'employee_data_cleaned.csv'")
```

---