#27.	Accept a list of words and sort them by their length using for loops.
n=int(input("Enter the no.of elements you'd like to add to the list:  "))
lst=[]
length=[]
for i in range(n):
    element=input("Enter the word: ")
    lst.append(element)
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(len(lst[i])>len(lst[j])):
            lst[i],lst[j]=lst[j],lst[i]
print(lst)
