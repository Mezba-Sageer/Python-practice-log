# 072
# Create a list of six school subjects.
# Ask the user which of these subjects they don't like.
# Delete the subject they have chosen from the list before you display the list again.
subjects=['biology','physics','computer','chemistry','history','geography']
print(subjects)
dislike=input("Enter the subject you don't like: ")
subjects.remove(dislike)
print(subjects)