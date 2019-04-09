name = input("Enter The String\n")
char = input("Enter character whose frequency to find\n")

count = 0
for i in range(len(name)):
    if name[i] == char:
        count += 1

print(char, "appeared", count, "times")