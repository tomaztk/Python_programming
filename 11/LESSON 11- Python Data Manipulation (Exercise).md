
## LESSON 11: MANIPULATING DATA IN PYTHON – PART 1

### **Hands-On Practice Assignments (20 Exercises)**


* Data loading, cleaning, transformation
* Conditionals, loops, user-defined functions
* Performance comparison: Pandas vs. Polars
* NumPy vectorized operations

---

## 📁 Dataset: `employee_performance.csv`

```csv
EmployeeID,Name,Department,Gender,Age,Salary,YearsExperience,PerformanceScore,BonusEligible,Location
101,Alice,HR,Female,29,52000,4,88,Yes,New York
102,Bob,Finance,Male,34,61000,7,77,No,Chicago
103,Charlie,IT,Male,41,72000,10,90,Yes,San Francisco
104,Daisy,Finance,Female,28,59000,3,81,Yes,Boston
105,Edward,IT,Male,36,73000,9,85,Yes,Chicago
106,Fiona,HR,Female,26,51000,2,72,No,New York
107,George,Marketing,Male,30,56000,5,75,No,Los Angeles
108,Helen,Finance,Female,38,64000,8,93,Yes,Chicago
109,Ian,Marketing,Male,45,58000,12,65,No,Los Angeles
110,Jane,IT,Female,32,70000,6,91,Yes,San Francisco
```

> Save this as `employee_performance.csv` in your project folder.

---

###  **Part-A. Data Exploration & Cleansing**

---

#### **1. Load and Inspect the Dataset**

**🧾 Outcome:** Use Pandas to load and display the first 5 rows.

```python
df = pd.read_csv("employee_performance.csv")
print(df.head())
```

---

#### **2. Dataset Overview**

**🧾 Outcome:** Use `.info()`, `.describe()`, and `.shape` to inspect structure and stats.

---

#### **3. Fill Missing Values**

**🧾 Outcome:** Replace any missing experience or salary values (if added later) with the mean.

---

#### **4. Rename Columns for Clarity**

**🧾 Outcome:** Rename `'YearsExperience'` to `'ExperienceYears'`, `'Salary'` to `'AnnualSalary'`.

---

### **Part-B. Data Selection, Filtering, Sorting**

---

#### **5. Filter High Performers**

**Outcome:** Filter all employees with `PerformanceScore > 85` and print their names and departments.

---

#### **6. Sort by Experience and Performance**

**Outcome:** Sort the dataset by `'ExperienceYears'` descending, then `'PerformanceScore'`.

---

#### **7. Conditional Column Creation**

**Outcome:** Add a column `'PerformanceTier'`:

* `'High'` if score ≥ 85
* `'Medium'` if 70–84
* `'Low'` otherwise

---

### **Part-C. Aggregation & Grouping**

---

#### **8. Department Performance Summary**

**Outcome:** Group by `'Department'`, calculate:

* Average salary
* Average performance

---

#### **9. Bonus Eligibility Rate by Department**

**Outcome:** Count how many in each department are `'BonusEligible' == "Yes"` and calculate percentage.

---

### **Part-D. NumPy Integrations**

---

#### **10. Calculate Z-Scores for Salary**

**Outcome:** Use NumPy to add a `'SalaryZScore'` column:

```python
from scipy.stats import zscore
df['SalaryZScore'] = zscore(df['AnnualSalary'])
```

---

#### **11. Normalize Performance Scores (0 to 1)**

**Outcome:** Apply min-max normalization using NumPy:

```python
df['PerfNorm'] = (df['PerformanceScore'] - df['PerformanceScore'].min()) / (df['PerformanceScore'].max() - df['PerformanceScore'].min())
```

---

### **Part-E. Functions & Loops**

---

#### **12. Define Function to Flag Promotions**

**Outcome:** Write a function `is_promotable(score, experience)` returning `"Yes"` if score > 85 and experience > 5.

Apply it across the DataFrame to create a new column.

---

#### **13. Loop Through and Print Custom Reports**

**Outcome:** Use a `for` loop to print:

> "Alice (HR) is eligible for a bonus."
> "Bob (Finance) is not eligible..."

---

### **Part-F. Advanced Filtering and Logic**

---

#### **14. Filter by Multiple Conditions**

**Outcome:** Display IT employees in San Francisco with salary > 70,000.

---

#### **15. Employees Close to Retirement**

**Outcome:** Add a column `'RetirementRisk'` set to `"Yes"` if `Age > 40`, otherwise `"No"`.

---

###  **Part-G. Polars Comparisons**

---

#### **16. Load Dataset with Polars**

**Outcome:** Load the same CSV with Polars and display first 5 rows.

```python
import polars as pl
pl_df = pl.read_csv("employee_performance.csv")
print(pl_df.head())
```

---

#### **17. Filter in Polars (PerformanceScore > 85)**

**Outcome:** Use Polars syntax to filter high performers.

```python
pl_df.filter(pl.col("PerformanceScore") > 85)
```

---

#### **18. Group and Aggregate in Polars**

**Outcome:** Group by `'Department'`, calculate mean `Salary` and `PerformanceScore`.

---

#### **19. Add Derived Column in Polars**

**Outcome:** Add a column `'BonusAmount' = Salary * 0.1` in Polars.

---

#### **20. Compare Pandas vs. Polars Performance**

** Outcome:** Use a large version of the dataset (100k+ rows).

* Compare time to filter high performers in Pandas vs. Polars using `time` or `%%timeit`.

---

## Additional:

* Try replicating one Polars operation in Pandas and compare line-by-line syntax.
* Export filtered data to CSV using both libraries.

