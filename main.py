# For loops in Python
# Udemy course
# Section 5: Python Statements

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in myList:
    if number % 2 == 0:
        print("Even number: {}".format(number))
    else:
        print(number)

list_sum = 0
for numb in myList:
    list_sum = list_sum + numb

print(list_sum)

my_name = "Kamran Rashidov"

for letter in my_name:
    print(letter)

# tuples with for loop - iterate through the tuple

my_tuple = ("koko", "moko", "shoko", "lolo")
print(type(my_tuple))
for words in my_tuple:
    print(words)

# tuple unpacking

listOfTuple = [("K", "a"), ("m", "r"), ("a", "n"), ("R", "a"), ("s", "h"), ("i", "d"), ("o", "v")]

for (a, b) in listOfTuple:
    print(a)
    print(b)

# iterate through the dictionary
# dictionaries are unordered!
dict1 = {"Name": "Kamran", "Surname": "Rashidov"}
print(type(dict1))
for values in dict1.values():
    print(values)


# while loops
# break - Break out of the current closest enclosing loop
# continue - Return to the beginning of closest enclosing loop
# pass - do nothing ! Empty!

list2 = [12, 34, 51, 77, 88, 99, 1000]
for n in list2:
    if n == 77:
        continue # go to the top of the closest enclosing loop
    print(n)


num1 = 1
while num1 < 7:
    #if num1 == 4:
     #   break # stop! break the loop
    print(num1)
    num1 = num1 + 1
else:
    print("stop")


# generating the information instead of saving it to the memory
list3 = [23, 14, 17, 18, 19]

# start, stop, range
# docstring
# range(stop), range(start, stop, range)
for num in range(5, 11, 2):
    print(num)

print(list(range(0, 100, 2))) # generating the list of numbers


# enumerate function returns in tuple form
word = "Kamran"

for letter in enumerate(word):
    print(letter)

season = ["Winter", "Spring", "Summer", "Autumn"]
t = list(enumerate(season))
print(t)

# zip function, pairing data
# zip() returns an iterator of tuples
print("Zip function!")
names = ["Kamran", "Mario"]
surnames = ["Rashidov", "Ivanov"]
fullname = zip(names, surnames)
print(type(fullname))
for f in fullname:
    print(f)

# shuffle function is returning nothing, its inplace function.
# first we have to import shuffle from built-in random library
from random import shuffle


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list
print(x)
shuffle(x)
print(x)



# nested for loop
empty = []

for a in [12, 23, 14]:
    for b in [2, 3, 4]:
        empty.append(a * b)
print(empty)