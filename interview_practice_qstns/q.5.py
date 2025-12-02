# Write a function called capitalize.
# This function takes a string as an argument and capitalizes the first letter of each word. For example,
# 'i like learning' becomes '1 Like Learning'.

def capitalize(text):
    new_words=text.split()
    capital_wrd=""
    for i in new_words:
        capital_wrd+=i.capitalize()+" "
    print(capital_wrd)
text=input("Enter a sentence: ")
capitalize(text)