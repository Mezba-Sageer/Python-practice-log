#count the vowels in a string using list
str1="LuminarTechnolab"
vowels=['a','e','i','o','u']
count=0
for i in str1:
    if(i in vowels):
        count+=1
print("count of vowels: ",count)

#another method - this is how u should do using list not abv method
vowel="aeiouAEIOU"
lst=[]
for j in str1:
    if(j in vowel):
        lst.append(i)
print(len(lst))
