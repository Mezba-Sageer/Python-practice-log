#16.	Accept a string and print frequency of each character.
string1=input("Enter a word: ")
count=0
dic={}
for i in string1:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

