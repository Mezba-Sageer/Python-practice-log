#write a python program to read four numbers(representing the four octets of an IP) and print the next five IP address
#eg: input: 192 168 255 252
IP_input=input("Enter IP address (e.g 192 168 1 250): ").split()
#here the IP address is taken as string and the split function is used to read the input as list,
# using the spaces to separate values - ['192','168','1','250'] - the list is in string format rn
if (len(IP_input)!=4):
    print("Enter a valid 4 numbers with spaces in between")
else:
    a,b,c,d=map(int,IP_input)
#map() give answer for each variable
#where 'a' acts as the first part i.e 192 similarly the following
if any(part<0 or part>255 for part in [a,b,c,d]):
    print("Each part of the IP must be between 0 and 255")
else:
    for _ in range(5):
        d+=1 #value in part d is incremented until it become 255
        if(d==256):
            d=0
            c+=1
            if(c==256):
                c=0
                b+=1
                if(b==256):
                    b=0
                    a+=1
                    if(a==256):
                        print("IP limit exceeded")
                        break
        print(a,b,c,d)


