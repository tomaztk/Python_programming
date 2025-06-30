##  **V. Working with Index and MultiIndex**

The index in a DataFrame helps uniquely identify rows and improves performance for lookups and joins.

###  **Basic Index Manipulation**

```python
df.set_index('EmployeeID', inplace=True)
df.reset_index(inplace=True)
```

* `set_index()` moves a column into the index.
* `reset_index()` returns it back to a column.

###  **Creating MultiIndex**

```python
grouped = df.groupby(['Department', 'Location']).mean()
```

This creates a **hierarchical index** with two levels.

###  **Accessing MultiIndex Rows**

```python
grouped.loc[('Sales', 'NY')]
```

###  **Flattening MultiIndex Columns**

```python
df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]
```

* Useful after aggregating with `groupby().agg()`.
