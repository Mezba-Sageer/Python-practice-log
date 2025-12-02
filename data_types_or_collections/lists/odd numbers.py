#add 1-50 odd numbers into the list and find their sum
lst=[]
for i in range(1,51):
    if(i%2!=0):
        lst.append(i)
print(lst)
print(sum(lst))