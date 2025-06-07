



### Dictionary of assignments

#sample
assignments = {
    "assignment1": {
        "title": "Assignment 1: Introduction to Python",
        "description": "This assignment covers the basics of Python programming, including variables, data types, and control structures.",
        "due_date": "2023-10-15",
        "points": 100,

        "resources": [
            {
                "title": "Python Official Documentation",
                "url": "https://docs.python.org/3/"
            },
            {

                "title": "W3Schools Python Tutorial",
                "url": "https://www.w3schools.com/python/"
            },
            {
                "title": "Codecademy Python Course",
                "url": "https://www.codecademy.com/learn/learn-python-3"
            }
        ],      
    }
}

capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi"
}

# Get value for a specific key

print(capitals.get("USA"))  # Returns "Washington, D.C."

# print(dir(capitals))  # Lists all attributes and methods of the dictionary
# print(help(capitals))  # Displays help information for the dictionary

print(capitals.get("Slovenia", "Not Found"))  # Returns "Not Found" if key doesn't exist



keys = capitals.keys()  # Returns a view object of the dictionary's keys
print(keys)  # Output: dict_keys(['USA', 'Canada', 'Mexico', 'France', 'Germany', 'Japan', 'China', 'India'])


items = capitals.items()  # Returns a view object of the dictionary's key-value pairs
print(items)  # Output: dict_items([('USA', 'Washington, D.C.'), ('Canada', 'Ottawa'), ...])

for key, value in capitals.items():
    print(f"The capital of {key} is {value}")



print( {x for x in range(1,11,1) if x % 2 == 0} )   


from functools import reduce

def multiply_elements(lst):
    return reduce(lambda x, y: x * y, [i for i in lst])


#print(multiply_elements([1, 2, 3, 4, 5])) 




product = [0,1]
[(lambda x: product.append(product[-1] * x))(x) for x in [2, 3, 4, 5]]
print(product[-1])




# (lambda x,i: x = x*i)

# (lambda x, i: x = x * i for i in (1,2,3,4,5))

result = [1]
[(lambda i: result.append(result[-1] * i))(i) for i in (1, 3, 4, 5)]
print(result[-1])  