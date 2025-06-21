## II. **Loading Data into Pandas**

Data analysis often starts with **loading external datasets**—typically stored in files like CSV or Excel. Pandas makes this process very easy and intuitive with built-in functions.

---

### Why Load External Data?

Real-world data doesn’t usually come from variables typed into code. Instead, data is collected and stored in:

* **CSV files** (comma-separated values)
* **Excel spreadsheets**
* **Databases**
* **Web APIs**

To analyze such data, we need to **import** it into our Python program. That’s where Pandas shines.

---

### 1. Reading CSV Files with `pd.read_csv()`

**CSV (Comma-Separated Values)** files are one of the most common formats for tabular data. Each line in a CSV file represents a row, with values separated by commas.

#### Syntax:

```python
import pandas as pd

df = pd.read_csv("filename.csv")
```

####  Parameters You Might Use:

* `sep=','`: delimiter (use `'\t'` for TSV files)
* `header=0`: row to use as column names
* `index_col=0`: column to use as the row index
* `na_values=["NA", "?"]`: treat certain strings as missing values

####  Example:

```python
df = pd.read_csv("students_scores.csv")
print(df.head())
```

##### Sample CSV: `students_scores.csv`

```
Name,Math,Science,English
Alice,85,90,78
Bob,72,80,69
Charlie,88,85,95
```

---

### 2. Reading Excel Files with `pd.read_excel()`

Excel is widely used in businesses, and Pandas allows reading Excel `.xls` or `.xlsx` files.

#### Syntax:

```python
df = pd.read_excel("filename.xlsx", sheet_name="Sheet1")
```

#### Example:

```python
df = pd.read_excel("sales_data.xlsx", sheet_name="Quarter1")
print(df.head())
```

##### Sample Excel: `sales_data.xlsx`

(Sheet name: `Quarter1`)

| Product | Region | Sales |
| ------- | ------ | ----- |
| A       | East   | 1000  |
| B       | West   | 850   |
| C       | North  | 920   |

You can create this manually in Excel or programmatically using:

```python
import pandas as pd

data = {
    "Product": ["A", "B", "C"],
    "Region": ["East", "West", "North"],
    "Sales": [1000, 850, 920]
}
df = pd.DataFrame(data)
df.to_excel("sales_data.xlsx", sheet_name="Quarter1", index=False)
```

---

###  3. Understanding File Paths and Working Directories

####  What is a File Path?

* A **file path** is the address where your data file is stored.
* **Relative path**: Refers to a file in the same or nearby folder (e.g., `"data/students.csv"`)
* **Absolute path**: Full address from the system root (e.g., `"C:/Users/Name/Desktop/data.csv"`)

####  Checking Your Current Working Directory

Use this to find or set where Python is looking for files:

```python
import os

print(os.getcwd())  # Current working directory
```

You can also change it:

```python
os.chdir("C:/Users/Name/Documents/MyProject/")
```

Or, use a **relative path** to load files from a subfolder:

```python
df = pd.read_csv("data/students_scores.csv")
```

---

###  Tips for Loading Data

* Always check the first few rows using `df.head()`
* Use `df.info()` to check structure and types
* If data isn’t displaying correctly, try tweaking parameters like `sep`, `encoding`, or `header`

---

### 4. **Reading JSON Files with `pd.read_json()`**

####  What is a JSON File?

**JSON (JavaScript Object Notation)** is a popular format for storing structured data, especially for APIs and web data. It’s a text format that is easy to read and write for both humans and machines.

* JSON structures resemble Python dictionaries and lists.
* It's often used when transferring data between servers and clients or saving complex structured data.

---

####  Reading JSON Files in Pandas

Pandas can **automatically parse** JSON files into DataFrames with the function:

```python
df = pd.read_json("filename.json")
```

---

####  Example:

```python
import pandas as pd

df = pd.read_json("employees.json")
print(df)
```

##### Sample JSON: `employees.json`

```json
[
  {"Name": "Alice", "Department": "HR", "Salary": 50000},
  {"Name": "Bob", "Department": "Finance", "Salary": 60000},
  {"Name": "Charlie", "Department": "IT", "Salary": 70000}
]
```

**Expected Output:**

```
      Name Department  Salary
0    Alice         HR   50000
1      Bob    Finance   60000
2  Charlie         IT   70000
```

---

####  Generating Sample JSON File in Python

To create the file within your script:

```python
import json

data = [
    {"Name": "Alice", "Department": "HR", "Salary": 50000},
    {"Name": "Bob", "Department": "Finance", "Salary": 60000},
    {"Name": "Charlie", "Department": "IT", "Salary": 70000}
]

with open("employees.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

### 📍 Notes When Working with JSON in Pandas

* JSON can be **nested**. For complex or deeply nested JSON, you may need to **normalize** it using `pd.json_normalize()`:

  ```python
  from pandas import json_normalize
  json_data = {
      "employees": [
          {"name": "Alice", "details": {"dept": "HR", "salary": 50000}},
          {"name": "Bob", "details": {"dept": "Finance", "salary": 60000}}
      ]
  }

  df = json_normalize(json_data['employees'], sep="_")
  print(df)
  ```

* Ensure your JSON is **well-formed** and matches the structure Pandas expects.

* Works great for data from **APIs**, logs, or systems that generate structured data.


###  Sample Files for This Lesson

Include these two datasets in your class or project folder:

#### 1. **students_scores.csv**

```
Name,Math,Science,English
Alice,85,90,78
Bob,72,80,69
Charlie,88,85,95
```

#### 2. **sales_data.xlsx**

* Sheet name: `Quarter1`
* Columns: Product, Region, Sales

To generate them in code:

```python
# CSV file
df_csv = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Math": [85, 72, 88],
    "Science": [90, 80, 85],
    "English": [78, 69, 95]
})
df_csv.to_csv("students_scores.csv", index=False)

# Excel file
df_excel = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Region": ["East", "West", "North"],
    "Sales": [1000, 850, 920]
})
df_excel.to_excel("sales_data.xlsx", sheet_name="Quarter1", index=False)
```

#### 3. **employee.json**

```json
[
  {"Name": "Alice", "Department": "HR", "Salary": 50000},
  {"Name": "Bob", "Department": "Finance", "Salary": 60000},
  {"Name": "Charlie", "Department": "IT", "Salary": 70000}
]
```


### Summary of File Types and Read Functions

| **File Type** | **Extension** | **Pandas Function** | **Example**                  |
| ------------- | ------------- | ------------------- | ---------------------------- |
| CSV           | `.csv`        | `pd.read_csv()`     | `pd.read_csv("data.csv")`    |
| Excel         | `.xlsx`       | `pd.read_excel()`   | `pd.read_excel("file.xlsx")` |
| JSON          | `.json`       | `pd.read_json()`    | `pd.read_json("file.json")`  |

---

