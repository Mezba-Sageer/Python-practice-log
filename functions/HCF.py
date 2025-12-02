#find the HCF- highest common factor
#eg:12: 1,2,3,4,6,12
#eg:15: 1,3,5,15
#3 is the HCF
# def HCF(num1,num2):
#     if(num1>num2):
#         lowest=num2
#     else:
#         lowest=num1
#     for i in range(1,lowest+1): #has to go only till the lowest num. bcz bfr that the we'll get the hcf.
#         if(num1%i==0 and num2%i==0):
#             hcf=i
#     return hcf
# num1=int(input("Enter first number: "))
# num2=int(input("Enter 2nd number: "))
# print(HCF(num1,num2))

#if print statement inside function no need for return, jst have to call function
#since the print statement is outside use return

def hcf(x,y):
    if x<y:
        lowest=x
    else:
        lowest=y
    for i in range(1,lowest+1):
        if(x%i==0 and y%i==0):
            HCF=i
    return HCF
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
print(hcf(x,y))
