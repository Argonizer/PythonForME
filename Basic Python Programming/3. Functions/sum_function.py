
#This is a program to find out CI

P = float(input("Enter Principal"))
R = float(input("Enter Rate"))
n = float(input("Enter Time"))

A = P * (1 + (R/100))**n

print("The amount is " + str(A))

