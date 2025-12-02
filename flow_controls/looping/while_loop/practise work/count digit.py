#27.	Accept a number and count how many times each digit appears.
# num=int(input("Enter a number: "))
# original=num
# digit=0
# while(digit<=9):
#     n=original
#     count=0
#     while(n!=0):
#         rem=n%10
#         if(rem==digit):
#             count+=1
#         n//=10
#     if(count>0):
#         print("digit: ",digit,"appears",count,"of times")
#     digit+=1


#for counting how many times a particular digit appears in a number we have to run the loop from 0-9
n=int(input("Enter a number: "))
i=0
while(i<=9):
    temp=n
    count=0
    while(temp!=0):
       rem = temp % 10
       if(rem==i):
          count+=1
       temp//=10
    if(count>0):
       print("digit: ",i,"appears",count,"no of times")
    i+=1
