x=10 #global value
def myfunctn():
    x=10 #local value
    print("local x value is: ",x)
print("global x value is: ",x)
myfunctn()


x=10
def myfunctn():
    x=15
    print("local x value is: ",x)
print("global x value is: ",x)
myfunctn()
