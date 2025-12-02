#LCM- Least common multiple
#x=3 multiples of 3: 3,6,9,12,15,18,21,24.....
#y=4 multiples of 4: 4,8,12,16,20,24....
#common multiples= 12,24.....
#here LCM is 12
#using while true and mod of both numbers

# x=int(input("Enter x: "))
# y=int(input("Enter Y: "))
# def lcm(x,y):
#     if(x>y):
#         greater=x
#     else:
#         greater=y
#     while(True):
#      if(greater%x==0 and greater%y==0):
#         return greater
#      else:
#          greater+=1
# print("LCM is: ",lcm(x,y))


def lcm(x,y):
    if(x>y):
        greatest=x
    else:
        greatest=y
    while(True):
            if(greatest%x==0 and greatest%y==0):
                break
            greatest+=1
    return greatest
x=int(input("enter a number: "))
y=int(input("enter a number: "))
print(lcm(x,y))
