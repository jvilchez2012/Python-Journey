import random

number_to_guess = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10. You have 3 chances to guess it!")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")
