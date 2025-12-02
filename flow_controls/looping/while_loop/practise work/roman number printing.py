#22.	Accept a number and print its Roman numeral form using loop logic.
num=int(input("enter a number: ")) #eg:58
roman=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman_value=""
for i in range(0,len(values)): #
    while(num>=values[i]): #58>1000F #58>900F #58>500F #58>400F #58>100F #58>90F #58>50T
                           #12>10T #2>1T #1=1T
        roman_value+=roman[i] #roman=X #roman=XI #roman=XII
        num-=values[i]        #12-10=2 #2-1=1 #1-1=0

print("The roman value is: ",roman_value)

