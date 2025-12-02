# Q1. Even-Odd Dictionary
# Problem:
# Input: A list of integers
# Tasks:
# 1. Separate the numbers into even and odd using for loop.
# 2. Count how many are divisible by 3.
# 3. Use while loop to sum all odd numbers.
# 4. Return a dictionary.

def lst():
    lst1=[]
    lst_odd=[]
    lst_even=[]
    count=0
    total=0
    n=int(input("Enter the limit: "))
    i=1
    while(i<=n):
        num=int(input("Enter a number: "))
        lst1.append(num)
        i+=1
    for i in lst1:
        if(i%3==0):
            count+=1
        if(i%2==0):
            lst_even.append(i)
        else:
            lst_odd.append(i)
    i=0
    while(i<len(lst_odd)):
        total+=lst_odd[i]
        i+=1
    result={'Even':lst_even,'Odd':lst_odd,'Count':count,'Sum':total}
    return result
print(lst())









