#10.	Find all 3-digit numbers whose digits are in ascending order.
for i in range(100,1000):
    hundreds=i//100 #this extracts the number at the 1st position
    tens=(i//10)%10 #this extract the digits at the middle position,
                    #i//10 extracts the first to digits and %10 extracts the last digit among the two hence we get the centre digit
    units=i%10 #used to extract the last
    if(hundreds<tens<units): #here w compare all three digits to see if the no.s frm 1st to last position is in ascending 
        print(i)
