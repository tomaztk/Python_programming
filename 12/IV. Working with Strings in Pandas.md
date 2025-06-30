## **IV. Working with Strings in Pandas**


String processing is a fundamental part of data cleaning, feature extraction, and formatting—especially for columns like names, emails, text notes, and categorical labels.

To apply string functions in Pandas, use the `.str` accessor: `df['column'].str.method()`.

---

###  **1. Basic String Operations**

Let’s clean and extract some useful information from the `Name` and `Email` columns.

#### **Capitalize names properly**

```python
df['Name_Clean'] = df['Name'].str.title()
```

> Converts `alice johnson` to `Alice Johnson`.

#### **Extract email domain**

```python
df['EmailDomain'] = df['Email'].str.split('@').str[1]
```

> Extracts `"example.com"` from `"alice@example.com"`.

#### **Remove or replace values**

```python
df['IsRemote_Recode'] = df['IsRemote'].str.replace('Yes', 'Remote').str.replace('No', 'Onsite')
```

---

### **2. Filtering with String Conditions**

These operations are useful for selecting rows based on string patterns.

#### **Check if name contains a word**

```python
df[df['Name'].str.contains('li', case=False, na=False)]
```

> Finds names containing “li” (like `Alice`, `Charlie`, `Grace Li`).

#### **Emails ending with `.org`**

```python
df[df['Email'].str.endswith('.org', na=False)]
```

> Useful for filtering domains (e.g., `.edu`, `.com`, `.gov`).

#### **String length**

```python
df['NameLength'] = df['Name'].str.len()
```

> Counts the number of characters in each name.

---

###  **3. Cleaning and Formatting**

String functions help clean up inconsistencies.

####  **Convert to lowercase or uppercase**

```python
df['Name_Lower'] = df['Name'].str.lower()
df['Name_Upper'] = df['Name'].str.upper()
```

#### **Strip extra whitespace**

```python
df['Name_Strip'] = df['Name'].str.strip()
```

> Removes leading/trailing whitespace.

---

### **4. Extract and Split**

#### **Extract username from email**

```python
df['EmailUser'] = df['Email'].str.extract(r'(^[^@]+)')
```

#### **Split full name into first and last**

```python
df[['FirstName', 'LastName']] = df['Name'].str.split(' ', n=1, expand=True)
```

> Uses `n=1` to split only on the first space.

---

### **5. Advanced Matching (Optional)**

#### **Startswith / endswith**

```python
df[df['Name'].str.startswith('A', na=False)]
df[df['Email'].str.endswith('.net', na=False)]
```

#### **Regex search**

```python
df[df['Email'].str.contains(r'\.org$', regex=True, na=False)]
```

---

### Summary: Common `.str` Operations

| Task                 | Code Example                                            |
| -------------------- | ------------------------------------------------------- |
| Capitalize Names     | `df['Name'].str.title()`                                |
| Extract Email Domain | `df['Email'].str.split('@').str[1]`                     |
| Replace Text         | `df['IsRemote'].str.replace('Yes', 'Remote')`           |
| Contains Pattern     | `df['Name'].str.contains('john', case=False, na=False)` |
| Ends With `.org`     | `df['Email'].str.endswith('.org', na=False)`            |
| String Length        | `df['Name'].str.len()`                                  |
| Split Full Name      | `df['Name'].str.split(' ', n=1, expand=True)`           |
| Extract Username     | `df['Email'].str.extract(r'(^[^@]+)')`                  |
| Strip Whitespace     | `df['Name'].str.strip()`                                |
| Count Domain Types   | `df['Email'].str.extract(r'\.([a-z]+)$')`               |

