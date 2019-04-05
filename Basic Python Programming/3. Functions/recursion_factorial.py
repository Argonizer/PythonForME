num = int(input("Enter a number\n"))

def factorial(num):
    fact = 1
    if(num > 1):
        fact = num * factorial(num-1)
    else:
        fact = 1
    return fact

print("The factorial for number", num, "is", factorial(num))