#Ask how many slices of pizza the user started with and ask how many slices they have eaten.
#work out how many slices they have left and display the answer in a user-friendly format.
total_pieces=int(input("Enter the total slices of pizza: "))
final_pieces=int(input("Enter the no.of pizza slices eaten: "))
balance=total_pieces-final_pieces
print("No.of pizza slices left",balance)


