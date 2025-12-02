#Q.3 write a program that prints all even numbers from 1-10 using
# a while loop and continue statement
i=1
while(i<=10):
    if(i%2==1):
        i+=1
        continue
    print(i)
    i+=1