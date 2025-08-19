##  **V. Working with Index and MultiIndex**

The index in a DataFrame helps uniquely identify rows and improves performance for lookups and joins. It helps in **data alignment, faster lookups, slicing**, and organizing complex structures like **hierarchical indexes (MultiIndex)**.

---

###  **Setting and Resetting Index**

By default, Pandas uses integer index (0, 1, 2...). We can set meaningful columns as index.

#### Set `EmployeeID` as index

```python
df_indexed = df.set_index('EmployeeID')
print(df_indexed.head())
```

This makes `EmployeeID` the unique identifier for each row.

#### Reset to default index

```python
df_reset = df_indexed.reset_index()
```

>  Use `inplace=True` to modify the DataFrame directly.

---

###  **Setting a MultiIndex**

A **MultiIndex** is a hierarchical index — useful when grouping by multiple dimensions like `Department` and `Location`.

#### Set MultiIndex with `Department` and `Location`

```python
df_multi = df.set_index(['Department', 'Location'])
print(df_multi.head())
```

This nests `Location` under each `Department`.

---

### **Accessing Data with MultiIndex**

Once you have a MultiIndex, you can **select** data by a combination of levels:

```python
# Get all rows in the IT department and NY location
print(df_multi.loc[('IT', 'NY')])
```

You can also **slice** across levels using `.loc` with `pd.IndexSlice`:

```python
idx = pd.IndexSlice
print(df_multi.loc[idx[:, 'NY'], :])  # All departments in NY
```

---

### **Sorting and Working with MultiIndex**

A MultiIndex must be **sorted** for slicing and some operations:

```python
df_multi_sorted = df_multi.sort_index()
```

###  **Resetting a MultiIndex**

If you want to convert a MultiIndex back to regular columns:

```python
df_reset_multi = df_multi.reset_index()
```

---

###  **Example: Aggregating with MultiIndex**

Group by Department and Location:

```python
grouped = df.groupby(['Department', 'Location'])[['Salary', 'ExperienceYears']].mean()
print(grouped)
```

Access one group:

```python
grouped.loc[('IT', 'NY')]
```

Flatten MultiIndex columns after `agg()`:

```python
agg_df = df.groupby(['Department', 'Location']).agg({
    'Salary': ['mean', 'max'],
    'ExperienceYears': 'median'
})

# Flatten the columns
agg_df.columns = ['_'.join(col) for col in agg_df.columns]
agg_df.reset_index(inplace=True)
print(agg_df)
```

###  **Flattening MultiIndex Columns**

```python
df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]
```

* Useful after aggregating with `groupby().agg()`.
