

# ** LESSON 12: MANIPULATING DATA IN PYTHON – PART 2**

## **DATA AGGREGATION AND CLEANING**


** Goal:** Equip learners with essential techniques to clean, prepare, and summarize data using **Pandas** (and optionally Polars).

---

## **Recap of Lesson 11**

* Reviewed Pandas & NumPy basics
* Practiced selection, filtering, sorting
* Created functions, used loops, and compared Polars vs. Pandas
* Focused on performance insights and transformation pipelines

---

## **1. Data Cleaning in Pandas**

Data cleaning ensures accuracy and consistency before analysis or modeling.

###  Handling Missing Data

#### **Detect missing values**

```python
df.isnull().sum()
```

#### **Drop missing values**

```python
df.dropna(inplace=True)
```

#### **Fill missing values**

```python
df['Column'].fillna(df['Column'].mean(), inplace=True)
```

> Tip: Use `median()` or `mode()` for categorical data.

---

###  Handling Duplicates

#### **Check duplicates**

```python
df.duplicated().sum()
```

#### **Drop duplicates**

```python
df.drop_duplicates(inplace=True)
```

---

###  Detecting and Handling Outliers

#### **Using IQR method**

```python
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Salary'] < Q1 - 1.5 * IQR) | (df['Salary'] > Q3 + 1.5 * IQR)]
```

> Optionally: Remove or cap/floor them using `clip()`.

---

##  **2. Data Aggregation in Pandas**

Aggregating data helps summarize information at group level (e.g., by department, location).

###  Using `groupby()`

```python
df.groupby('Department')['Salary'].mean()
```

Group by multiple columns:

```python
df.groupby(['Department', 'Location'])['Salary'].agg(['mean', 'count'])
```

---

###  Using `agg()` for custom aggregations

```python
df.groupby('Department').agg({
    'Salary': ['mean', 'max'],
    'ExperienceYears': 'median'
})
```

---

###  Using `pivot_table()`

```python
df.pivot_table(values='Salary', index='Department', columns='Location', aggfunc='mean')
```

>  Pivot tables are great for cross-tab reports.

---

###  Merging and Joining DataFrames

Combine multiple datasets for integrated analysis.

#### **Example: Merge employee and performance tables**

```python
pd.merge(df1, df2, on='EmployeeID', how='inner')
```

* `how='inner'`, `'outer'`, `'left'`, `'right'`

---

##  **3. Hands-on Practice**

###  Dataset: `employee_performance.csv`

####  Practice Tasks

1. Load dataset and check for missing values
2. Fill missing `YearsExperience` with mean
3. Remove any duplicated rows
4. Identify outliers in `PerformanceScore`
5. Group by `Department` to calculate average salary and experience
6. Create a pivot table showing average salary per department/location
7. Merge with another mini dataset (e.g., project assignments)

---

##  **4. Homework Assignment**

Clean and summarize a dataset using Pandas


1. Load a dataset (`employee_performance.csv`)
2. Identify and fill missing values
3. Drop duplicate records (if any)
4. Detect and optionally handle outliers in salary
5. Group by department and calculate:

   * Average salary
   * Headcount
6. Create a pivot table of average performance score by department/location
7. Export the cleaned dataset to a new CSV

 

##  **Additional Topics to Cover in Lesson 12**

###  **Pandas**

####  1. **Working with Dates and Time**

* `pd.to_datetime()`
* Extracting year, month, day: `df['date'].dt.year`
* Filtering by date ranges

**Example:**

```python
df['HireDate'] = pd.to_datetime(df['HireDate'])
df[df['HireDate'].dt.year > 2020]
```

---

####  2. **Value Counts and Unique Values**

* `.value_counts()` for frequency
* `.nunique()` for distinct counts

**Example:**

```python
df['Department'].value_counts()
df['Location'].nunique()
```

---

####  3. **String Operations**

* `.str.lower()`, `.str.contains()`, `.str.replace()`

**Example:**

```python
df[df['Name'].str.contains("an")]
df['Name'] = df['Name'].str.upper()
```

---

#### 4. **Cutting and Binning Data**

* Use `pd.cut()` or `pd.qcut()` to segment continuous values into categories

**Example:**

```python
df['ExperienceLevel'] = pd.cut(df['ExperienceYears'], bins=[0, 3, 6, 10], labels=["Junior", "Mid", "Senior"])
```

---

###  **NumPy**

####  5. **Array Broadcasting and Element-wise Operations**

* Apply transformations over arrays efficiently

**Example:**

```python
salaries = df['Salary'].values
adjusted = salaries * 1.1  # apply 10% raise
```

---

####  6. **Logical Indexing and Masking with NumPy**

* Use `np.where()` or boolean masks

**Example:**

```python
df['Bonus'] = np.where(df['PerformanceScore'] > 85, 5000, 0)
```

---

###  **Polars**

####  7. **Lazy Execution in Polars**

* Use `scan_csv()` and `.collect()` for efficient data pipelines

**Example:**

```python
lazy_df = pl.scan_csv("employee_performance.csv")
result = lazy_df.filter(pl.col("Salary") > 60000).select(["Name", "Salary"]).collect()
```

---

####  8. **Apply/Map-Like Transformations (Functional Style)**

* Polars discourages row-wise loops; use expressions and chaining

**Example:**

```python
pl_df.with_columns(
    (pl.col("PerformanceScore") > 85).cast(pl.Utf8).alias("HighPerformer")
)
```

---

###  Bonus Concepts (Optional)

####  9. **Chaining in Pandas (Method Chaining Style)**

Encourage writing clean, chainable data transformation pipelines:

```python
df_filtered = (
    df[df['Salary'] > 60000]
    .groupby('Department')
    .agg({'Salary': 'mean'})
    .reset_index()
)
```

---

###  Suggested Integration into Lesson 12:

| Topic                     | Integration Point                 |
| ------------------------- | --------------------------------- |
| Value counts / string ops | During data exploration           |
| Grouping & pivoting       | Include `cut()`, `qcut()` bins    |
| NumPy masks, where        | While building bonus/salary logic |
| Polars lazy execution     | At end or bonus material          |
| Date parsing              | Add optional column in dataset    |


