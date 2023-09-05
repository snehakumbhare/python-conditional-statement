#Write a program to Accept marks 0f 5 subject each subject out 100 and Display Each subject marks, Total Marks, Percentage and He/She Grade as per following critica 

	#A grades - marks above 85

	#B grades - Marks above 70

	#C grade - Marks above 60

	#D grade - Marks above 45

	#E grade - Marks above 35

	#Fail - Marks below 35

sub1=int(input("Enter marks of the first subject:"))
sub2=int(input("Enter marks of the second subject:"))
sub3=int(input("Enter marks of the third subject:"))
sub4=int(input("Enter marks of the fourth subject :"))
sub5=int(input("Enter marks of the fifth subject:"))
total=(sub1+sub2+sub3+sub4+sub5)
percentage=(total/500)*100
if(percentage>=80):
    print("Grade: A")
elif(percentage>=70&avg<80):
    print("Grade: B")
elif(percentage>=60&avg<70):
    print("Grade: C")
elif(percentage>=45&avg<60):
    print("Grade: D")
elif(percentage>=35&avg<45):
    print("Grade: E")
else:
    print("Grade: fail")
print("total:",total)
print("Percentage:",percentage)