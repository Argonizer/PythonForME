def pattern1(num, char):
    for i in range(num):
        for j in range(num):
            if j <= i:
                print(char, end = "")
        print("")


def pattern2(num, char):
    for i in range(num):
        for j in range(num):
            if i + j < num:
                print(char, end = "")
        print("")

def pattern3(num, char):
    for i in range(num):
        for j in range(num):
            if j < i:
                print(" ", end = "")
            else:
                print(char, end = "")
        print("")

def pattern4(num, char):
    for i in range(num):
        for j in range(num):
            if i + j < num - 1:
                print(" ", end = "")
            else:
                print(char, end = "")
        print("")

pattern1(5, "*")
pattern2(5, "*")
pattern3(5, "*")
pattern4(5, "*")