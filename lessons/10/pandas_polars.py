# Part I
import pandas as pd

data = [10, 20, 30, 40]
labels = ['a', 'b', 'c', 'd']



data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
print(df)


## polars

import polars as pl

df = pl.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
})

print(df)

# Select a single column
df.select("Name")

# Filter rows
df.filter(pl.col("Age") > 28)

# Part II


import pandas as pd

df = pd.read_csv("data/students_scores.csv")
print(df.head())

df = pd.read_excel("data/sales_data.xlsx", sheet_name="Quarter1")
print(df.head())


# working directory

import os

print(os.getcwd())  # Current working directory
# os.chdir("/Users/tomazkastrun/Documents/tomaztk_github/Python_programming/10")

# json

import pandas as pd

df = pd.read_json("data/employees.json")
print(df)

# Writing JSON data to a file
import json

data = [
    {"Name": "Alice", "Department": "HR", "Salary": 50000},
    {"Name": "Bob", "Department": "Finance", "Salary": 60000},
    {"Name": "Charlie", "Department": "IT", "Salary": 70000}
]

with open("data/employees2.json", "w") as f:
    json.dump(data, f, indent=4)


# normalization

from pandas import json_normalize
json_data = {
  "employees": [
      {"name": "Alice", "details": {"dept": "HR", "salary": 50000}},
      {"name": "Bob", "details": {"dept": "Finance", "salary": 60000}}
  ]
}

df = json_normalize(json_data['employees'], sep="_")
print(df)


# Part IV.

import pandas as pd

df = pd.read_csv("data/students_scores.csv")
print(df.head())
print(df.info())
print(df.describe())

df['Math']
df[['Math', 'English']]


df.loc[0]          # First row
df.loc[0:2]        # Rows with labels 0 to 2 inclusive
df.loc[:, 'Math']  # All rows, only 'Math' column


df[(df['Math'] > 80) & (df['Science'] > 85)]
df['Total'] = df['Math'] + df['Science'] + df['English']

# comparing pandas and polars



import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
df.head()

import pandas as pd
import polars as pl
           
dfp = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
})

print(dfp)


dfp2 = pl.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
})

print(dfp2)



import pandas as pd

# Load dataset
df = pd.read_csv("data/employees.csv")

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