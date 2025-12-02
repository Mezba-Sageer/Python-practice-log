#code of fibonocci series which means sum of first two numbers in the third
#have to swap the sum from one place to another progressively
#eg:- 0 1(this is defualt in the series) 1(0+1) 2(1+1) 3(2+1) 5(3+2) 8(5+3)
# the series to print - 0 1 1 2 3 5 8 13

limit=int(input("enter the limit: "))
num1=0
num2=1
print(num1,end=" ") #prints 1 nd 2
print(num2,end=" ")
for i in range(3,limit+1): #(when i=3) (sum=0+1=1) (when i=4) (when i=5) i=6
#0&1 is default so tht is to be printed as first step and
# if limit is 10 first 2 position has been filled so we strt frm 3
    sum=num1+num2 #1+1=2 1+2=3 2+3=5 3+5=8
    #swapping is performed as the series is basically swapping
    num1=num2 #num1=1, num1=1, num1=2, num1=3
    num2=sum #num2=1 num2=2 num2=3, num2=5
    print(sum,end=" ")