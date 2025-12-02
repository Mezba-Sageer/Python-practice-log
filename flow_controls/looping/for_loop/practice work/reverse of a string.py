#3.	Print the reverse of a string without using slicing or reversed().
st1=input("Enter a word: ")
rev=""
for i in st1:
    rev=i+rev
    #in this the i value gets added first later the first value which was added to rev
    #suppose input word is hello
    #i 1st iterates to h
    #rev=h+' ' ---> 2nd iteration: rev=e+'h' -----> 3rd iteration- rev=l+'eh' --> therefore at the end the input is
    #completely reversed
print(rev)


