## 6. Practical Examples

### Pass

Begin with pass to create an class that we can instantiate.

```python
some_number = 2
some_text = "Anna"

type(some_number)
type(some_text)
```


We are assigning attributres to our instance of this class.

```python
class Item:
	pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5


print(type(item1)) # item
print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) #int
```

We can create methods (we used to call them functions, but in classes they are called methods) and run against instances.


```python

class Item:
	def calculate_total_price_test(self):
		pass
	
	def calculate_total_price(self, x, y):
		return x * y
	
item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

```

_self_ passes this argument on to method, therefore Python uses this word to push propagate this attribute. With every new method, we need to have (!) at least one parameter. "self" is like a common convention


This class needs attributes, not that we need to instance these attributes  every single time. Therefore we create ____init____ constructor (also known as magic method)


"init" is automatically created when object is instantiated.

```python
class Item:
	def __init__(self):
		print("See, This is created")
		
item1 = Item()
item2 = Item()
```

So we want to get rid of "hard-coded" attributes for each instance. We will use init constructor

```python

class Item:
	def __init__(self, name):
		print(f"An, Instance is created {name}")

item1 = Item("Phone")
#item2.name = "Prhone"
item2 = Item("LAptop")
#item2.name = "Laptop"

```

With dynamic attribute assignement using magic method ____init____ we use self to create this attribute within the method, so that we do not need to instance it every time.

```python
class Item:
	def __init__(self, name):
		self.name = name

item1 = Item("Phone")
item2 = Item("Laptop")
print(item1.name)
print(item2.name)

```

And let's do it for all the attributes. We call also assign a default value to the parameters in ____init____ (e.g.: quantity=0)

```python

class Item:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity
		
		
	def calculate_total_price(self, x, y):
		return x * y

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

```

We can also change now the "calculate_total_price" method.

```python

class Item:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity
		
		
	def calculate_total_price(self):
		return self.price * self.quantity



item3 = Item("lala",10,23)
print(item3.name)
print(item3.calculate_total_price())

```

We need to validate the data types we type in!

```python
class Item:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity
		
		
	def calculate_total_price(self):
		return self.price * self.quantity



item1 = Item("Phone","100",1) #making strings instead of integers
item2 = Item("Keyboard","10",5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

```
So we change it to and enforce also the validations using "assert"


```python
class Item:
	def __init__(self, name: str, price: float, quantity: int):
		assert price >= 0, f"Price {price} is not negative"
		assert quantity >=0, f"Quantity must be positive or 0"
		self.name = name
		self.price = price
		self.quantity = quantity
		
		
	def calculate_total_price(self):
		return self.price * self.quantity



item1 = Item("Phone",100,1) 
item2 = Item("Keyboard",10,5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

```

Accessing information from instance level and then on class level. Item1 and Item2 are instances of the class. and pay_rate is on class level!

```python

class Item:
	pay_rate = 0.8
	def __init__(self, name: str, price: float, quantity: int):
		assert price >= 0, f"Price {price} is not negative"
		assert quantity >=0, f"Quantity must be positive or 0"
		self.name = name
		self.price = price
		self.quantity = quantity
		
		
	def calculate_total_price(self):
		return self.price * self.quantity



item1 = Item("Phone",100,1) 
item2 = Item("Keyboard",10,5)

print(Item.pay_rate)
print(item1.pay_rate)
```

Find all the attributes that are available on instance and class level

```python
class Item:
	pay_rate = 0.8
	def __init__(self, name: str, price: float, quantity: int):
		assert price >= 0, f"Price {price} is not negative"
		assert quantity >=0, f"Quantity must be positive or 0"
		self.name = name
		self.price = price
		self.quantity = quantity
		
		
	def calculate_total_price(self):
		return self.price * self.quantity

item1 = Item("Phone",100,1) 

print(Item.__dict__)
print(item1.__dict__)
		
```
And finally, applying the discount (20%) using the pay_rate.

```python
class Item:
	pay_rate = 0.8
	def __init__(self, name: str, price: float, quantity: int):
		assert price >= 0, f"Price {price} is not negative"
		assert quantity >=0, f"Quantity must be positive or 0"
		self.name = name
		self.price = price
		self.quantity = quantity
		
		
	def calculate_total_price(self):
		return self.price * self.quantity
		
	def apply_discount(self):
		self.price = self.price * self.pay_rate #Item.pay_rate or self.pay_rate
		
item1 = Item("Phone",100,1) 
item1.apply_discount()
print(item1.price)


item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount() #change self.pay_rate to Item.pay_rate to change the behaviour
print(item2.price)

```

Store all instances in object:

```python

class Item:
	all = []
	pay_rate = 0.8
	def __init__(self, name: str, price: float, quantity: int):
		assert price >= 0, f"Price {price} is not negative"
		assert quantity >=0, f"Quantity must be positive or 0"
		self.name = name
		self.price = price
		self.quantity = quantity
		
		Item.all.append(self)


item1 = Item("apple",10,2)
item2 = Item("pear",70,4)
item3 = Item("egg",60,1)
item4 = Item("milk",40,4)

print(Item.all)

for inst in Item.all:
    print(inst.name)
```


we can use another magic function ____repr____.

```python
class Item:
	all = []
	pay_rate = 0.8
	def __init__(self, name: str, price: float, quantity: int):
		assert price >= 0, f"Price {price} is not negative"
		assert quantity >=0, f"Quantity must be positive or 0"
		self.name = name
		self.price = price
		self.quantity = quantity
		
		Item.all.append(self)
		
	def __repr__(self):
		return f"Item('{self.anem}, {self.price}')"


item1 = Item("apple",10,2)
item2 = Item("pear",70,4)
item3 = Item("egg",60,1)
item4 = Item("milk",40,4)

print(Item.all)

```

Example of classmethod

```python

@classmethod
def instantiate_from_csv(cls):
	with open ('items.csv', 'r') as f:
		reader = csv. DictReader (f)
		items = list(reader)

	for item in items:
		Item(
			name=item get ( 'name'),
			price=float(item get('price')),
			quantity=int(item.get( 'quantity')),
		)


Item. instantiate_from_csv)
print(Item.all)

```

example of static method

```python
@classmethod
def instantiate_from_csv(cls):
	with open ('items.csv', 'r') as f:
		reader = csv. DictReader (f)
		items = list(reader)

	for item in items:
		Item(
			name=item get ( 'name'),
			price=float(item get('price')),
			quantity=int(item.get( 'quantity')),
		)

@statiscmethod
def is_integer(num):
	if isinstance(num, float):
		return num.is_integer()
	elif isinstance(num, int):
		return True
	else:
		return False

print(Item.is_integer(7))   #7.0 = True; 7.5 = False; 7 = True 

```

Difference between static and class method:

- use static - this should do something that has a relationship with the class but nothing to do that must be unique to the instance
- use class - this should also do something that has a relationshop with the class, but usually used to manipulate different structures of data to instantiate objects, like reading CSV file


