#python program to display all numbers within a range except the prime numbers.
lowest=int(input("Enter the lower range: ")) #10
upper=int(input("Enter the upper range: ")) #20

#prime num numbers where only 1 and tht number is the multiple
for i in range(lowest,upper+1): #(10-20)
    c=2
    count=0
    while(c<i): #(2<20) #3<20T
        if(i%c==0): #20%2==0
            count+=1 #count=1
        c+=1
    if(count!=0):
        print(i,end=" ")


