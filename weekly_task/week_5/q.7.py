#Q.7 Write a program that uses continue to skip over certain iterations in a loop that processes a list or strings,
# skipping strings shorter than 3 characters.
strings = ["a","abc", "defg", "hi", "jkl"]
for i in strings:
    if(len(i)<3):
        continue
    print(i)