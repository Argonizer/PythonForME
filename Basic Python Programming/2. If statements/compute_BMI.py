
height = float(input("Enter Height in metres : "))
weight = float(input("Enter Weight in kilograms : "))

BMI = weight / height**2

print("Your BMI is", BMI)

if BMI < 16:
    print("You are seriously underweight")

elif BMI < 18:
    print("You are underweight")

elif BMI < 24:
    print("You are normal weight")

elif BMI < 29:
    print("You are overweight")

elif BMI < 35:
    print("You are seriously overweight")