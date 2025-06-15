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


# What is the output of the following code?
m, n, m, m  = [i for i in range(4)]
print(m + n)

# Wha is the output of the following code?
# a: 4
# b: 3
# c: 2
# d: Error due to duplicate variable names