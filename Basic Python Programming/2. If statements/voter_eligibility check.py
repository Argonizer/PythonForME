age = int(input("Enter your age"))

if(age > 18):
    print("You can vote")

if(age < 18):
    print("You can't vote")

else:
    print("Register ID")
    gender = input("Enter your gender")
    if(gender == "male"):
        print("go to male booth")
    else:
        print("go to female booth")
