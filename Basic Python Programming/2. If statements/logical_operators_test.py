print("Enter True or False")
cond1 = input("Enter condition 1\n")
if cond1 == "False":
    cond1 = ""
    
cond2 = input("Enter condition 2\n")
if cond2 == "False":
    cond2 = ""

cond1 = bool(cond1)
cond2 = bool(cond2)

if cond1 and cond2:
	print("Both are True")

elif cond1 or cond2:
	print("One True, Other one False")

elif not cond1 and not cond2:
	print("Both are False")
