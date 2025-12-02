#print even numbers in the range of 1-75 inside a list 
lst=[]
for i in range(1,76):
    if(i%2==0):
        lst.append(i)
print(lst)