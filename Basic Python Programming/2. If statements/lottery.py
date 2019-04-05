from random import randint

num = randint(1, 100)

answer = int(input("Enter your ticket number\n"))

if answer == num:
    print("You've won the lottery! 1000000 Rs is yours!")

else:
    print("Better luck next time")