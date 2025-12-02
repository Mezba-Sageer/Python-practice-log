#wite a program that uses continue, ver see fewers in a list While printing the rest.
words=["apple","banana","cherry","date","elderberry"]
skip_words = ["banana", "date"]
f1=[i for i in words if i not in skip_words]
print(f1)