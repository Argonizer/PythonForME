from perfect_number_check import perfect

num = int(input("Enter the limit upto which perfect numbers be checked\n"))
for i in range(1, num):
     if perfect(i):
         print(i)