### IV. Introduction to Sets

#### **1. Creating Sets**

A **set** is an unordered collection of unique, immutable elements.

**Using curly braces:**  

```python
nums = {1, 2, 3, 4}
```
**Using the set() constructor (especially for lists/strings):**  

```python
nums2 = set([3, 4, 5, 6])
print(nums, nums2)  # Output: {1, 2, 3, 4} {3, 4, 5, 6}
```

**Important:**  

Empty set: Use `set()`, not `{}` (which makes an empty dictionary).

```python
empty_set = set()
```

#### **2. Adding and Removing Elements**

**Adding an element:**  

```python
nums.add(5)
print(nums)  # Output: {1, 2, 3, 4, 5}
```
 If the element already exists, nothing changes.

**Removing an element:**  

```python
nums.remove(1)   # Removes 1, raises error if 1 not found
print(nums)
nums.discard(10) # Removes 10 if present, does nothing if not (no error)
```

**Remove and return an arbitrary element:**  

```python
popped = nums.pop()
print("Removed:", popped)
```

**Clear all elements:**  

```python
nums.clear()
print(nums)  # Output: set()
```

#### **3. Set Operations**

Sets support powerful operations for comparing and combining groups of items:

**Union:** Elements in either set

```python
nums = {2, 3, 4, 5}
nums2 = {3, 4, 5, 6}
union = nums | nums2
print(union)                   # Output: {2, 3, 4, 5, 6}
# OR
print(nums.union(nums2))
```

**Intersection:** Elements in both sets

```python
intersection = nums & nums2
print(intersection)            # Output: {3, 4, 5}
# OR
print(nums.intersection(nums2))
```

**Difference:** Elements in the first set but not the second

```python
difference = nums - nums2
print(difference)              # Output: {2}
# OR
print(nums.difference(nums2))
```

**Symmetric Difference:** Elements in either set, but not both

```python
sym_diff = nums ^ nums2
print(sym_diff)                # Output: {2, 6}
# OR
print(nums.symmetric_difference(nums2))
```

**Membership test:**  

```python
print(3 in nums)    # True if 3 is in nums
print(10 in nums)   # False
```

#### **4. Example: Removing Duplicates from a List**

Sets make it easy to remove duplicates:

```python
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print(unique_items)  # Output: {1, 2, 3, 4, 5}
```
- If you need the result as a list again:
  ```python
  unique_list = list(unique_items)
  print(unique_list)
  ```

#### **5. Useful Set Methods**

| Method                        | Description                              | Example                           |
|-------------------------------|------------------------------------------|-----------------------------------|
| `add(element)`                | Add an element to the set                | `nums.add(7)`                     |
| `remove(element)`             | Remove element (error if not present)    | `nums.remove(3)`                  |
| `discard(element)`            | Remove element (no error if not present) | `nums.discard(10)`                |
| `pop()`                       | Remove and return an arbitrary element   | `nums.pop()`                      |
| `clear()`                     | Remove all elements                      | `nums.clear()`                    |
| `union(other_set)`            | All unique elements from both sets       | `a.union(b)`                      |
| `intersection(other_set)`     | Only elements in both sets               | `a.intersection(b)`               |
| `difference(other_set)`       | Elements only in the first set           | `a.difference(b)`                 |
| `symmetric_difference(other)` | Elements in either, but not both         | `a.symmetric_difference(b)`       |
| `issubset(other)`             | True if set is subset of another         | `a.issubset(b)`                   |
| `issuperset(other)`           | True if set is superset of another       | `a.issuperset(b)`                 |
| `copy()`                      | Returns a shallow copy of the set        | `a.copy()`                        |

#### **6. Real World Examples of Using Sets**

**Removing Duplicates:**  
 
 Get unique email addresses from a mailing list.
 
```python
  emails = ['a@mail.com', 'b@mail.com', 'a@mail.com']
  unique_emails = set(emails)
  print(unique_emails)
```

**Membership Test:**  
Check if a user has admin privileges.

```python
admins = {'alice', 'bob'}
username = 'charlie'
if username in admins:
  print('Admin')
else:
  print('Not admin')
```

**Finding Common/Unique Items:**  

Find students in both math and science clubs.

```python
math_club = {'Tom', 'Jane', 'Sara'}
science_club = {'Sara', 'Alex', 'Jane'}
both_clubs = math_club & science_club
print(both_clubs)  # Output: {'Jane', 'Sara'}
```

