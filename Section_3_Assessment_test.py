# Python Course from Udemy
# End of section 3
# Assessment test
# Date: 22.10.2021
# Author: Kamran Rashidov

# Write (or just say out loud to yourself) a brief description of all the following
# Object Types and Data Structures we've learned about.

# Numbers:
# Strings:
# Lists:
# Tuples:
# Dictionaries:




# NUMBERS

# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25
import math

print(100.25 - 10 / 2 + 12 * 2);
print(4 * (6 + 5)) # Answer: 44
print(4 * 6 + 5 ) # Answer: 29
print(4 + 6 * 5 ) # Answer: 34

result = 3 + 1.5 + 4
print(type(result)) # float

# What would you use to find a number’s square root, as well as its square?
number = 12
squareRoot = math.sqrt(number)
square = 12 ** 2 # Power of 2
print(squareRoot)
print(square)







# STRINGS

# Given the string 'hello' give an index command that returns 'e'.
# Enter your code in the cell below:
word = "hello"
print(word[1])

# Reverse the string 'hello' using slicing:
print(word[::-1])

# Given the string hello, give two methods of producing the letter 'o'
# using indexing.
print(word[4])
print(word[-1]) # the last letter






# LISTS
# Build this list [0,0,0] two separate ways.
list1 = [0, 0, 0]
print(list1)
list2 = [0] * 3
print(list2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
print(list3[2][2])
list3[2][2] = "goodbye"
print(list3[2][2])

# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)








# Dictionaries

d = {"key": "Hello", "model": "mustang"}
d2 = {"k1": {"k2": "Hi"}}
print(d.get("key"))
print(d["key"])
print(d2["k1"]["k2"])
# grab hello # combination of dictionary and list
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3["k1"])
print(d3["k1"][0]["nest_key"][1])




# TUPLES
# Tuples are ordered and unchangeable (immutable) and allow duplicate values.
# indexed!
tuple1 = ("banana", "orange")
# this is one item tuple
tuple2 = ("coconut",)
str1 = ("coconut") # this is not tuple!
print(type(tuple2))
print(type(str1))

print(tuple1)
print(tuple1[0])






# SETS
# no duplication

list7 = [1,2,2,33,4,4,11,22,3,3,2]
set2 = set(list7) # casting list to set
print(type(set2))
print(set2)





# BOOLEANS

print(2 > 3) # False
print(3 <= 2) # False
print(3 == 2.0) # False
print(3.0 == 3) # True
print(4**0.5 != 2.0) # False


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
kk = l_one[2][0] >= l_two[2]['k1'] # 3 < 4
print(kk)
print(l_one[2][0]) # 3
print(l_two[2]['k1']) # 4