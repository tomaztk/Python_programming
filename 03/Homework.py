balance = 1000


while True:
    print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Balance:", balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited:", amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

