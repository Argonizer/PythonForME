from temperature_methods import *

temp = float(input("Enter temperature without units : "))
unit1 = str(input("Enter the current temperature unit (C, F or K) : "))

unit2 = str(input("Enter the temperature unit to convert to (C, F or K) : "))

if unit1 == "C":
    if unit2 == "F":
        new_temp = celsius_to_fahrenheit(temp)
    if unit2 == "K":
        new_temp = celsius_to_kelvin(temp)
    print("The converted temperature is", new_temp, unit2)

elif unit1 == "F":
    if unit2 == "C":
        new_temp = fahrenheit_to_celsius(temp)
    if unit2 == "K":
        new_temp = fahrenheit_to_kelvin(temp)
    print("The converted temperature is", new_temp, unit2)

elif unit1 == "K":
    if unit2 == "F":
        new_temp = kelvin_to_fahrenheit(temp)
    if unit2 == "C":
        new_temp = kelvin_to_celsius(temp)
    print("The converted temperature is", new_temp, unit2)