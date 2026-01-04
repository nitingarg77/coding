# collection is single variable used to store multiple values
# list, tuple, set, dictionary are types of collections
# list is ordered, changeable, allows duplicate members
# tuple is ordered, unchangeable, allows duplicate members
# set is unordered, unindexed, no duplicate members

fruits = ["apple", "banana", "cherry"]  # list

for fruit in fruits:
    print(fruit, end="-")


print(help(fruits))  # shows all attributes and methods of list object