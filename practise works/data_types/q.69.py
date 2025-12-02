#069
# Create a tuple containing the names of five countries and display the whole tuple.
# Ask the user to enter one of the countries that have been shown to them and then display the index number
# (i.e. position in the list) of that item in the tuple.
tu1=('india','australia','canada','uk','germany')
print(tu1)
word=input("Enter a country from the display: ")
print(tu1.index(word))

#070
#Add to program 069 to ask the user to enter a number and display the country in that position.
num=int(input("Enter a num: "))
if(num<5):
    print(tu1[num])
else:
    print("Enter a valid number ")