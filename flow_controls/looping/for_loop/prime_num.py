#to check if a num is a prime num
#we strt the range from 2- bcz we have to check whether the number we enter is divisible after 1 which is from 2
#till the num entered the num entered need not be checked since it's already divisible
#here a flag variable is used bcz if the print statement is used within the loop it'll keep printing
# prime or not prime in each iteration to avoid this we use a flag variable
# num=int(input("Enter a number: "))
# flag=0
# for i in range(2,num):
#     if(num%i==0):
#        flag=1
# if(flag>0):
#     print("number is not prime")
# else:
#     print("number is prime")

num=int(input("Enter a number: "))
count=0
for i in range(2,num):
    if(num%i==0):
        count+=1
if(count>0):
    print("number is not prime")
else:
    print("Number is prime")


