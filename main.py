import random

def guess_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        # Ask the user to guess the number
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        # Compare the user's guess to the generated number
        if user_guess < number_to_guess:
            print("Too low, try again!")
        elif user_guess > number_to_guess:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            print(f"It took you {attempts} attempts to guess the number.")
            break

# Run the game
guess_number()
