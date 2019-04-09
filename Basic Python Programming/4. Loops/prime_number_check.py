num = int(input("Enter a number\n"))
count = 0
for i in range(1,num):
    if num % i == 0:
        count += 1

if count == 2:
    print("It is a prime number")
else:
    print("It's not a prime number")
