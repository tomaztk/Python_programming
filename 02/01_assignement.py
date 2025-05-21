def print_menu():
    print("\nPlease select an option:")
    print("1. Show all numbers from 1 to 20 divisible by 3")
    print("2. Calculate the sum of all numbers from 1 to 100")
    print("3. Enter numbers until 0 is typed, then display their sum")
    print("4. Filter a list of names to show those starting with a vowel")
    print("5. Print a triangle pattern of stars with user-defined height")
    print("0. Exit")

while True:
    print_menu()
    choice = input("Enter your choice (0-5): ")

    if choice == "1":
        print("Numbers from 1 to 20 divisible by 3:")
        for i in range(1, 21):
            if i % 3 == 0:
                print(i, end=' ')
        print()
        
    elif choice == "2":
        total = 0
        for i in range(1, 101):
            total += i
        print("The sum of numbers from 1 to 100 is:", total)
        
    elif choice == "3":
        total = 0
        while True:
            num = int(input("Enter a number (0 to finish): "))
            if num == 0:
                break
            total += num
        print("The sum of entered numbers is:", total)
        
    elif choice == "4":
        names_input = input("Enter names separated by commas: ")
        names = [name.strip() for name in names_input.split(",")]
        print("Names starting with a vowel:")
        for name in names:
            if name and name[0].lower() in "aeiou":
                print(name)
                
    elif choice == "5":
        height = int(input("Enter the height of the triangle: "))
        print("Triangle pattern:")
        for i in range(1, height+1):
            print("*" * i)
            
    elif choice == "0":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please select from 0 to 5.")
