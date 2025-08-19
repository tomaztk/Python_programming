

## V. Combined Hands-On Assignment: Python Control Flow Mini-Project

### **Assignment Description**

Create a Python program that **assists a small club in managing some of their daily tasks.** Your program should be menu-driven (using loops and conditional statements) and let the user choose from several options. Each option demonstrates a concept from this lesson.

---

### **Menu Options and Requirements**

The program should display a menu like this:

```
Please select an option:
1. Show all numbers from 1 to 20 divisible by 3
2. Calculate the sum of all numbers from 1 to 100
3. Enter numbers until 0 is typed, then display their sum
4. Filter a list of names to show those starting with a vowel
5. Print a triangle pattern of stars with user-defined height
0. Exit
```

* The program must **keep running** (loop) until the user selects “0. Exit”.
* After each operation, the menu should reappear.

---

### **Detailed Breakdown of Each Option**

#### **Option 1: Show numbers from 1 to 20 divisible by 3**

* Use a `for` loop and conditional (`if`) to check divisibility.

#### **Option 2: Sum numbers from 1 to 100**

* Use a `for` loop and an accumulator variable.

#### **Option 3: Enter numbers until 0 is typed; display the sum**

* Use a `while` loop and conditional logic.
* Input validation is encouraged.

#### **Option 4: Print names starting with a vowel**

* Prompt the user to enter a comma-separated list of names.
* Use a `for` loop, `if`, and string methods.

#### **Option 5: Print triangle pattern**

* Prompt the user for the triangle’s height.
* Use nested `for` loops to print a left-aligned triangle of stars (`*`).

---

## **Sample Program Structure**

```python
def print_menu():
    print("\nPlease select an option:")
    print("1. Show all numbers from 1 to 20 divisible by 3")
    print("2. Calculate the sum of all numbers from 1 to 100")
    print("3. Enter numbers until 0 is typed, then display their sum")
    print("4. Filter a list of names to show those starting with a vowel")
    print("5. Print a triangle pattern of stars with user-defined height")
    print("0. Exit")

while True:
    print_menu()
    choice = input("Enter your choice (0-5): ")

    if choice == "1":
        print("Numbers from 1 to 20 divisible by 3:")
        for i in range(1, 21):
            if i % 3 == 0:
                print(i, end=' ')
        print()
        
    elif choice == "2":
        total = 0
        for i in range(1, 101):
            total += i
        print("The sum of numbers from 1 to 100 is:", total)
        
    elif choice == "3":
        total = 0
        while True:
            num = int(input("Enter a number (0 to finish): "))
            if num == 0:
                break
            total += num
        print("The sum of entered numbers is:", total)
        
    elif choice == "4":
        names_input = input("Enter names separated by commas: ")
        names = [name.strip() for name in names_input.split(",")]
        print("Names starting with a vowel:")
        for name in names:
            if name and name[0].lower() in "aeiou":
                print(name)
                
    elif choice == "5":
        height = int(input("Enter the height of the triangle: "))
        print("Triangle pattern:")
        for i in range(1, height+1):
            print("*" * i)
            
    elif choice == "0":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select from 0 to 5.")
```

---

## **Instructor Notes & Learning Objectives**

* This assignment reinforces **loops** (for, while), **conditionals** (if, elif, else), **input/output**, **operators**, **enumerate/string operations**, and **nested logic**.
* Encourages thinking about **program structure**, user interaction, and combining multiple skills.
* You can encourage students to use **comments** and experiment with error-handling (e.g., handling non-integer input).

---

## **Extension Ideas (for advanced students or extra credit):**

* Add input validation for all inputs.
* Allow repeating option 4 with different name lists until a blank line is entered.
* Enhance the triangle pattern to be centered or inverted.
* Add a summary at the end of each loop iteration showing which options have been run.


