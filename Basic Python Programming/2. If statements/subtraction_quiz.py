from random import randint

num1 = randint(1, 100)
num2 = randint(1, 100)

if num1 < num2:
    temp = num1
    num1 = num2
    num2 = temp

answer = int(input("What is " + str(num1) + " - " + str(num2) + " ?\n"))

if answer == (num1 - num2):
    print("Right Answer!")

else:
    print("Wrong Answer!")
