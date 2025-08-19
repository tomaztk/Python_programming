
## **LESSON 09: Additional Python Function exercises (with solutions)**

---

#### **16. Temperature Converter**

Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit using the formula: `F = C * 9/5 + 32`.


---

#### **17. BMI Calculator**

Create a function `calculate_bmi(weight, height)` that returns the BMI value and a health message.

---

#### **18. Password Validator**

Write a function `is_valid_password(password)` that checks if the password is at least 8 characters long and includes both letters and numbers.


---

#### **19. Tip Calculator**

Define a function `calculate_tip(bill_amount, tip_percent=15)` to return total tip and final amount.


---

#### **20. Email Masker**

Write a function `mask_email(email)` that masks an email (e.g., j\*\*\*[e@gmail.com](mailto:e@gmail.com)).

---

#### **21. Age Calculator**

Write a function `calculate_age(birth_year, current_year)` that returns the person’s age.


---

#### **22. To-Do List Manager (Add Task)**

Create a function `add_task(todo_list, task)` that adds a task to a list.


---

#### **23. Loan Monthly Payment Calculator**

Write a function `calculate_monthly_payment(principal, rate, years)` using the formula for fixed monthly payments.



## **Solutions**


#### **16. Temperature Converter**

```python
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

print(celsius_to_fahrenheit(25)) 
```

#### **17. BMI Calculator**

```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi < 25:
        return bmi, "Normal"
    elif bmi < 30:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"

bmi_value, status = calculate_bmi(70, 1.75)
print(f"BMI: {bmi_value:.2f}, Status: {status}")
```


#### **18. Password Validator**


```python
def is_valid_password(password):
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return len(password) >= 8 and has_letter and has_digit

print(is_valid_password("abc12345")) 
```

---

#### **19. Tip Calculator**


```python
def calculate_tip(bill_amount, tip_percent=15):
    tip = bill_amount * (tip_percent / 100)
    return tip, bill_amount + tip

tip, total = calculate_tip(100)
print(f"Tip: {tip}, Total: {total}")
```

#### **20. Email Masker**


```python
def mask_email(email):
    name, domain = email.split('@')
    masked = name[0] + '***' + name[-1]
    return masked + '@' + domain

print(mask_email("johndoe@gmail.com")) 
```

#### **21. Age Calculator**


```python
def calculate_age(birth_year, current_year):
    return current_year - birth_year

print(calculate_age(1990, 2025)) 
```

---

#### **22. To-Do List Manager (Add Task)**


```python
def add_task(todo_list, task):
    todo_list.append(task)
    return todo_list

my_list = []
my_list = add_task(my_list, "Finish homework")
print(my_list)
```

#### **23. Loan Monthly Payment Calculator**



```python
def calculate_monthly_payment(principal, rate, years):
    monthly_rate = rate / 12 / 100
    months = years * 12
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    return payment

print(round(calculate_monthly_payment(10000, 5, 2), 2)) 
```