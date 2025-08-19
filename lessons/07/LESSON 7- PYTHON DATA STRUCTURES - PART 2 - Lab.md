## LESSON 7: PYTHON DATA STRUCTURES - PART 2 (Exercise)



### **Dictionaries**

**1. Create a Contact Book**
Write code to create a dictionary called `contacts` where the keys are names and the values are phone numbers. Add at least three contacts. Print the dictionary.

---

**2. Update a Dictionary Value**
Given the dictionary below, update the city to "San Francisco":

```python
person = {'name': 'Tom', 'age': 30, 'city': 'New York'}
```

---

**3. Delete an Entry**
Remove the `'age'` key from the `person` dictionary above and print the updated dictionary.

---

**4. Loop Through Keys and Values**
Write a loop that prints every key and value in the following dictionary:

```python
scores = {'Alice': 90, 'Bob': 82, 'Charlie': 95}
```

---

**5. Count Word Occurrences**
Given a list of words:

```python
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
```

Use a dictionary to count how many times each word appears.

---

**6. Nested Dictionaries – Student Records**
Create a dictionary `students` with three students. Each student should have their own dictionary with `'age'` and `'marks'` as keys.

---

**7. Retrieve All Keys and Values**
Given any dictionary, write code to print all the keys and all the values (each on a new line).

---

**8. Dictionary from Two Lists**
Given two lists:

```python
keys = ['id', 'name', 'email']
values = [1, 'Sarah', 'sarah@example.com']
```

Create a dictionary that combines them.

---

### **Sets**

**9. Remove Duplicates from a List**
Given a list with duplicate numbers, convert it into a set to remove duplicates, and then print the result as a list.

---

**10. Set Operations – Union and Intersection**
Given two sets of numbers, find their union and intersection:

```python
a = {1, 3, 5, 7}
b = {3, 4, 5, 6}
```

---

**11. Check Membership**
Write code to check if the element `10` is present in the set

```python
numbers = {2, 4, 6, 8, 10, 12}
```

---

**12. Add and Remove Set Elements**
Create a set called `animals` with values `'cat'`, `'dog'`, and `'parrot'`. Add `'hamster'` and remove `'dog'`.

---

**13. Common Elements in Two Lists**
Given two lists, use sets to find which elements are common:

```python
list1 = [2, 4, 6, 8, 10]
list2 = [3, 6, 9, 12, 15]
```

---

### **Combined / Application**

**14. Unique Words in a Sentence**
Write a program that takes a sentence from the user, splits it into words, and prints all the unique words (ignore case).

---

**15. Frequency Dictionary from a String**
Given a string, create a dictionary that counts how many times each letter appears (ignore spaces and case).

Example input:

```python
sentence = "Python Programming"
```

**16. Word Frequency Counter**

Write a function that receives a string as input and returns a dictionary where the keys are words and the values are the number of times each word appears in the string. Ignore case and punctuation. Use a loop to build the dictionary.


**17. Student Grades Analyzer**

Given a dictionary where the keys are student names and the values are lists of their grades (integers), write a function to create a new dictionary where each student name maps to their average grade. Use a loop to calculate averages.
