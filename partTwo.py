import random

print("***Number Guessing Game***")

number = int(input("Guess the number: "))
secret_number = random.randint(1,10)

if number > secret_number:
    print("Too high")
elif number < secret_number:
    print("Too low")
else:
    print("You guessed the number correctly")
