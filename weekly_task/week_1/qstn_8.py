#Write a Python program to check if a given string is a valid identifier or not. An identifier is valid
# if it starts with a letter (a-z, A-Z) or an underscore (_)
# followed by zero or more letters, underscores, or digits (0-9).
word=input("Enter a string: ")
if(word!="")and(word[0].isalpha()or word[0]=="_")and all(char.isalnum() or char=="_" for char in word[1:]):
    print("Valid identifier")
else:
    print("Invalid identifier")
#word!=="" - checks if the user entered something
#word[0].isalpha or word[0]=="_" - checks if the first character of the input is an alphabet regardless of the case.
#all - checks all values and conditions within that function
#char.isalnum - checks whether each letter/character is an alphabet or a number
#for char in word[1:] - this is a loop to check each character in a word from the index position one
# since the first character has already been checked
