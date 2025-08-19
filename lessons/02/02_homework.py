print("Welcome to the Fibonacci Sequence Generator!\n")

while True:
    try:
        n = int(input("How many terms would you like to generate? (Enter a positive integer): "))
        if n <= 0:
            print("Please enter a positive integer greater than zero.\n")
            continue
    except ValueError:
        print("Invalid input. Please enter a positive integer.\n")
        continue

    # Generate Fibonacci sequence
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    # Print the full sequence
    print("\nFibonacci sequence:")
    for num in fib_sequence:
        print(num, end=' ')
    print()

    # Find and print even Fibonacci numbers
    print("\nEven Fibonacci numbers:")
    has_even = False
    for num in fib_sequence:
        if num % 2 == 0:
            print(num, end=' ')
            has_even = True
    if not has_even:
        print("None in this range.", end='')
    print()

    # Print the sum of the sequence
    fib_sum = 0
    for num in fib_sequence:
        fib_sum += num
    print(f"\nSum of all Fibonacci numbers: {fib_sum}\n")

    # Bonus
    again = input("Would you like to generate another sequence? (y/n): ").strip().lower()
    if again != 'y':
        print("Thank you for using the Fibonacci Sequence Generator!")
        break
