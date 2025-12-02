#Accept any city from the user and display monument of that city.
city=input("enter a city: ").lower()
if city=="agra":
    print("city:",city,"Monument: Taj Mahal")
elif city == "delhi":
    print("city:",city,"Monument: Red Fort")
elif city == "jaipur":
    print("city:",city,"Monument: Jal Mahal")
else:
    print("enter another city")

