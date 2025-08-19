# LESSON 3: PYTHON CONTROL FLOW (Exercises & Solutions)

## Instructions

* Try to solve each problem on your own before checking the solution.
* If you get stuck, look at the hint, then try again before looking at the code.

---

### 1. Even or Odd?

**Task:**
Ask the user for a number and print whether it is even or odd.

**Solution:**

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### 2. Positive, Negative, or Zero

**Task:**
Prompt the user to enter a number. Print whether the number is positive, negative, or zero.

**Solution:**

```python
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---


### 4. Grade Evaluator

**Task:**
Get a score from the user (0-100). Print the corresponding letter grade.

**Solution:**

```python
score = int(input("Enter your score (0-100): "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

---

### 5. Multiplication Table

**Task:**
Print the multiplication table for a number (1 to 10).

**Solution:**

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

---

### 6. Sum of N Numbers

**Task:**
Calculate the sum from 1 to N.

**Solution:**

```python
n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
```

---

### 7. Countdown

**Task:**
Count down from 10 to 1 using a `while` loop.

**Solution:**

```python
i = 10
while i > 0:
    print(i)
    i -= 1
    #i = i - 1
```

---

### 8. Print All Even Numbers Between 1 and 50

**Task:**
Print all even numbers between 1 and 50.

**Solution:**

```python
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
```

---

### 9A. Number Guessing Game (Basic)

**Task:**
Guess a secret number (set to 7).

**Solution:**

```python
secret = 7
guess = None
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
```

---

### 9B. Number Guessing Game (Advanced)r

**Task:**
Guess a secret number (set to 7).
Calculates the success ratio and warns user of repeated guess

```
print("\n“")
print("Welcome to the Guessing Game!\n")
print("Try to guess the secret number between 1 and 10.")


secret = 7
guesses = set()  # Stores unique valid guesses
all_tries = 0    # Counts every input (including repeats)

while True:
    guess = int(input("Guess the number: "))
    all_tries += 1
    if guess in guesses:
        print("You already tried this number! Try a different one.")
        all_tries -= 1
        continue  # Don't count this as a new valid guess
    guesses.add(guess)
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        break

print("\nYour guesses:", sorted(guesses))
valid_guesses = len(guesses)
if all_tries > 0:
    success_ratio3 = ( 10 / valid_guesses ) * 10
    print(f"Success ratio: {success_ratio3:.1f}%")

```

---
### 10. Sum of Even Numbers in a List

**Task:**
Sum all even numbers in a list.

**Solution:**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for n in numbers:
    if n % 2 == 0:
        total += n
print("Sum of even numbers:", total)
```

---

### 11. Find the Largest Number

**Task:**
Get 5 numbers from the user and print the largest.

**Solution:**

```python
largest = None
for i in range(5):
    num = float(input("Enter a number: "))
    if (largest is None) or (num > largest):
        largest = num
print("The largest number is:", largest)
```

---

### 12. Simple ATM Menu

**Task:**
Simulate a simple ATM menu using loops and control flow.

**Solution:**

```python
balance = 1000
while True:
    print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited:", amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
```

---

### 13. AbraKadabra

**Task:**
Print numbers from 1 to 50, replace multiples of 3 with "Abra", 5 with "Kadabra", both with "AbraKadabra".

**Solution:**

```python
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("AbraKadabra")
    elif i % 3 == 0:
        print("Abra")
    elif i % 5 == 0:
        print("Kadabra")
    else:
        print(i)
```

---

### 14. Palindrome Checker (advanced)

**Task:**
Ask the user for a word. Print whether it is a palindrome.

**Solution:**

```python
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```
or

```python
word = input("Enter a word: ")
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
```


**Keep Coding!**
