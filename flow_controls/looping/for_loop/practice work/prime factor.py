#29.	Find the largest prime factor of a number.
lst=[]
prime_fact=[]
num=int(input("Enter a number: "))
for i in range(2,num):
    if(num%i==0):
       for j in range(2,i):
         if(i%j==0):
            break
       else:
         prime_fact.append(i)
print(max(prime_fact))