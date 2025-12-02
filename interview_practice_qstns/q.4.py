#Write a function called sort_words that takes a string of words as an argument,
# removes the whitespaces, and returns a list of letters sorted in alphabetical order.
# Letters will be separated by commas. All letters should appear once in the list.
# This means that you sort and remove duplicates. For example 'love life' should return as ['e,f,i,l,o,v'].

def sort_words(word):
    lst=[]
    no_space=word.replace(" ","")
    for i in no_space:
        if i not in lst:
            lst.append(i)
    result=[",".join(sorted(lst))]
    print(result)

word=input("Enter a sentence: ")
sort_words(word)



