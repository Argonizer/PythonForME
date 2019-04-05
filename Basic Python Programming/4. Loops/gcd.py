print("Enter two numbers whose greatest common divisor is to be found")

num1 = int(input())
num2 = int(input())

gcd = 1
k = 2

while(k <= min(num1, num2)):
    if num1 % k == 0 and num2 % k == 0:
        gcd == k

    k+=1

print("The GCD of the two numbers is", gcd)
