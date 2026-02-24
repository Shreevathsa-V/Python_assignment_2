# Q16 - Number Guessing Game
# The program generates a random number and the user has limited attempts.

import random

while True:
    secret_number = random.randint(1, 100)
    attempts_left = 7

    print("Guess the number between 1 and 100")

    while attempts_left > 0:
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print("Correct! You guessed it.")
                break
            elif guess > secret_number:
                print("Too high.")
            else:
                print("Too low.")

            attempts_left -= 1
            print("Attempts remaining:", attempts_left)

        except ValueError:
            print("Enter a valid number.")

    if attempts_left == 0:
        print("You lost. The correct number was", secret_number)

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break