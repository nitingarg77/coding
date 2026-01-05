# Number guessung game
import random
low = 1
high = 100
number = random.randint(low, high)

guesses = 0
is_running = True
while is_running:
    guess = random.randint(low,high)
    guesses += 1

    if guess < number:
        print("Too low!")
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number {number} in {guesses} attempts.")
        is_running = False


print(f"Random number between {low} and {high}: {number}")