# 36.	Simulate a password entry system with 3 attempts.
correct_pass="admin123"
attempt=1
while(attempt<=3):
    enter_pass=input("Enter the password: ")
    if(enter_pass==correct_pass):
        print("Access granted")
        break
    else:
        print("Access denied,try again: ")
        attempt+=1
if(attempt>3):
    print("Too many attempts try again later")