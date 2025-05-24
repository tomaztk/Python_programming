## **Solutions: Python Data Structures - Tuples and Lists**



### **1. Tuple Creation & Access**

```python
fruits = ("apple", "banana", "orange", "grape", "mango")
print(fruits[0])   # First fruit: apple
print(fruits[-1])  # Last fruit: mango
```

---

### **2. Unpacking Tuples**

```python
person = ("Alice", 21, "USA")
name, age, country = person
print(f"Name: {name}, Age: {age}, Country: {country}")
```

---

### **3. Tuple Immutability**

```python
my_tuple = (1, 2, 3)
try:
    my_tuple[1] = 20
except TypeError as e:
    print("Error:", e)
# Output: Error: 'tuple' object does not support item assignment
```

---

### **4. Tuple with Mixed Data Types**

```python
data = (10, 3.14, "hello", True)
for item in data:
    print(item, type(item))
```

---

### **5. List Creation and Manipulation**

```python
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 25)
numbers.remove(40)
print(numbers)  # Output: [10, 25, 20, 30, 50, 60]
```

---

### **6. Slicing Lists and Tuples**

```python
nums = [5, 10, 15, 20, 25, 30]
print(nums[:3])   # [5, 10, 15]
print(nums[-2:])  # [25, 30]
```

---

### **7. List Methods Practice**

```python
cities = ["London", "Paris", "Rome"]
cities.append("Berlin")
print(cities)   # ['London', 'Paris', 'Rome', 'Berlin']

cities.pop()
print(cities)   # ['London', 'Paris', 'Rome']

cities.reverse()
print(cities)   # ['Rome', 'Paris', 'London']

cities.sort()
print(cities)   # ['London', 'Paris', 'Rome']
```

---

### **8. Converting Between Tuples and Lists**

```python
my_tuple = (1, 2, 3, 4)
temp_list = list(my_tuple)
temp_list.append(5)
my_tuple = tuple(temp_list)
print(my_tuple)  # (1, 2, 3, 4, 5)
```

---

### **9. Looping Through Tuples and Lists**

```python
def print_even_numbers(numbers):
    for n in numbers:
        if n % 2 == 0:
            print(n)

print_even_numbers([1, 2, 3, 4, 5, 6])
# Output: 2 4 6
```

---

### **10. Nested Lists**

```python
marks = [
    [85, 90, 92],    # Student 1
    [78, 88, 80],    # Student 2
    [90, 91, 89]     # Student 3
]
for i, student_marks in enumerate(marks, start=1):
    print(f"Student {i}: {student_marks}")
```

---

### **11. Using Lists with Input**

```python
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
```


---

### **12. List Comprehensions**

```python
numbers = [2, 4, 6, 8]
squares = [n ** 2 for n in numbers]
print(squares)  # [4, 16, 36, 64]
```

---

### **13. Finding Duplicates in a List**

```python
nums = [1, 2, 3, 2, 4, 5, 3, 6, 1]
duplicates = []
for n in nums:
    if nums.count(n) > 1 and n not in duplicates:
        duplicates.append(n)
print(duplicates)  # [1, 2, 3]
```

---

### **14. Functions Returning Tuples**

```python
def sum_and_product(a, b):
    return (a + b, a * b)

result = sum_and_product(5, 3)
print("Sum:", result[0])
print("Product:", result[1])
```

---

### **15. Combining Strings and Lists**

```python
csv = "banana,apple,mango,pear"
fruits_list = csv.split(",")
fruits_list.sort()
sorted_csv = ",".join(fruits_list)
print(sorted_csv)  # apple,banana,mango,pear
```

