# Write a Program to Calculate the Simple Interest for Bank Customer for Fixed Deposit

# a. If customer is Female and Senior Citizen 8% rate

# b. If customer is Female and Non-Senior Citizen 6% rate

# c. If customer is Male and Senior Citizen 7% rate

# d. If customer is Male and Non-Senior Citizen 5% rate



age=int(input("Enter your Age:"))
gender=input("Choose your Gender(M/F):")

if age>=65 and gender == 'M':
    p=int(input("Enter capital Amount:"))
    t=int(input("Enter Time in Years:"))
    simint=(p*0.07*t)
    print("Simple Interest: {}".format(simint))
elif age < 65 and gender == 'M':
    p=int(input("Enter capital Amount:"))
    t=int(input("Enter Time in Years:"))
    simint=(p*0.05*t)
    print("Simple Interest: {}".format(simint))

elif age >= 65 and gender == 'F':
    p=int(input("Enter capital Amount:"))
    t=int(input("Enter Time in Years:"))
    simint=(p*0.08*t)
    print("Simple Interest: {}".format(simint))
elif age < 65 and gender == 'F':
    p=int(input("Enter capital Amount:"))
    t=int(input("Enter Time in Years:"))
    simint=(p*0.06*t)
    print("Simple Interest: {}".format(simint))
else:
    print("Invalid Input")