#Create a function called words_with_vowels, this function takes a string of words and returns a list of
# only words that have vowels in them. For example ' You have no rhythm' should return ['You', 'have', 'no'].
def words_with_vowels(words):
    vowel_lst=[]
    lst=words.split()
    for i in lst:
        for j in i:
            if j in 'aeiouAEIOU':
                vowel_lst.append(i)
    return vowel_lst
words=input("Enter a sentence: ")
words_with_vowels(words)
