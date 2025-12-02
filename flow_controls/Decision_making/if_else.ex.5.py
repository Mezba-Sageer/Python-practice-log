#if attendance less than 75% will not sit for exam
#get no.of classes held
#get no.of classes attended
#print percentage of classes attended
#and if the kid is allowed to sit

num_of_classes=int(input("Enter the no.of classes held: "))
atnd_classes=int(input("Enter the number of classes attended: "))
atndnc_prcnt=(atnd_classes/num_of_classes)*100
print("Your attendance percentage is",atndnc_prcnt)
if(atndnc_prcnt>=75):
    print("You're allowed to attend the exam")
else:
    print("You're not allowed to attend the exam")


