#string concatenation using '+' operator
str1="Python"
str2="Programming"
print(str1+str2)

#using join()
x="Luminar"
y="Technolab"
print("".join([x,y])) #prints without space since it's not there btw double quotes
print(" ".join([x,y])) #prints with space since there's space btw double quotes
print("_".join([x,y]))

#using '%' operator
a="hello"
b="welcome"
print("%s%s" %(a,b))
print("%s_%s" %(a,b))
print("%s***%s" %(a,b))
print("%s %s" %(a,b))


#using format()
p="Hello"
q="Mezba"
r="Sageer"
print("{}{}".format(p,q))
print("{} {} {}".format(p,q,r))
print("{}_{}_{}".format(p,q,r))


#using ','or comma
print(p,q,r)
