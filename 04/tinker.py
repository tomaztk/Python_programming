largest_number = None

for i in range(5):
    num = int(input("Please input a number: "))
    if (largest_number is None) or (num > largest_number):
        largest_number=num
        print(num)
        print(largest_number)
print("The largest number is: ", largest_number)