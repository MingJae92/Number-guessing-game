import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
tries = 1

while guess != number:
    if guess < number:
        print("Too low.")
    else:
        print("Too high.")
    guess = int(input("Guess again: "))
    tries += 1

print("Congratulations, you guessed the number in", tries, "tries!")
