#1. create a list of square of numbers from 1 to 10
lst1=[i**2 for i in range(1,11)]
print(lst1)

#2. Create a list of even numbers from 1 to 20
lst2=[i for i in range(1,21) if i%2==0]
print(lst2)

#3. Generate a list of characters from a string
string='Helloworld'
lst3=[i for i in string]
print(lst3)

#4. create a list of lengths of words in a sentence
string='this is a sample sentence'
lsts=string.split(' ')
lst4=[len(i) for i in lsts]
print(lst4)

#5. create a list of common multiples of 3 and 5 upto 100
lst5=[i for i in range(1,101) if i%3==0 and i%5==0 ]
print(lst5)

#6. create a list of reversed strings from another list
words=['apple','orange','mango']
lst6=[i[::-1] for i in words]
print(lst6)