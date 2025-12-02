#python program to check the validity of password input by users
password=input("Enter your password: ")
upper=lower=digit=spcl=0
spcl_char='@#$%^&*!'
for i in password:
    if(i.isupper()):
        upper+=1
    elif(i.islower()):
        lower+=1
    elif(i.isdigit()):
        digit+=1
    elif(i in spcl_char):
        spcl+=1
if(len(password)>=8 and upper>=1 and lower>=1 and digit>=1 and spcl>=1):
    print("password is valid")
else:
    print("password is not valid")

