#24.	Accept a password and check:
# •	At least 8 characters,
# •	Includes at least one digit,
# •	Starts with a capital letter.

password=input("Enter your password: ")
count=0
if(len(password)>=8):
   for i in range(len(password)):
       if password[i].isdigit():
        count+=1
   if(count>0 and password[0].isupper()):
       print("Password meets all conditions")
   else:
       print("Password doesn't either have a digit or the first letter is not capital")
else:
    print("password has less than 8 characters")
