#39.	Accept a sentence and reverse it word by word using while loop.
sentence=input("Enter a sentence: ")
rev=" "
words=sentence.split(" ")
i=1
while(i<=len(words)): #(1<3)
    rev+=words[-i]+" "
    i+=1
print(rev)