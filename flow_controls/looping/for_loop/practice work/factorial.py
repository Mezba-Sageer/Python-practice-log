#14. Find the factorial of all numbers from 1 to 10 and store in a dictionary.
dic={}
for i in range(1,11):
    fact=1
    for j in range(1,i+1):
        fact*=j
    dic[i]=fact
print(dic)
