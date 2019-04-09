num = int(input("Enter nth term of Fibonacci series\n"))

def fibonacci(num):
 #fib = 1
    if(num == 2):
        fib = 1
    elif num == 1:
        fib = 0
    else:
        fib = fibonacci(num - 1) + fibonacci(num - 2)
    return fib

print("The", num, "th term of fibonacci series is", fibonacci(num))


0, 1, 1, 2, 3, 5, 8, 13, 21
