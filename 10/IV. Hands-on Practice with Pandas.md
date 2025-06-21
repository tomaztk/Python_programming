
##  **IV. Hands-on Practice with Pandas**

Reinforce core concepts through practical data manipulation tasks using **real-world-style datasets**.

---

###  Dataset Sources

We’ll use two types of datasets:

1. **Built-in dataset** via `seaborn` (Iris or Titanic)
2. **CSV file** (e.g. `employees.csv` or `students_scores.csv` from earlier)

---

###  Step-by-Step Practice Tasks

---

###  1. **Loading a Dataset**

#### Example A – Load Titanic dataset from `seaborn`:

```python
import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
df.head()
```

#### Example B – Load a CSV file:

```python
df = pd.read_csv("employees.csv")
df.head()
```

##### Sample `employees.csv`:

```
Name,Department,Salary,Experience,Location
Alice,HR,50000,3,New York
Bob,Finance,60000,5,Chicago
Charlie,IT,70000,8,San Francisco
Daisy,Finance,58000,,Boston
Edward,IT,72000,7,Chicago
```

---

###  2. **Column Selection**

Why? You often only need a subset of columns for your analysis or modeling.

```python
df[['Name', 'Salary']]
```

> Use column selection to narrow your focus to relevant data.

---

###  3. **Row Filtering**

Why? To analyze specific groups or remove irrelevant entries.

#### Example: Filter employees with salary above 60,000

```python
df[df['Salary'] > 60000]
```

#### Combine filters:

```python
df[(df['Salary'] > 60000) & (df['Department'] == 'IT')]
```

> Filtering lets you zoom into meaningful segments (e.g., high earners, specific departments).

---

###  4. **Sorting Data**

Why? Sorting helps rank or prioritize based on values.

```python
df.sort_values(by='Experience', ascending=False)
```

> Tip: Combine with `head()` to get top performers or outliers.

---

###  5. **Summarizing Data**

Why? Summarization gives insights into distributions, totals, or averages.

```python
df['Salary'].mean()
df.groupby('Department')['Salary'].mean()
```

> Use `.groupby()` for department-level aggregations or comparisons.

---

###  6. **Basic Cleaning**

####  Rename Columns

Why? Column names might be messy, inconsistent, or unclear.

```python
df.rename(columns={'Experience': 'YearsExperience'}, inplace=True)
```

####  Handle Missing Values

Why? Missing data can break functions or skew results.

Check missing:

```python
df.isnull().sum()
```

Remove rows with missing values:

```python
df.dropna(inplace=True)
```

Or fill missing values:

```python
df['Experience'] = df['Experience'].fillna(0)
```

---

###  Combined Demo: Real Use Case

```python
import pandas as pd

# Load dataset
df = pd.read_csv("employees.csv")

# Step 1: View structure
print(df.info())

# Step 2: Select relevant columns
df = df[['Name', 'Department', 'Salary', 'Experience']]

# Step 3: Filter employees with 5+ years experience
experienced = df[df['Experience'] >= 5]

# Step 4: Sort by salary
experienced_sorted = experienced.sort_values(by='Salary', ascending=False)

# Step 5: Add new column for tax estimate (just for fun)
df['TaxEstimate'] = df['Salary'] * 0.25

# Step 6: Rename column
df.rename(columns={'Experience': 'YearsExperience'}, inplace=True)

# Step 7: Fill missing experience
df['YearsExperience'] = df['YearsExperience'].fillna(0)

print(df.head())
```

---

### Bonus Dataset for Practice: `students_scores.csv`

(Same as used previously — use it for practice with academic data.)

---

### Summary: Why These Skills Matter

| **Skill**        | **Purpose**                                 |
| ---------------- | ------------------------------------------- |
| Column selection | Focus analysis on relevant variables        |
| Row filtering    | Target groups or exclude unwanted data      |
| Sorting          | Rank values or find top/bottom entries      |
| Summarization    | Understand data trends and compute metrics  |
| Cleaning         | Prepare clean data for analysis or modeling |

