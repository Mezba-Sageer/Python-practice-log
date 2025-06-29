#A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks=int(input("enter the marks: "))
if(80<=marks<=100):
    print("grade: A")
elif(60<=marks<80):
    print("grade: B")
elif(50<=marks<60):
    print("grade: C")
elif(45<=marks<50):
    print("grade: D")
elif(25<=marks<45):
    print("grade: E")
elif(marks<25):
    print("grade: F")
else:
   print("enter a valid number")

