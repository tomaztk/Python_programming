## **V. Hands-On Practice (20 min)**

Let students try these tasks **step by step**, encourage them to experiment, and discuss their results. You can guide, check, and answer questions as they go!

---

### **1. Lists Practice**

#### **a. Create a list of 5 favorite movies.**

This shows how to create and store multiple items in a list.

```python
movies = ['Inception', 'Before the rain', 'The Matrix', 'Splav Meduze', 'Top Gun']
```

---

#### **b. Print the first and last movie.**


Practices indexing (positive and negative).

```python
print("First movie:", movies[0])
print("Last movie:", movies[-1])
```

**Expected Output:**

```
First movie: Inception
Last movie: Top Gun
```

---

#### **c. Replace the third movie.**


Shows how to change an item in a list (lists are mutable).

```python
movies[2] = 'Interstellar'  # Change 'The Matrix' to 'Interstellar'
print(movies)
```

**Expected Output:**

```
['Inception', 'Before the rain', 'Interstellar', 'Splav Meduze', 'Top Gun']
```

---

#### **d. Add a new movie at the end.**

*Why?*
Demonstrates adding with `.append()`.

```python
movies.append('The Godfather')
print(movies)
```

**Expected Output:**

```
['Inception', 'Before the rain', 'Interstellar', 'Splav Meduze', 'Top Gun', 'The Godfather']
```

---

#### **e. Remove one movie by name.**

*Why?*
Shows how to remove an item by value.

```python
movies.remove('Before the rain')
print(movies)
```

**Expected Output:**

```
['Inception', 'Interstellar', 'Splav Meduze', 'Top Gun', 'The Godfather']
```

---

### **2. Tuples Practice**

#### **a. Create a tuple with 3 cities.**

*Why?*
Demonstrates how to store multiple values in a tuple.

```python
cities = ('Seoul', 'Busan', 'Pohang')
```

---

#### **b. Print each city using a loop.**


Shows how to iterate over a tuple.

```python
for city in cities:
    print(city)
```

**Expected Output:**

```
Seoul
Busan
Pohang
```

---

#### **c. Try to change one city (observe the error).**


Shows immutability—tuples can’t be changed.

```python
# Try this (it will cause an error!)
# cities[1] = 'Asan-si'
```

**Expected Output:**

```
TypeError: 'tuple' object does not support item assignment
```

**Explanation:**
Unlike lists, you **cannot** change the value of any item in a tuple after creation.

---

#### **d. Unpack the tuple into variables.**


Shows how to assign tuple elements to multiple variables at once.

```python
city1, city2, city3 = cities
print(city1)
print(city2)
print(city3)
```

**Expected Output:**

```
Seoul
Busan
Pohang
```

---

### **Extra Challenge (if time allows):**

* **List:**
  Ask the user for a new movie to add to their list (use `input()`), then print the updated list.
* **Tuple:**
  Create a tuple of (latitude, longitude) for a city and print both using unpacking.



