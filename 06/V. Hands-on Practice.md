## V. Hands-on Practice

Below are three guided exercises to help reinforce your understanding of dictionaries and sets.

---

### **Exercise 1: Store and Retrieve Data Using a Dictionary**

#### **Goal:**

Practice creating a dictionary, storing user input, and retrieving values.

**Instructions:**

1. Create an empty dictionary called `person`.
2. Ask the user to enter their name and age.
3. Store these values in the dictionary using appropriate keys (`'name'`, `'age'`).
4. Print a personalized greeting using data from the dictionary.

**Sample Solution:**

```python
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
print(f"Hello {person['name']}, you are {person['age']} years old.")
```

**Try this:**

* Add a new key for `'city'` and ask the user for their city.
* Print a message that uses all three fields.

---

### **Exercise 2: Use a Set to Check for Duplicates**

#### **Goal:**

Learn how sets can help check for duplicates in a collection.

**Instructions:**

1. Prompt the user to enter numbers separated by spaces.
2. Convert the input string into a list of integers.
3. Convert the list to a set.
4. If the length of the set is less than the list, there were duplicates.

**Sample Solution:**

```python
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
if len(nums) != len(set(nums)):
    print("There are duplicates!")
else:
    print("All numbers are unique.")
```

**Try this:**

* Print the duplicate numbers (hint: use a dictionary or a set to count).
* Let the user enter words instead of numbers and check for duplicate words.

---

### **Exercise 3: Iterating Over a Dictionary**

#### **Goal:**

Practice iterating through a dictionary and printing key-value pairs.

**Instructions:**

1. Use a dictionary of names and grades.
2. Loop through each key-value pair.
3. Print the name and corresponding grade in a formatted string.

**Sample Solution:**

```python
grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
for name, grade in grades.items():
    print(f"{name}: {grade}")
```

**Try this:**

* Calculate and print the average grade.
* Find and print the name(s) of the student(s) with the highest grade.

---

## VI. Homework

### **Build a Contact Book Using Dictionaries**

#### **Goal:**

Create an interactive program that allows users to store, update, and search for contact information using dictionaries.

---

#### **Detailed Requirements:**

* Store each contact’s name as the key.
* The value for each contact is another dictionary with at least `'phone'` and `'email'`.
* The program should allow the user to:

  * **Add** a new contact.
  * **Update** an existing contact.
  * **Search** for a contact by name.
  * **Exit** the program.
* Display appropriate messages for each action (e.g., "Contact added", "Contact not found").
* Use a loop to keep the program running until the user chooses to exit.

---

#### **Example Starter Code:**

```python
contacts = {}

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact added.")
    elif choice == '2':
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contacts[name] = {'phone': phone, 'email': email}
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")
    elif choice == '4':
        break
    else:
        print("Invalid option.")
```

---

### **Tips for Success:**

* Use dictionaries for flexible, fast lookups.
* Remember to check if a contact exists before updating or searching.
* Think about user experience—give clear instructions and feedback.
* Try breaking your code into functions (optional, for more advanced students).
