
#This is a program to find out CI or SI

P = float(input("Enter Principal"))
R = float(input("Enter Rate"))
n = float(input("Enter Time"))
choice = input("CI or SI?")

def CI(P, R, n):
    A = P * (1 + (R/100))**n
    return A

def SI(P, R, n):
    A = P + P * R * n / 100
    return A

if choice == "SI":
    print("The amount is " + str(SI(P, R, n)))

elif choice == "CI":
    print("The amount is " + str(CI(P, R, n)))

