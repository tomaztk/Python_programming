
## **VI. Wrap Up & Homework Assignment**

### **A. Lesson Wrap Up**

#### **Key Takeaways:**

* **Operators** are used for math and comparisons.
* **Control flow** allows your program to make decisions with `if`, `elif`, and `else`.
* **Loops** (`for`, `while`) repeat code, enabling programs to process lists, handle repeated input, or perform calculations.
* **Special statements** like `break` and `continue` give you extra control over loop execution.
* When you combine these features, you can create powerful, flexible programs that interact with users and handle a wide variety of tasks.

#### **Typical Interview/Quiz Questions:**

* What’s the difference between `=` and `==`?
* How do `for` and `while` loops differ?
* What does the `break` statement do in a loop?
* How can you check if a string starts with a vowel?
* What is the output of:

  ```python
  for i in range(1, 5):
      if i % 2 == 0:
          continue
      print(i)
  ```

#### **Q\&A**

* Ask questions, clarify doubts, and discuss real-world uses of control flow and loops.

---

### **B. Homework Assignment: Fibonacci Sequence**

#### **What is the Fibonacci Sequence?**

The **Fibonacci sequence** is a famous mathematical series where **each number after the first two is the sum of the previous two numbers**.

* It starts with 0 and 1.
* The sequence goes:
  `0, 1, 1, 2, 3, 5, 8, 13, 21, ...`
* **Mathematical definition:**
  For `n ≥ 0`,

#### Latex syntax
  $$
  F(0) = 0, \quad F(1) = 1 \\
  F(n) = F(n-1) + F(n-2), \quad \text{for } n \geq 2
  $$

The Fibonacci sequence appears in nature (like the arrangement of leaves or the spiral patterns of shells), computer science, and many other areas.

---

#### **Homework Instructions**

Write a Python program that:

1. **Asks the user how many terms** of the Fibonacci sequence to generate.
2. **Generates and prints** the Fibonacci sequence up to that many terms.
3. **Displays only the even Fibonacci numbers** from the sequence on a separate line.
4. **Calculates and prints the sum** of all Fibonacci numbers generated.
5. **Handles invalid input** (like zero or negative numbers) gracefully.

**Bonus challenge:**

* After finishing, allow the user to repeat the process for a new number of terms.

---

#### **Example Output:**

```
How many terms? 8

Fibonacci sequence:
0 1 1 2 3 5 8 13

Even Fibonacci numbers:
0 2 8

Sum of all Fibonacci numbers: 34
```

---

#### **Starter Code (Optional):**

```python
n = int(input("How many terms? "))

a, b = 0, 1
fib_sum = 0

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=' ')
    fib_sum += a
    a, b = b, a + b

# Students: Add code to collect and display even numbers, and show the sum at the end.
```

---

**Tip:**
Try breaking the problem into steps:

* Use a loop to generate Fibonacci numbers,
* Use an `if` statement to check for even numbers,
* Use a variable to keep track of the sum.

**Bring your solution and questions to the next session for discussion and feedback!**


**Keep coding!**
