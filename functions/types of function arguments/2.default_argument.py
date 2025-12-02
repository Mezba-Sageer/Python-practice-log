#eg of: default argument
def myfunct(name="mezba",place="Kochi",age=21):
    #place is added as a default here in the absence
    #of entering any values while calling the function, this acts as the default value
    #when no separate value is passed while calling
    print("name: ",name)
    print("place: ",place)
    print("Age: ",age)
myfunct()

