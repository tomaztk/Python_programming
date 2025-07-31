## **III. Hands-on Example: Modeling Real-World Objects (ATM)**

---

### **Example 1: ATM Machine**

We start with a **simple ATM class** that can turn on and off.
Later, we’ll connect it to a **BankAccount**.

```python
class ATM:
    def __init__(self, location, bank_name):
        self.location = location
        self.bank_name = bank_name
    
    def power_on(self):
        print(f"ATM at {self.location} ({self.bank_name}) is now ON.")
    
    def power_off(self):
        print(f"ATM at {self.location} ({self.bank_name}) is now OFF.")

# Create an ATM
atm1 = ATM("Main Street", "City Bank")
atm1.power_on()
atm1.power_off()
```

**Output:**

```
ATM at Main Street (City Bank) is now ON.
ATM at Main Street (City Bank) is now OFF.
```

---

### **Example 2: Bank Account**

A **BankAccount** class stores account details and allows deposits/withdrawals.

```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

# Create account and perform transactions
account1 = BankAccount("John Doe", 500)
account1.deposit(200)
account1.withdraw(100)
account1.withdraw(700)
```

**Output:**

```
Deposited $200. New balance: $700
Withdrew $100. New balance: $600
Insufficient funds!
```

---

### **Example 3: Bank Client**

A **Client** has a **BankAccount** and can interact with an ATM.

```python
class Client:
    def __init__(self, name, account):
        self.name = name
        self.account = account  # BankAccount object
    
    def check_balance(self):
        print(f"{self.name}'s current balance: ${self.account.balance}")
    
    def use_atm(self, atm, action, amount=0):
        print(f"{self.name} is using the ATM at {atm.location}...")
        
        if action == "withdraw":
            self.account.withdraw(amount)
        elif action == "deposit":
            self.account.deposit(amount)
        elif action == "balance":
            self.check_balance()
        else:
            print("Invalid ATM action.")

# Create bank account
john_account = BankAccount("John Doe", 1000)

# Create client
client1 = Client("John Doe", john_account)

# Create ATM
atm1 = ATM("Main Street", "City Bank")
atm1.power_on()

# Client uses ATM
client1.use_atm(atm1, "withdraw", 200)
client1.use_atm(atm1, "deposit", 500)
client1.use_atm(atm1, "balance")

atm1.power_off()
```

**Output:**

```
ATM at Main Street (City Bank) is now ON.
John Doe is using the ATM at Main Street...
Withdrew $200. New balance: $800
John Doe is using the ATM at Main Street...
Deposited $500. New balance: $1300
John Doe's current balance: $1300
ATM at Main Street (City Bank) is now OFF.
```

---

## **4. Summary Table (Aligned to Bank Story)**

| Concept         | Meaning                 | Example from Bank Story                         |
| --------------- | ----------------------- | ----------------------------------------------- |
| **Class**       | Blueprint for objects   | `class BankAccount:`                            |
| **Object**      | Instance of a class     | `atm1 = ATM("Main Street", "City Bank")`        |
| **Attribute**   | Variable inside a class | `self.balance`                                  |
| **Method**      | Function inside a class | `def deposit(self, amount)`                     |
| **Constructor** | Initializes an object   | `def __init__(self, account_holder, balance=0)` |
| **`*args`**     | Many positional args    | `def __init__(self, *transactions)`             |
| **`**kwargs`**  | Many keyword args       | `def __init__(self, **account_info)`            |

---

Some Ideas **extend this** even more:

* Multiple clients
* Multiple accounts
* Multiple ATMs
* `*args` & `**kwargs` usage
* Error handling for withdrawals
* Logging transactions to a file


