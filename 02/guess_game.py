print("\n“")
print("Welcome to the Guessing Game!\n")
print("Try to guess the secret number between 1 and 10.")


secret = 7
guesses = set()  # Stores unique valid guesses
all_tries = 0    # Counts every input (including repeats)

while True:
    guess = int(input("Guess the number: "))
    all_tries += 1
    if guess in guesses:
        print("You already tried this number! Try a different one.")
        all_tries -= 1
        continue  # Don't count this as a new valid guess
    guesses.add(guess)
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        break

print("\nYour guesses:", sorted(guesses))
valid_guesses = len(guesses)
if all_tries > 0:
    success_ratio3 = ( 10 / valid_guesses ) * 10
    print(f"Success ratio: {success_ratio3:.1f}%")




largest = None
for i in range(5):
    num = float(input("Enter a number: "))
    if (largest is None) or (num > largest):
        largest = num
print("The largest number is:", largest)