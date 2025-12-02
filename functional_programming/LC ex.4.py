#1. split the sentence into words
#2. Remove all words that contain any digits
#3. Convert remaining words to title case
#4. count how many words start with a capital vowel
#5. Return the list and the count

#sentence: "In 2025, Alice and Bob Visited 3 Countries Before Returning To India."
string1="In 2025 Alice and Bob Visited 3 Countries Before Returning To India"
lst1=string1.split(' ')
count=0
filtered=[i for i in lst1 if i.isalpha()]
title=[i.title() for i in filtered]
count_vowel=[count+1 for i in title if i[0] in "AEIOU"]
print(title)
print(len(count_vowel))