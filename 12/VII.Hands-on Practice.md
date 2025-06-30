##  **VII. Hands-on Practice with `employee_performance.csv`**

---

####  Practice Tasks

1. Load dataset and check for missing values
2. Fill missing `YearsExperience` with mean
3. Remove any duplicated rows
4. Identify outliers in `PerformanceScore`
5. Group by `Department` to calculate average salary and experience
6. Create a pivot table showing average salary per department/location
7. Merge with another mini dataset (e.g., project assignments)

---

###  **Step 1: Load dataset and check for missing values**

```python
import pandas as pd

# Load the dataset
df = pd.read_csv("employee_performance.csv")

# Display basic info
print(df.info())

# Check for missing values
print(df.isnull().sum())
```

---

###  **Step 2: Fill missing `YearsExperience` with mean**

```python
mean_experience = df['YearsExperience'].mean()
df['YearsExperience'].fillna(mean_experience, inplace=True)

print("Missing values after imputation:\n", df.isnull().sum())
```
---

### **Step 3: Remove duplicated rows**

```python
# Check for duplicates
print("Duplicates found:", df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Confirm
print("Remaining duplicates:", df.duplicated().sum())
```

---

### **Step 4: Identify outliers in `PerformanceScore` using IQR**

```python
Q1 = df['PerformanceScore'].quantile(0.25)
Q3 = df['PerformanceScore'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['PerformanceScore'] < Q1 - 1.5 * IQR) | (df['PerformanceScore'] > Q3 + 1.5 * IQR)]

print("Outliers detected:\n", outliers)
```

> Optionally remove or clip outliers:

```python
df['PerformanceScore'] = df['PerformanceScore'].clip(lower=Q1 - 1.5 * IQR, upper=Q3 + 1.5 * IQR)
```

---

###  **Step 5: Group by `Department` to calculate average salary and experience**

```python
department_summary = df.groupby('Department').agg({
    'Salary': 'mean',
    'YearsExperience': 'mean'
}).rename(columns={
    'Salary': 'AvgSalary',
    'YearsExperience': 'AvgExperience'
})

print(department_summary)
```

---

###  **Step 6: Create a pivot table of average salary per department/location**

```python
pivot_salary = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='Location',
    aggfunc='mean',
    fill_value=0
)

print(pivot_salary)
```

---

###  **Step 7: Merge with another dataset: `project_assignments.csv`**

```python
# Example second dataset
projects = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Project': ['Apollo', 'Zeus', 'Hermes', 'Athena', 'Poseidon']
})

# Merge datasets
df_merged = pd.merge(df, projects, on='EmployeeID', how='left')

print(df_merged[['EmployeeID', 'Name', 'Project']])
```

---

###  Optional Final Step: Save the Cleaned Data

```python
df_merged.to_csv("cleaned_employee_performance.csv", index=False)
```


