import random

print("Welcome to the Number Guessing Game!")
print("Can you guess the secret number between 1 and 100?")

secret_number=random.randint(1, 100)

attempts=0
max_attempts=5

while attempts < max_attempts:
    try:
        n=int(input("\nEnter your guess: "))
        attempts+=1
        if n < secret_number:
            print("Too low! Try again.")
        elif n > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == max_attempts:
        print(f"\nSorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

        