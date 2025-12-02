#Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
# For example, if you pass '23569' as an argument, your function should return 9. Use list comprehension.
def biggest_odd(str1):
    lst1=[int(i) for i in str1 if int(i)%2!=0]
    print(max(lst1))
text=input("Enter a string of numbers: ")
biggest_odd(text)
