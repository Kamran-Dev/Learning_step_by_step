# Lists
# Author: Kamran Rashidov
# Date: 11.19.2021
# Duplication is allowed, with indexes,
# Methods: append, insert, remove, del, len, extend, pop, reverse, sort, sorted
# Methods: mean, max, sum, enumerate, in (True/False), list to string - join method
# Methods: string to list split method
# print through for loop





# print list through for loop
names = ["Kamran", "Mario", "Reeza"]
nums = [1, 23, 45, 65, 75, 49, 55, 66]
numbers = range(0, 10)
for name in names:
    print(name)
for number in numbers:
    print(number)


# append - add the element into the end of the list
names.append("Rio")
# insert - insert the element to the list with index
names.insert(0, "Kamran")
print(names)

# remove the element from the list
names.remove("Kamran")
del names[0]
del names[0]
del names[0]
del names[0]
print(names)
names.insert(0, "lolo")
names.append("Kopolo")
print(names[1])
print(len(names))
cars = ["Ferrari", "Audi", "Mercedes", "Kia", "Hyundai", "BMW"]
print(cars[1:2]) # start, stop, step
cars2 = ["Chrysler", "Bugatti", "VW"]
cars.extend(cars2) # Extend the list by appending elements from the iterable
print(cars)
print(cars.pop())
print(cars)
print(cars.pop()) #takes out the last element of the list
print(cars)
cars.reverse()
cars.sort()
print(cars)
sorted_cars = sorted(cars)

# min, max, sum
ages = [23, 55, 22, 66, 89]
print(min(ages))
print(max(ages))
print(sum(ages))

# enumerate function
# Enumerate() method adds a counter to an iterable and
# returns it in a form of enumerating object.
# This enumerated object can then be used directly for loops or
# converted into a list of tuples using the list() method.

programs = ["Word", "Excel", "Outlook", "PowerPoint", "Onenote", "Access"]
print(programs)
en = enumerate(programs) # created enumerate obj
print(type(en))
en_list = list(en) # obj enumerate casted to list
for e in en_list:
    print(e)
print(type(en_list))
print(en_list)
print("Excel" in programs) # True

stringFromList = ",".join(programs) # join all the elements of list into the string
print(stringFromList)

sw = stringFromList.split(",") # split the string into list
print(sw)
