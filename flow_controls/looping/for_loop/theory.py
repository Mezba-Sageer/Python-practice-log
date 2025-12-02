#for loop
#print hello using for loop
#syntax:
for i in range(1,11): #1- is the start point and 10 is the end point
    print("hello") #for loop only prints hello 9 times if 10 is given in range because by default for loop prints (n-1) times
    #no decrement statement needed as it automatically increments by 1
    #to print 10 times add 11 to the range instead of 10
    #for i in rang(start,stop,step)
    #here step is the increment or decrement number

for i in range(1,21,1): #this condition gives the output by printing 1-20 and the one after
                         #21 is the increment statement which increases the i value by 1
    print(i)

for i in range(1,16,3): #3 is the increment value 16 is not printed since for loop prints n-1 that is only till 15
    print(i)

#we can only pass integer values in the range

for i in range(10): #here 10 acts as the stop number or the limit and by default it starts at 0.
                    #therefor the output is 0-9, 10 is not printed bcz the output is n-1
    print(i)