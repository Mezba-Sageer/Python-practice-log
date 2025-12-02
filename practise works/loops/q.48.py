#048
# Ask for the name of somebody the user wants to invite to a party.
# After this, display the message "[name) has now been invited" and add 1 to the count.
# Then ask if they want to invite somebody else.
# Keep repeating this until they no longer want to invite anyone else to the party and
# then display how many people they have coming to the party.
name=input("Enter the name of the guest: ")
print(name,"has now been invited")
count=1
invite=input("Do you want to invite anyone else?(yes/no): ").lower()
while(invite=="yes"):
   if(invite=="yes"):
      name = input("Enter the name of the guest: ")
      print(name, "has now been invited")
      count += 1
      invite = input("Do you want to invite anyone else?(yes/no): ").lower()

print(count,"guests have been invited to the party")
