[**Use employee\_performance.csv**](employee_performance.csv)

---

## LESSON 11: SOLUTIONS
 
---

### Part-A. Data Exploration & Cleansing

#### **1. Load and Inspect the Dataset**

```python
import pandas as pd
df = pd.read_csv("employee_performance.csv")
print(df.head())
```

#### **2. Dataset Overview**

```python
print(df.info())
print(df.describe())
print(df.shape)
```

#### **3. Fill Missing Values (if any)**

```python
df['YearsExperience'].fillna(df['YearsExperience'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
```

#### **4. Rename Columns**

```python
df.rename(columns={'YearsExperience': 'ExperienceYears', 'Salary': 'AnnualSalary'}, inplace=True)
```

---

### Part-B. Selection, Filtering, Sorting

#### **5. Filter High Performers**

```python
print(df[df['PerformanceScore'] > 85][['Name', 'Department']])
```

#### **6. Sort by Experience and Performance**

```python
print(df.sort_values(by=['ExperienceYears', 'PerformanceScore'], ascending=False))
```

#### **7. Performance Tier Classification**

```python
def tier(score):
    if score >= 85:
        return 'High'
    elif score >= 70:
        return 'Medium'
    else:
        return 'Low'

df['PerformanceTier'] = df['PerformanceScore'].apply(tier)
```

---

### Part-C. Grouping and Aggregation

#### **8. Department Performance Summary**

```python
print(df.groupby('Department')[['AnnualSalary', 'PerformanceScore']].mean())
```

#### **9. Bonus Eligibility Rate by Department**

```python
print(df[df['BonusEligible'] == 'Yes'].groupby('Department')['BonusEligible'].count() / df.groupby('Department')['BonusEligible'].count())
```

---

### Part-D. NumPy Integrations

#### **10. Salary Z-Scores**

```python
from scipy.stats import zscore
df['SalaryZScore'] = zscore(df['AnnualSalary'])
```

#### **11. Normalize Performance Scores**

```python
df['PerfNorm'] = (df['PerformanceScore'] - df['PerformanceScore'].min()) / (df['PerformanceScore'].max() - df['PerformanceScore'].min())
```

---

### Part-E. Functions & Loops

#### **12. Promotion Eligibility Function**

```python
def is_promotable(score, exp):
    return "Yes" if score > 85 and exp > 5 else "No"

df['Promotable'] = df.apply(lambda row: is_promotable(row['PerformanceScore'], row['ExperienceYears']), axis=1)
```

#### **13. Loop Through for Bonus Reports**

```python
for _, row in df.iterrows():
    status = "eligible" if row['BonusEligible'] == "Yes" else "not eligible"
    print(f"{row['Name']} ({row['Department']}) is {status} for a bonus.")
```

---

### Part-F. Advanced Filtering

#### **14. IT Employees in SF with Salary > 70K**

```python
print(df[(df['Department'] == 'IT') & (df['Location'] == 'San Francisco') & (df['AnnualSalary'] > 70000)])
```

#### **15. Retirement Risk Flag**

```python
df['RetirementRisk'] = df['Age'].apply(lambda age: 'Yes' if age > 40 else 'No')
```

---


>  Polars is not supported in this current environment, but the code below can be run **locally** after installing Polars using:

```bash
pip install polars
```

---

## **Part-G. Polars Solutions (Assignments 16–20)**

---

### **16. Load Dataset with Polars**


```python
import polars as pl

pl_df = pl.read_csv("employee_performance.csv")
print(pl_df.head())
```

---

### **17. Filter High Performers in Polars**


```python
high_perf = pl_df.filter(pl.col("PerformanceScore") > 85)
print(high_perf)
```

---

### **18. Group and Aggregate in Polars**


```python
grouped = pl_df.groupby("Department").agg([
    pl.col("Salary").mean().alias("AvgSalary"),
    pl.col("PerformanceScore").mean().alias("AvgPerformance")
])
print(grouped)
```

---

### **19. Add Derived Column in Polars**


```python
pl_df = pl_df.with_columns(
    (pl.col("Salary") * 0.10).alias("BonusAmount")
)
print(pl_df.select(["Name", "Salary", "BonusAmount"]))
```

---

### **20. Compare Pandas vs Polars Performance**

**Outcome:** Use `%%timeit` in Jupyter or Python's `time` module to measure execution time for a filter.

#### ▶ Pandas

```python
import pandas as pd
import time

df = pd.read_csv("employee_performance.csv")

start = time.time()
filtered = df[(df['PerformanceScore'] > 85) & (df['Salary'] > 60000)]
end = time.time()
print("Pandas filter time:", end - start)
```

#### ▶ Polars

```python
import polars as pl
import time

pl_df = pl.read_csv("employee_performance.csv")

start = time.time()
filtered = pl_df.filter(
    (pl.col("PerformanceScore") > 85) & (pl.col("Salary") > 60000)
)
end = time.time()
print("Polars filter time:", end - start)
```


