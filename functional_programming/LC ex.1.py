#using list comprehension count the vowels
string='Luminartechnolab'
lst=[i for i in string if i in "AEIOUaeiou"]
print(len(lst))

#calculate the sum of consonants
lst2=[i for i in string if i not in "AEIOUaeiou"]
print(len(lst2))