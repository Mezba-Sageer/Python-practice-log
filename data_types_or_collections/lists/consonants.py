#another method - this is how u should do using list not abv method
#consonants meaning- letters other than vowels is referred as consonants
str1="luminartechnolab"
vowel="aeiouAEIOU"
lst=[]
for i in str1:
    if(i not in vowel):
        lst.append(i)
print(lst)
