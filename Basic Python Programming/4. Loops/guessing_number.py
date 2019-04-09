from random import randint

number = randint(0,100)
guess = 10000

while guess != number:
    number = randint(0,100)
    guess = int(input("Guess the number : "))
    if guess > number:
        print("You've guessed too high!")
    elif guess < number:
        print("You've guessed too low!")
    else:
        print("You guessed it Right!")
