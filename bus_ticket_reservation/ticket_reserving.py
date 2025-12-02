routes = {
    'Kochi to Trivandrum': {'time': '08:00 AM', 'price': 300},
    'Kozhikode to Kochi': {'time': '01:30 PM', 'price': 450},
    'Trivandrum to Palakkad': {'time': '10:00 AM', 'price': 550},
    'Kochi to Bangalore': {'time': '09:00 PM', 'price': 900},}

route_lst=list(routes)
print("Welcome to Bus Ticket Reservation System")
print("Available routes: ")
print("-----------------------------")
count = 1
for i in routes:
    print(count, ":", "Route: ", i, "| Time: ", routes[i]['time'], "| Price: ", routes[i]['price'])
    count += 1

print("-----------------------------")

print("Please enter your Details")
while True:
    name = input("Please enter your name: ")
    if name !="":
        break
    else:
        print("Enter a valid name")

while True:
    age_txt = input("Enter your age: ")
    if age_txt.isdigit():
        age = int(age_txt)
        if 1 <= age <= 120:
            break
        else:
            print("Enter a valid age")

while True:
    ph_no = input("Enter your phone number: ")
    if ph_no.isdigit() and 7 <= len(ph_no) <= 15:
        break
    else:
        print("enter a valid number")

print("----------------------------")

while True:
    choice = input("Enter your number of choice of route(1/2/3/4): ")
    if choice.isdigit():
        option=int(choice)
        if 1 <= option <= len(route_lst):
            selected_option = route_lst[option-1]
            break
    else:
        print("Enter a valid choice")

seats=int(input("Enter your desired number of seats: "))
print("Which category do you belong to:\n "
      "1. Student\n"
      "2. Senior\n"
      "3. General\n")

cat=input("Enter the category(1/2/3): ")
if cat in ("1","2","3"):
    if cat=="1":
        category="Student"
    elif cat=="2":
        category="Senior"
    else:
        category="General"
else:
        print("Invalid choice")

departure=routes[selected_option]['time']
price=routes[selected_option]['price']

total_amt=price*seats
discount_rate=0.0

if category=="Student":
    discount_rate=0.15
elif (category=="Senior"):
    if age>60:
        discount_rate=0.20
    else:
        category="General"
        discount_rate=0.0
discount=total_amt*discount_rate
final_amt=total_amt-discount

print("-----------------------------")
print("  BUS TICKET - TRAVEL AGENCY  ")
print("-----------------------------")
print("Passenger name: ",name)
print("Phone number:   ",ph_no)
print("Age:            ",age)
print("Category:       ",category)
print("Route:          ",selected_option)
print("Departure Time: ",departure)
print("Seats booked:   ",seats)

print("------------------------------")

print("Ticket Price:   ",price)
print("Total amount:   ",total_amt)
print("Discount:       ",discount)
print("Final Amount:   ",final_amt)

print("------------------------------")

print("Thank you for booking with us!")
print("Have a safe journey,",name,"!")

filename="ticket"+name.replace(" ","")+ph_no+".txt"
f1=open(filename,"w")
f1.write("-----------------------------\n")
f1.write("  BUS TICKET - TRAVEL AGENCY \n ")
f1.write("-----------------------------\n")
f1.write("Passenger name: "+name+'\n')
f1.write("Phone number:   "+ph_no+'\n')
f1.write("Age:            "+str(age)+'\n')
f1.write("Category:       "+category+'\n')
f1.write("Route:          "+selected_option+'\n')
f1.write("Departure Time: "+departure+'\n')
f1.write("Seats booked:   "+str(seats)+'\n')
f1.write("------------------------------\n")
f1.write("Ticket Price:   "+str(price)+'\n')
f1.write("Total amount:   "+str(total_amt)+'\n')
f1.write("Discount:       "+str(discount)+'\n')
f1.write("Final Amount:   "+str(final_amt)+'\n')
f1.write("------------------------------\n")
f1.write("Thank you for booking with us!\n")
f1.write("Have a safe journey,"+name+"!"+'\n')
f1.close()