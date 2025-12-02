#factorial of a number
#fatorial=1*2*3*4*5*6*7
num=int(input("Enter a number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print("factorial is",factorial)
