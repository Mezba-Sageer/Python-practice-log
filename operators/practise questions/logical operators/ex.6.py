#48.	Accept a string and check if the first and last characters are the same.
str=input("Enter a string: ")
if(len(str)>0 and str[0]==str[-1]):
    print("they are same")
else:
    print("tis not")