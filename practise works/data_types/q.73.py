# 073
# Ask the user to enter four of their favourite foods and store them in a dictionary so that they are indexed
# with numbers starting from 1. Display the dictionary in full, showing the index number and the item.
# Ask them which they want to get rid of and remove it from the list. Sort the remaining data and display the dictionary.
fav_food=input("Enter 4 favourite food of yours: ")
lst_food=fav_food.split(' ')
dic1={}
for i in range(0,4):
        dic1[i+1]=lst_food[i]
print(dic1)
remove_data=input("WHich element do you want to remove: ")
for i in dic1:
    if dic1[i]==remove_data:
        del dic1[i]
        break
sorted_dic1=sorted(dic1.values())
lst2={i+1:sorted_dic1[i] for i in range(0,5)}
print(lst2)