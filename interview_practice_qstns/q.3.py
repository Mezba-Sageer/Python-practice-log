#Coding questions (first round)
# 1: implement a function to encode a given string by the following manner
# car - ect
# c -3 becomes  e-5 .
# +2 for each alphabet
#
# 2: given a list of numbers indicating the changes.
# Return minimum number of coin required to give the required amount.

word=input("Enter a word: ")
word1=""
for i in word:
    ascii_num=ord(i)+2
    word1+=chr(ascii_num)
print(word1)