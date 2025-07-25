## LESSON 7: PYTHON DATA STRUCTURES - PART 2 (Exercise) - Solution

### **Dictionaries**

---

**1. Create a Contact Book**

```python
contacts = {
    'Alice': '123-456-7890',
    'Bob': '234-567-8901',
    'Charlie': '345-678-9012'
}
print(contacts)
```

---

**2. Update a Dictionary Value**

```python
person = {'name': 'Tom', 'age': 30, 'city': 'New York'}
person['city'] = 'San Francisco'
print(person)
```

---

**3. Delete an Entry**

```python
del person['age']
print(person)
```

*Note: This uses the updated `person` from the previous question.*

---

**4. Loop Through Keys and Values**

```python
scores = {'Alice': 90, 'Bob': 82, 'Charlie': 95}
for name, score in scores.items():
    print(f"{name}: {score}")
```

---

**5. Count Word Occurrences**

```python
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)
```

---

**6. Nested Dictionaries – Student Records**

```python
students = {
    'Alice': {'age': 19, 'marks': 85},
    'Bob': {'age': 20, 'marks': 90},
    'Carol': {'age': 21, 'marks': 78}
}
print(students)
```

---

**7. Retrieve All Keys and Values**

```python
sample_dict = {'x': 1, 'y': 2, 'z': 3}
print("Keys:")
for key in sample_dict.keys():
    print(key)
print("Values:")
for value in sample_dict.values():
    print(value)
```

*You can replace `sample_dict` with any dictionary.*

---

**8. Dictionary from Two Lists**

```python
keys = ['id', 'name', 'email']
values = [1, 'Sarah', 'sarah@example.com']
combined = dict(zip(keys, values))
print(combined)
```

---

### **Sets**

---

**9. Remove Duplicates from a List**

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)
```

---

**10. Set Operations – Union and Intersection**

```python
a = {1, 3, 5, 7}
b = {3, 4, 5, 6}
union = a | b         # or a.union(b)
intersection = a & b  # or a.intersection(b)
print("Union:", union)
print("Intersection:", intersection)
```

---

**11. Check Membership**

```python
numbers = {2, 4, 6, 8, 10, 12}
if 10 in numbers:
    print("10 is in the set")
else:
    print("10 is not in the set")
```

---

**12. Add and Remove Set Elements**

```python
animals = {'cat', 'dog', 'parrot'}
animals.add('hamster')
animals.remove('dog')
print(animals)
```

---

**13. Common Elements in Two Lists**

```python
list1 = [2, 4, 6, 8, 10]
list2 = [3, 6, 9, 12, 15]
common = set(list1) & set(list2)
print("Common elements:", common)
```

---

### **Combined / Application**

---

**14. Unique Words in a Sentence**

```python
sentence = input("Enter a sentence: ")
#remove commas or stops
sentence = sentence.replace(".", " ")
words = sentence.lower().split()
unique_words = set(words)
print("Unique words:", unique_words)
```

---

**15. Frequency Dictionary from a String**

```python
sentence = "Python Programming"
frequency = {}
for char in sentence.lower():
    if char != ' ':  # or we can replace " " with ""
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
print(frequency)
```

**16. Word Frequency Counter**

```python
# import string
s = "Hello hello, world today, Hello"
s = s.lower()
# Remove punctuation
s = s.translate(str.maketrans('', '', string.punctuation))
words = s.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)
```

**16. Student Grades Analysis**

```python
students = {'Alice': [90, 85, 88], 'Bob': [78, 80], 'Carol': []}
averages = {}
for student, grades in students.items():
    if grades:
        avg = sum(grades) / len(grades)
        averages[student] = avg
    else:
        averages[student] = None  # or 0
print(averages)
```