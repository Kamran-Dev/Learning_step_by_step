# Statements
# if, elif, else
# for loops
# while loops

hungry = True
ffs = False


if (19 < 10):
    print("Hello World")
elif (12 > 99):
    print("koko")
else:
    print("nii")

location = "Bank"

if (location == "Auto Shop"):
    print("Nice cars!")
elif (location == "Bank"):
    print("Give money!")
else:
    print("lolo")

my_itterable = [12, 42, 53, 14, 98, 41]
for elements in my_itterable:
    print(elements)

print("check for the even numbers")
for elements in my_itterable:
    if(elements % 2 == 0):
        print("even {}".format(elements))
    elif(elements % 2 == 1):
        print("odd {}".format(elements))

# sum of the number
list_sum = 0

for elements in my_itterable:
    list_sum = list_sum + elements

print(list_sum)

# iterate the characters in string
for letter in "Hello World":
    print(letter)

# list with for loop
# List works with index, changeable, allows duplication, ordered
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
ko = list([2, 4, 5, 5, 6, 9])
print(type(list1), type(ko))
k = 0
for el in list1:
    print(el)
    k = k + el
print("Sum is {}".format(k))



# tuple in the list
# Tuples are works with index, unchangeable, allows duplication, ordered
tuple1 = (12, 12, 32, 32, 44, 52, 14)
print(type(tuple1))
list2 = [(1, 2), (2, 3), (4, 5)]
for t in list2:
    print(t)
# tuple unpacking
for (a, b) in list2:
    print(a)
    print(b)

# Sets are unordered, no duplication, no index, no change
set1 = {1, 1, 23, 43, 12, 14, 15, 16, 17, 18, 19, 20}
x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
y = set(("op", "op", "bup"))
print(set1)
print(type(x),type(y),type(set1))

for ko in set1:
    print(ko) # as we can see there is no order in set



# Dictionary is a collection which is ordered* and changeable.
# No duplicate members.
dic1 = {"color": "black", "length": 3, "width": 4}
print(type(dic1))
x = dict([("car", "toyota"), ("door", "back")])

MLB_team = dict(
     Colorado='Rockies',
     Boston='Red Sox',
     Minnesota='Twins',
     Milwaukee='Brewers',
     Seattle='Mariners'
)


req_list = ["mushrooms", "banana", "orange"]
print("mushrofoms" not in req_list)

for fruits in req_list:
    if fruits == "banana":
        print(req_list[1].upper())
    else:
        print(req_list)

house = "wohnung"
print("I think it should be: {}".format(house == "wohnung"))


age = 18
if (age <= 4):
    print("Admission is free")
elif (age > 4) and (age < 18):
    print("Admission is 25 EUR")
else:
    print("35 EUR! ")


# testing multiple conditions with series of if statements

ing = ["salami", "peperoni", "chicken", "salt"]
if "salami" in ing:
    print("Salami added!")
if "chicken" in ing:
    print("Chicken added")


# alien colors exercise
alien_color = "red"
if alien_color == "green":
    print("5 points")
elif alien_color == "yellow":
    print("10 points")
elif alien_color == "red":
    print("15 points")

# stage of life exercise
person_age = 65

if (person_age < 2):
    print("baby")
elif(person_age >= 2) and (person_age < 4):
    print("toddler")
elif(person_age >= 4) and (person_age < 13):
    print("kid")
elif(person_age >= 13) and (person_age < 20):
    print("teenager")
elif(person_age >= 20) and (person_age < 65):
    print("adult")
elif (person_age >= 65):
    print("elder")



# favourite foods
fav_food = ["brezel", "yoghurt", "doner", "kebab"]
if "brezel" in fav_food:
    print("Yes I like Brezel")
if "doner" in fav_food:
    print("Yes I like doner")

# I like pizza
fav_pizzas = ["margaritta", "havayi", "sucuk"]
for pizzas in fav_pizzas:
    print("I like {} pizza".format(pizzas))
print("Yes I love pizza")

# favourite animals
fav_animals = ["cat", "dog", "rabbit", "fish"]
for animals in fav_animals:
    print("I like {} very much".format(animals))
print("all animals are very good")

numbers = range(1, 100, 2)
for number in numbers:
    print(number)
sum_numbers = sum(numbers)
min_num = min(numbers)
max_num = max(numbers)
print(sum_numbers, min_num, max_num)

print("cube exercise")
# cubes
cube = range(0, 11)
for numb in cube:
    print(numb ** 3)
# list compeherision
print("list com.")
cubes = [value ** 3 for value in range (0,11)]
print(cubes)

# tuples
tuple_of_food = ("doner", "kebab", "ayran")
print(tuple_of_food)
print(tuple_of_food[0])
#writing over the tuple
tuple_of_food = ("ketchup", "kebab", "ayran", "smit")
print(tuple_of_food)
for food in tuple_of_food:
    print(food)


# lists combine if statement

list_of_cars = ["Mercedes", "Porsche", "BMW", "Honda", "KIA"]
print("Cars in the list: {}".format(list_of_cars))

for cars in list_of_cars:
    print("I like to drive {}".format(cars.upper()))
print("I like all the cars but my fav car is {}.".format(list_of_cars[0]))

if "Mercedes" in list_of_cars:
    print("{} is really great car to drive.".format(list_of_cars[0]))
if "Honda" in list_of_cars:
    print("{} is also a great car!".format(list_of_cars[3]))

# checking for the special item in a list
ingredients = ["mushroom", "green peppers", "extra cheese"]
for ing in ingredients:
    if ing == "green peppers":
        print("Sorry we do not have green peppers")
    else:
        print("You are added {} to your pizza!".format(ing))
print("Pizza is ready")

#checking that a list is not empty

print(" ----------------------------- ")

requested_things = []# empty list
if requested_things: # checks if the list contain at least one item
    for things in requested_things:
        print("Adding {}".format(things))
    print("Finished making your pizza!")
else:
    print("Nothing added to your pizza. Plain Pizza?")

# using multiple lists
print("-------------------------")

print("********")
listOfAvailables = ["mercedes", "toyota", "kia", "bmw", "ferrari", "porsche"]
listOfDemand = ["Mazda", "toyota", "Audi", "Bentley"]

for demand in listOfDemand:
    if demand in listOfAvailables:
        print("{} is in your garage!".format(demand))
    else:
        print("Sorry no {}".format(demand))
print("Mission is completed")


# Exercise from book: 5.8, 5.9, 5.19, 5.11
print(" ------------------------------")


listOfNames = ["Jack", "Rose", "Admin", "Shelly", "Jelly"]

if len(listOfNames) == 0:
    print("we need to find someone")
else:
    for names in listOfNames:
        if (names == "Admin"):
            print("Hi {}".format(names))
        else:
            print("Hello {}".format(names))

# checking available usernames in website

current_usernames = ["jeck", "mario", "orkhan", "lodhi", "kamran"]
new_usernames = ["nino", "mimo", "Mario","tino", "Lodhi"]

for newNames in new_usernames:
    if newNames.lower() in current_usernames:
        print("The name {} is taken.".format(newNames))
    else:
        print("Name {} is available".format(newNames))


# ordinal numbers 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th

listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in listOfNumbers: # looping the list
    if number == 1:
        print(" 1st ")
    elif number == 2:
        print(" 2nd ")
    elif number == 3:
        print(" 3rd ")
    else:
        print(" {}th ".format(number))