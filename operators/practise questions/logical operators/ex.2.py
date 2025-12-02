#35.	Accept a string and check if it starts with 'A' and length > 5.
word=input("Enter a word: ")
if((word[0]=="A" or word[0]=="a") and len(word)>5):
    print("right format")
else:
    print("wrong format")

