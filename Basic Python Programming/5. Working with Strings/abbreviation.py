name = input("Enter Full Name\n")

name.strip()
name = " " + name
abbr = ""

for i in range(len(name)):
    if name[i] == " ":
        abbr += name[i+1].upper() + ". "

print(abbr)