name = input("Enter a word\n")

name.strip()
pig = name[1:] + "-" + name[0].upper() + "ay"

print("Pig Latin form of the word would be", pig)