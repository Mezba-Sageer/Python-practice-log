#Ask the user to enter their favourite colour. If they enter "red", "RED" or
#"Red" display the message "I like red too", otherwise display the message
#"I don't like [colour],I prefer red".
red=input("Enter your favourite color: ")
if(red=='red')or(red=='RED')or(red=='Red'):
    print("I like red too")
else:
    print("I don't like",red,"I prefer red")

