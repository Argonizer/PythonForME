def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        return True
    
num = int(input("Enter a number\n"))

if perfect(num):
    print("It is a perfect number")
else:
    print("It's not a perfect number")

