# Q5. Password Strength Checker
# Problem:
# Input: A password string
# Tasks:
# 1. Check for upper, lower, digit, special char.
# 2. Count missing types.
# 3. Check length.
# 4. Return strength and suggestions.

def password_strength_checker(st):
    upper=0
    lower=0
    digit_=0
    miss_count=0
    spcl_char=0
    for i in st:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            digit_+=1
        elif not i.isalnum():
            spcl_char+=1
    pass_len=len(st)

