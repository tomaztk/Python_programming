## **VI. Hands-on Coding: Breaking Down Problems with Functions **

### **Goal**

* Practice splitting a complex problem into smaller, manageable functions.
* Strengthen skills in writing, calling, testing, and debugging functions.

---

### **A. Example Problem 1: User Data Validation and Greeting**

**Scenario:**
Write a program that asks the user for their name and age, validates the input, and then greets the user if the data is valid.

**Step 1: Break Into Functions**

1. **get\_user\_input** – Get input from the user.
2. **validate\_name** – Ensure the name isn’t empty and contains only letters.
3. **validate\_age** – Ensure age is a positive integer.
4. **greet\_user** – Print a greeting message.

**Step 2: Code Structure & Examples**

```python
def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

def validate_name(name):
    return name.isalpha() and len(name) > 0

def validate_age(age):
    return age.isdigit() and int(age) > 0

def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

def main():
    name, age = get_user_input()
    if not validate_name(name):
        print("Invalid name. Please use only letters.")
        return
    if not validate_age(age):
        print("Invalid age. Please enter a positive number.")
        return
    greet_user(name, age)

main()
```

**Explanation:**

* Each function does one job—making the code clear and reusable.
* `main()` acts as the program’s “controller,” coordinating the logic.

---

### **B. Example Problem 2: Simple Text Processing**

**Scenario:**
Given a sentence, count the number of words and the number of vowels.

**Step 1: Break Into Functions**

1. **get\_sentence** – Get the sentence from the user.
2. **count\_words** – Count words in the sentence.
3. **count\_vowels** – Count vowels in the sentence.
4. **display\_results** – Print the results.

**Step 2: Code Structure & Examples**

```python
def get_sentence():
    return input("Enter a sentence: ")

def count_words(sentence):
    words = sentence.split()
    return len(words)

def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char in vowels)

def display_results(word_count, vowel_count):
    print(f"Words: {word_count}")
    print(f"Vowels: {vowel_count}")

def main():
    sentence = get_sentence()
    word_count = count_words(sentence)
    vowel_count = count_vowels(sentence)
    display_results(word_count, vowel_count)

main()
```

**Explanation:**

* The problem is split into logical parts, each handled by a function.
* This structure is easier to test, debug, and modify.

---

### **C. Tips for Students**

* **Plan before you code:** Write down the steps of your solution, then turn each step into a function.
* **Test as you go:** Test each function separately before integrating them.
* **Debugging:** If your program doesn’t work, test each function individually to find where the error is.
* **Reuse:** Functions can be reused in other programs or other parts of your code.

---

### **D. Group or Individual Work Structure**

* **Step 1:** Choose a problem (instructor may assign or let students pick).
* **Step 2:** Break the problem into functions—write down or discuss function names and their jobs.
* **Step 3:** Write each function, testing as you go.
* **Step 4:** Integrate all functions into a `main()` function and run the whole program.
* **Step 5:** Debug any issues together.

---

### **E. Sample Problems to Assign**

* A calculator that can add, subtract, multiply, and divide (as in the homework!).
* Email validator: Ask for an email, validate its format, and print a result.
* Simple password checker: Get password, check length and characters, print result.
* Word counter: Input a paragraph, count sentences, words, and characters.

---

### **Key Understanding **

* **Divide and conquer:** Complex problems become much easier when split into smaller pieces.
* **Functions are building blocks:** Each function should have one clear job.
* **Testing and debugging:** With small functions, it’s easier to find and fix mistakes.

 
