mystring="Python is easy to learn, it is simple to use"
print(mystring.find("is")) #returns the index of is
print(mystring.find("hello")) #returns -1 when hello is not there in the string


print(mystring.index("is")) #returns index number as output
# print(mystring.index("hello")) #returns error message that string is not available

#even when there is two same words in a string it returns the index of first word it finds - in case of both funct

print(mystring.rfind("is")) #returns the index of the last is.

print(mystring.count("is")) #returns the count of is
print(mystring.count("Python")) #returns the count of is


