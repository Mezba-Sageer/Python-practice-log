#factorial of a number
limit=int(input("Enter a number: "))
i=1
factorial=1
while(i<=limit): #1<=5 2<=5 3<=5 4<=5
    factorial*=i #(fact= fact*i) fact=1*1 fact=1*2 fact=2*3 6*4 24*5=120
    i+=1
print("the factorial is",factorial)


