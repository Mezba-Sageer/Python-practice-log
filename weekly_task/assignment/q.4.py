# Q4. Sentence Word Mapper
# Problem:
# Input: A string of words
# Tasks:
# 1. Create dictionary: word -> length.
# 2. Filter out non-prime lengths.
# 3. Return sorted by length descending


#function to check if the length of the word is a prime number
def prime(num):
    j=2
    while j<num:
        if num%j==0: #if this condition is false the entire loop doesn't run and stop when the condition becomes false
            return False
        j+=1 #increment statement for prime no.s to check if they're divisible from 2 to n-1
    return True #returns true only if the no. is prime
#so for prime no.s the function returns true


def word_mapper(str1):
    lst1=str1.split()
    dic1={i:len(i) for i in lst1} #dic to store word and its length
    dic2={k:v for k,v in dic1.items() if prime(v)} #dictionary storing only prime length and their corresponding key value
    sorted_dic=dict(sorted(dic2.items(),reverse=True)) #this dictionary is sorted by its length in ascending order
    #sorted syntax - sorted(iterable to sort,key=(on what basis you want to sort the value),
    # reverse=True(this is mentioning the order by default its ascending))
    return sorted_dic

str1=input("Enter a sentence: ")
print(word_mapper(str1))