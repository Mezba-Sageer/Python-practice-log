#Q.6:Write a Python function that uses break to exit early if a
# certain condition is met while iterating through a list.
lst1=[1,2,3,4,5,6,7,8,9,10]
def demo(lst1):
    for i in lst1:
        if(i==5):
            break
        print(i)
demo(lst1)