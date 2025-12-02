#from the below list generate
lst=[12,8,3,10,7,15,5]
lst1=[]
#this list: #lst1=[48,52,57,50,53,45,55] - this list contains elements where the elements are the difference btw
#sum of all elements and each element
#i.e sum of lst=60
#first element of lst1=60-12=48
sum1=sum(lst) #can't use variable name sum bcz sum() is a function
print(sum1)
for i in lst:
    lst1.append(sum1-i)
print(lst1)

