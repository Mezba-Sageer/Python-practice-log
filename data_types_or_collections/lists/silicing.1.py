#list slicing
lst1=[2,54,56,67,87,95,46,799,96,69,34,100,120,345,765,12,28]
#syntax of slicing: [start:stop]----> output- [start:stop-1]
#slicing is applied when we have to extract a certain range of values from a list
print(lst1[3:6]) #prints the values from index 3-5
print(lst1[2:7]) #prints values from index 2-6
print(lst1[4:]) #this executes from the 4th index till the last index
print(lst1[:5]) #this print values from index 0 to 4
print(lst1[:]) #this range prints the entire values in a list because no start and stop is mentioned
print(lst1[2:8:2]) #here 2 is the step value and prints index's: 2,4,6
print(lst1[1:9:3])
print(lst1[3::2]) #prints from index 3 till the last index with the step value of 2
print(lst1[:9:3]) #prints from index 0 till the 8th index with the step value of 3
print(lst1[::4]) #even tho there isn't start and stop values it prints from the 0th index till the end with 4 as step

#athulya ma'am portion:
list1=["Neethu","Vipin","Anu","mezba","farsi"]
print(type(list1))
print(list1[0:5:2]) #only takes certain elements of the list using step value or slicing
print(list1[1:3]) #only prints certain elements within a range