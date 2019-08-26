a = int(input("Enter first number"))
b = int(input("Enter second number"))
b = a + b 
a = b - a
b = b - a
print("The swapped numbers are a = ",a," and b = ", b)

#This program swaps two numbers without using a temporary variable
#This can also be done using / and *
#b = a * b
#a = b / a
#b = b / a