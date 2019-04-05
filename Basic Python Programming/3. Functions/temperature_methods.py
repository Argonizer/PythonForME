def celsius_to_fahrenheit(cel):
    fah = cel * 9/5 + 32
    return fah

def celsius_to_kelvin(cel):
    kel = 273.15 + cel
    return kel

def kelvin_to_fahrenheit(kel):
    cel = kelvin_to_celsius(kel)
    fah = celsius_to_fahrenheit(cel)
    return fah

def kelvin_to_celsius(kel):
    cel = kel - 273.15
    return cel

def fahrenheit_to_celsius(fah):
    cel = (fah - 32) * 5/9
    return cel

def fahrenheit_to_kelvin(fah):
    cel = fahrenheit_to_celsius(fah)
    kel = celsius_to_kelvin(cel)
    return kel

#to see how these functions are used, refer to temperature.py