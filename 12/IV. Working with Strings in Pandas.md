## **IV. Working with Strings in Pandas**

String processing is common in cleaning names, emails, IDs, and descriptive fields.

###  **Common String Operations**

```python
df['EmailDomain'] = df['Email'].str.split('@').str[1]
df['Name'] = df['Name'].str.title()  # Capitalizes names properly
df['Position'].str.replace('Manager', 'Lead')
```

###  **Useful Functions**

```python
df['Name'].str.contains('John', case=False)
df['Email'].str.endswith('.org')
df['ID'].str.len()
```

> Add `na=False` in string functions to avoid `NaN` errors.
