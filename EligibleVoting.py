#Write a program to check whether a person is eligible for voting or not.(accept age from user)

age=int(input("Enter age:"))

if age>=18:
    print(f"{age} Eligible for voting")
else:
    print(f"{age} Not Eligible for voting")
