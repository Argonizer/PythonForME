set1 = "1 3 5 7\n" + \
       "9 11 13 15\n" + \
       "17 19 21 23\n" + \
       "25 27 29 31\n"

set2 = "2 3 6 7\n" + \
       "10 11 14 15\n" + \
       "18 19 22 23\n" + \
       "26 27 30 31\n"

set3 = "4 5 6 7\n" + \
       "12 13 14 15\n" + \
       "20 21 22 23\n" + \
       "28 29 30 31\n"

set4 = "8 9 10 11\n" + \
       "12 13 14 15\n" + \
       "24 25 26 27\n" + \
       "28 29 30 31\n"

set5 = "16 17 18 19\n" + \
       "20 21 22 23\n" + \
       "24 25 26 27\n" + \
       "28 29 30 31\n"

date = 0

print("Is your birthdate in Set 1?\n" + set1)
answer = int(input("Enter 1 for Yes and 0 for No\n"))
if answer == 1:
    date += 1

print("Is your birthdate in Set 2?\n" + set2)
answer = int(input("Enter 1 for Yes and 0 for No\n"))
if answer == 1:
    date += 2

print("Is your birthdate in Set 3?\n" + set3)
answer = int(input("Enter 1 for Yes and 0 for No\n"))
if answer == 1:
    date += 4

print("Is your birthdate in Set 4?\n" + set4)
answer = int(input("Enter 1 for Yes and 0 for No\n"))
if answer == 1:
    date += 8

print("Is your birthdate in Set 5?\n" + set5)
answer = int(input("Enter 1 for Yes and 0 for No\n"))
if answer == 1:
    date += 16

print("Your birthdate is", date)