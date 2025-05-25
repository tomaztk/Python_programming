## **VI. Homework Assignment**

### **Assignment Instructions**

**Write a Python program that:**

1. **Takes a list of numbers as input from the user.**

   * The numbers should be entered as a single line, separated by commas (e.g., `3,18,9,25,4,12`).
2. **Converts the input into a list of integers.**
3. **Sorts the list in ascending order.**
4. **Filters out all numbers less than 10.**
5. **Prints the sorted and filtered list.**

---

### ** Some hints**

* Use `input()` to get the user's numbers as a string.
* Use `.split(",")` to break the string into separate pieces.
* Use a list comprehension to convert each piece to an integer: `[int(x) for x in list]`.
* Use the `.sort()` method or the `sorted()` function.
* Use another list comprehension to filter the numbers (`if n >= 10`).

---

### **Sample Solution (with Explanations and Comments)**

```python
# Step 1: Ask the user to input numbers, comma-separated
numbers_str = input("Enter numbers separated by commas: ")

# Step 2: Split the string into a list of strings
numbers_list_str = numbers_str.split(",")

# Step 3: Convert each string to an integer using list comprehension
numbers = [int(x.strip()) for x in numbers_list_str]

# Step 4: Sort the list in ascending order
numbers.sort()  # Or: numbers = sorted(numbers)

# Step 5: Filter out numbers less than 10 (keep only >= 10)
filtered_numbers = [n for n in numbers if n >= 10]

# Step 6: Print the final sorted and filtered list
print("Sorted and filtered list:", filtered_numbers)
```


