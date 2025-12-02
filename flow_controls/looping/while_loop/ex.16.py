#print the sum of odd and even number between the lower and upper range
lower=int(input("enter the lower limit: ")) #initialization
upper=int(input("Enter the upper limit: "))
e_sum=0
o_sum=0
while(lower<=upper): #condition
    if(lower%2==0):
        e_sum+=lower
    else:
        o_sum+=lower
    lower+=1 #increment
print(e_sum)
print(o_sum)
