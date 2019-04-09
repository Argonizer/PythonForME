from random import randint
count = 0
def add_quiz(num1, num2):
    answer = int(input("What is " + str(num1) + " + " + str(num2) + "? : "))
    if answer == num1 + num2:
        print("You guessed it right! Good Job!")
        return 1
    else:
        print(str(num1) + " + " + str(num2) + "should be " + str(num1 + num2) + "! Wrong Answer")
        return 0

def sub_quiz(num1, num2):
    answer = int(input("What is " + str(num1) + " - " + str(num2) + "? : "))
    if answer == num1 - num2:
        print("You guessed it right! Good Job!")
        return 1
    else:
        print(str(num1) + " - " + str(num2) + "should be " + str(num1 + num2) + "! Wrong Answer")
        return 0

def mul_quiz(num1, num2):
    answer = int(input("What is" + str(num1) + "*" + str(num2) + "? : "))
    if answer == num1 * num2:
        print("You guessed it right! Good Job!")
        return 1
    else:
        print(str(num1) + " * " + str(num2) + " should be " + str(num1 + num2) + "! Wrong Answer")
        return 0

def div_quiz(num1, num2):
    answer = int(input("What is " + str(num1) + " / " + str(num2) + "? : "))
    if answer == num1 / num2:
        print("You guessed it right! Good Job!")
        return 1
    else:
        print(str(num1) + " / " + str(num2) + " should be " + str(num1 / num2) + "! Wrong Answer")
        return 0

for i in range(10):
    num1 = randint(0,100)
    num2 = randint(0,100)
    op = ["+", "-", "/", "*"]
    sign = op[randint(0,3)]
    if sign == "+":
        count = count + add_quiz(num1, num2)
    elif sign == "-":
        count += sub_quiz(num1, num2)
    elif sign == "*":
        num1 = num1//10
        num2 = num2 // 10
        count += mul_quiz(num1, num2)
    elif sign == "/":
        num2 = num2 // 10
        count += div_quiz(num1, num2)




print("You got", count, "answers right out of", 10)
