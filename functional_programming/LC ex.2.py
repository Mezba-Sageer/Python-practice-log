#qstn1: Find all numbers from 1-1000 that are divisible by 7
string="practice list comprehension problem to drill your head"
lst1=[i for i in range(1,1001) if i%7==0]
print(lst1)

#qstn2: Find all numbers from 1-1000 that have 3 in it
lst2=[i for i in range(1,1000) if "3" in str(i)]
print(lst2)

#qstn3: count no.of spaces in a string
lst3=[i for i in string if i==' ']
print(len(lst3))

#qstn4: count no.of vowels in a string
lst4=[i for i in string if i in "aeiouAEIOU"]
print(len(lst4))

#qstn5: count words in a list with less than 3 characters
lstw=string.split(' ')
lst5=[i for i in lstw if len(i)<4]
print(len(lst5))