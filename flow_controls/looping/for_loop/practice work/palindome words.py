#25.	From a given string, print all the words that are palindrome.
sentence = "Madam Arora teaches malayalam and level civic stats"
words=sentence.split()
for i in words:
    if i[::-1].lower()==i.lower():
        print(i)
