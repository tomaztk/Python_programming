# 1: What is different between the two functions `fact` and `fact2`?
def fact(n):
    if n >= 0 and n <= 1:
        return(n)
    
    else:
        res = n*(fact(n-1))
        return res


def fact2(n):
    if n >= 0 and n <= 1:
        return 1
    return n*(fact(n-1))

print(fact(5))  
print(fact2(5))  


# 2. What is the output of the following code?
m, n, m, m  = [i for i in range(4)]
print(m + n)

# Wha is the output of the following code? And explain why.
# 2a: 4
# 2b: 3
# 2c: 2
# 2d: Error due to duplicate variable names


# 3.  What is the output of the following code? explain why.
a = [11, 22, 33, 44, 55]
print(a[2:])

# 3a: [22, 33, 44, 55]
# 3b: []
# 3c: [33, 44, 55]
# 3d: [44, 55]


# 4. What is the output of the following code? explain why.

for i in range(3):
    for j in range(3):
        if j == 1:
            break
print(f"{i}-{j}")

# 4a: 2-1
# 4b: 2-2
# 4c: 0-1
      1-1
      2-1
# 4d: Error due to undefined variable j


# 5. What is the output of the following code? explain why.

def func():
    print(x)
    x = 5

x = 10
func()

# 5a: 5
# 5b: 10
# 5c: Error due to referencing before assignment
# 5d: Error due to local variable x being referenced before assignment


# 6. What is the output of the following code? explain why.
b = [1, 2, 3, 4, 5]
print(b[1:4:2])

# 6a: [2, 4]
# 6b: [1, 3, 5]
# 6c: [2, 3, 4, 5]
# 6d: [2, 3]

# 7. What is the output of the following code? explain why.

random_list = [0, 1, 2, 3, 4]
random_list[1:4] = [7, 8, 9, 10, 11, 12]
print(random_list)

# 7a: [0, 7, 8, 9, 10, 11, 12, 4]
# 7b: [0, 1, 2, 3, 4]
# 7c: [0, 7, 8, 9, 10, 11, 12]
# 7d: Error due to undefined undefined position in random_lst


# 8. What is the output of the following code? explain why.
# *Hint: This question involves boolean operations and operator precedence. 
#               Operator precedence: 1) not, 2) and, 3) or

x = False
y = True
z = False
print(not x and y or z and not y)

# 8a: True
# 8b: False
# 8c: Error due to invalid boolean operation
# 8d: Error due to undefined variable z


#9. What is the output of the following code? explain why.

n = 10

if n > 5:
    print("Hi")
if n < 15:
    print("There")
else:
    print("Bye")

# 9a: Hi
# 9b: There
# 9c: Hi
#     There
# 9d: Bye


# 10. What is the output of the following code? explain why.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[1:4:-1])

#10a: []
#10b: [2, 3, 4]
#10c: [3, 2, 1]
#10d: Error due to invalid slice step

# 11. What is the output of the following code? explain why.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[4:1:-1])

#11a: [5, 4, 3]
#11b: [4, 3, 2]
#11c: [5, 4, 3, 2]
#11d: Error due to invalid slice step

# 12. What is the output of the following code? explain why.

n = 2
while n < 20:
    print(n)
    n *= 2
    if n > 16: 
        break

# 12a: 2, 4, 8, 16
# 12b: 2, 4, 8
# 12c: 2, 4, 8, 16, 32
# 12d: Error due to infinite loop


# 13. What is the output of the following code? explain why.

for i in range(3):
    for j in range(2):
        if i == j:
            print(i , j)

# 13a: 0, 1
# 13b: 0, 2, 6
# 13c: 0, 1, 2
# 13d: Error due to undefined variable j

# 14. What is the output of the following code? explain why.

for i in range(1, 3):
    for j in range(2):
        print(i + j)

# 14a: 1, 2, 2, 3
# 14b: 1, 2, 3, 4
# 14c: 1, 2, 3
# 14d: Error due to invalid range


