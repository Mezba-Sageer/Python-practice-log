#29.	Implement a simple calculator that keeps asking for operation until user quits.

lst_opr=['+','-','*','/','%','//']
while True:
    num1 = int(input("enter 1st number: "))
    num2 = int(input("enter 2nd number: "))
    operation = input("enter an operation('+','-','*','/','%','//'): ")
    if(operation=="+"):
        result=num1+num2
    elif(operation=="-"):
        result=num1-num2
    elif(operation=="*"):
        result=num1*num2
    elif(operation=="/"):
        if(num2!=0):
           result=num1/num2
        else:
            print("cannot divide by zero")
        continue
    elif(operation=="//"):
        if (num2 != 0):
            result = num1 // num2
        else:
            print("cannot divide by zero")
        continue
    elif(operation=="%"):
        if (num2 != 0):
            result = num1 % num2
        else:
            print("cannot divide by zero")
        continue
    else:
        print("enter a valid operator")
        break
    print("Result is: ",result)
