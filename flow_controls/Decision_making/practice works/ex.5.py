#25.	Accept a string and check if it's a palindrome (same forward and backward).
str1=input("Enter a word: ") #eg:madam- length=5
temp=str1
reverse="" #to store string
for i in range(len(str1)-1,-1,-1): #range(5-1,-1,-1)=(4,0,-1)
    reverse+=str1[i]
    #str1[4]=m if simply i is added instead of str[i]
    # numbers are added to the string so hence str1[i]
    #to convert the int value of range to string
if(temp==reverse):
    print("palindrome")
else:
    print("Not palindrome")
    



