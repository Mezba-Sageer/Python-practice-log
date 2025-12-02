#Write a function that has one parameter and takes a list of words as an argument.
# The function returns the longest word from the list.
# Name the function longest word. The function should return the longest word and the number of letters in that word.
# For example, if you pass ['Java, 'JavaScript', 'Python'], your function should return [10, JavaScript] as the longest word.
def longest_word(lst1):
    longest=""
    for i in lst1:
        if len(i)>len(longest):
            longest=i
    return [len(longest),longest]

words=['Java','Javascript','Python']
print(longest_word(words))