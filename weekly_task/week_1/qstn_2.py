#question 5: 5. Create a simple marksheet program:
# Input marks of 5 subjects, calculate average, and print the * grade based on average marks.
sub1=int(input("Enter the marks of 1st subject: "))
sub2=int(input("Enter the marks of 2nd subject: "))
sub3=int(input("Enter the marks of 3rd subject: "))
sub4=int(input("Enter the marks of 4th subject: "))
sub5=int(input("Enter the marks of 5th subject: "))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("grade is A+")
elif(85<=avg<90):
    print("grade is A")
elif(80<=avg<85):
    print("grade is B+")
elif(75<=avg<80):
    print("grade is B")
elif(70<=avg<75):
    print("grade is C+")
elif(65<=avg<70):
    print("grade is C")
else:
    print("fail")




