#python program that accepts a word from the user and reverses it
word=input("enter a word: ") #hello
rev=""
for i in word[-1::-1]:
    rev+=i
print(rev)
#[::-1] logic behind this statement is that :
#here the start value is empty - so since the step value is -ve by default the iteration goes to the end of the string
#here the stop value is empty - so it runs till the beginning index of the word that is till the length of the word.
#both this happens by default since the step value is -1.
#-1 is the step values and it keep decrementing
