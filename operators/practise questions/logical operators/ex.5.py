#43.	Accept a character and check if it’s an alphabet and a vowel.
str1=input("Enter a character: ")
if(str1.isalpha()):
    if (str1 in ['a','e','i','o','u']):
        print("it is an alphabet and vowel")
    else:
        print("it is not a vowel")
else:
    print("Not an alphabet or vowel")