#Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller
# number goes into the larger number in a user-friendly format.
abv100=int(input("enter a number above 100: "))
blw10=int(input("enter a number below 10: "))
no_of_time=abv100//blw10
print("the number of times",blw10,"goes into",abv100,"is",no_of_time)
