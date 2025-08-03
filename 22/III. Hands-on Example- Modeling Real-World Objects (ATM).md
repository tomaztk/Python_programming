## **III. Hands-on Example: My First ATM Script :)**

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

atm1 = ATM("Copova ulica, Ljubljana", "NLB")
atm1.power_on()
atm1.power_off()
```

**Output:**

```
ATM at Copova ulica, Ljubljana (NLB) is now ON.
ATM at Copova ulica, Ljubljana (NLB) is now OFF.
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


account1 = BankAccount("Tomaz K.", 500)
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
cclass Client:
    def __init__(self, name, account):
        self.name = name
        self.account = account  
    
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


TK_account = BankAccount("SI56 0201 00000 00001230", 1000)

client1 = Client("Tomaz Kastrun", TK_account)


atm1 = ATM("NLB Copova, Ljubljana", "NLB Banka")
atm1.power_on()


client1.use_atm(atm1, "withdraw", 200)
client1.use_atm(atm1, "deposit", 500)
client1.use_atm(atm1, "balance")

atm1.power_off()
```

**Output:**

```
ATM at NLB Copova, Ljubljana (NLB Banka) is now ON.
Tomaz Kastrun is using the ATM at NLB Copova, Ljubljana...
Withdrew $200. New balance: $800
Tomaz Kastrun is using the ATM at NLB Copova, Ljubljana...
Deposited $500. New balance: $1300
Tomaz Kastrun is using the ATM at NLB Copova, Ljubljana...
Tomaz Kastrun's current balance: $1300
ATM at NLB Copova, Ljubljana (NLB Banka) is now OFF.
```

---

## **4. Summary Table (Aligned to Bank Story)**

| Concept         | Meaning                 | Example from Bank Story                         |
| --------------- | ----------------------- | ----------------------------------------------- |
| **Class**       | Blueprint for objects   | `class BankAccount:`                            |
| **Object**      | Instance of a class     | `atm1 = ATM("NLB Copova, LJubljana", "NLB")`        |
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


