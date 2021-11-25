# Tuples and Sets
# Author: Kamran Rashidov
# Date: 11.24.2021

# allows duplication, with indexes!
# modification is NOT allowed! no insert, no delete!
# Functions: len (length of tuple)

tuple_Names = ("Kamran", "Raschad", "Elvin", "Elvin")
print(type(tuple_Names))
print(tuple_Names)
print(tuple_Names[0])

# len() - gives the length of the tuple
print(len(tuple_Names))

# for loop




# sets
# NO duplication, NO index, NO order!
set1 = {"koko", "moko", "lolo", "choco", "toco"}
print(type(set1))
print(set1) # no ORDER! mixed everytime
print(len(set1))

# set with the for loop
for element in set1:
    print(element)

# add function, remove function,
set1 = {"koko", "moko", "lolo", "choco", "toco"}
set1.add("solo")
print(set1)
set1.remove("moko")
print(set1)

# remove and discard are the same. Discard does NOT give error!
set1.discard("huhu") # there is no huhu in set1. but discard does NOT give error
# sets - union, intersection, difference
set_A = {1, 34, 54, 55, 66, 88, 77}
set_B = {2, 22, 44, 55, 45, 54, 69}
print(set_A.union(set_B)) # union! no duplication
print(set_A.intersection(set_B)) # the same elements in both sets
print(set_A.difference(set_B)) # elements in A which is not in B
print(set_B.difference(set_A))

# in - True/False
print(22 in set_A) # False
print(22 in set_A.union(set_B)) # True

# create an empty list, tuple, set

list1 = []
list2 = list()
print(type(list1))
print(type(list2))
tuple1 = ()
tuple2 = tuple()
print(type(tuple1))
print(type(tuple2))
set11 = {}
print(type(set11)) # we wanted to create set but it is dictionary
set22 = set()
print(type(set22))


#
name = set("Kamran")
print(name)
surname = list("Rashidov")
print(surname)
address = tuple("Germany")
print(address)
