#read 3 numbers from the user and print the second-largest number
num1=int(input("Enter the first number:  "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

#nested if method
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("num2 is the 2nd greatest")
    else:
        print("num 3 is the 2nd greatest")
elif(num2>num1&num2>num3):
    if(num1>num3):
        print("Num1 is 2nd greatest")
    else:
        print("num 3 is 2nd greatest")
elif(num3>num1&num3>num2):
    if(num2>num1):
        print("num2 is 2nd greatest")
    else:
        print("num1 is 2nd greatest")
else:
    print("invalid")

#method 1:- when the order of input is eg:100,80,60 this code gives wrong ans
# if(num1>num2&num1<num3)or(num1>num3&num1<num2):
#     print("the second largest no. is",num1)
# elif(num2>num1&num2<num3)or(num2>num3&num2<num1):
#     print("the second largest is",num2)
# else:
#     print("the second largest is",num3)


#syntax of nested if
#if(condition1):
    #if(cndtnd2):
        #stmnt1
    #else:
        #stmnt2
#elif(condition3):
    #if(cndtn4):
        #stmnt3
    #else:
         #stmnt4
#else:
       #stmnt5




