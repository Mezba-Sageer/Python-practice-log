#Q2. Character Frequency Counter
# Problem:
# Input: A string
# Tasks:
# 1. Remove spaces and convert to lowercase.
# 2. Count frequency of each character.
# 3. Return only characters with frequency > 1.
# 4. Return as sorted list of tuples.

def word():
    s=input("Enter a string: ")
    s=s.replace(" ","").lower()
    freq={}
    lst1=[]
    for i in s:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    for i in freq:
        if freq[i]>1:
            lst1.append((i,freq[i]))
    return sorted(lst1)
print(word())













