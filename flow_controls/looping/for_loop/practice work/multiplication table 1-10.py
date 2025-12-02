#21.Print the multiplication table of all numbers from 1 to 10 using nested for loops.
for i in range(1,11):
    for j in range(1,11):
        print(j,"*",i,"=",i*j)
    print()
