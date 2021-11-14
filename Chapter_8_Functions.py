# Chapter 8: Functions
# Book: Python Crash Course
# Author: Kamran Rashidov
# Date: 31.10.2021

# defining the function and giving it parameter
def say_Hello(username):
    '''Display Simple Greeting.''' # docstring for documentation of the function
    print("Hello {}".format(username)) # body of the fuction

# calling the function

say_Hello("Kamran") # argument: Kamran




# positional arguments

def describe_pet(animal_type, animal_name):
    '''Display information about a pet'''
    print("Type is: {}".format(animal_type))
    print("Name is: {}".format(animal_name))

describe_pet("Dog", "Toplan")
describe_pet("Cat", "Mesi")
# keyword arguments, the order does not matter in key word
describe_pet(animal_type="snake", animal_name="pis-pis")
describe_pet(animal_name="don-don", animal_type="donkey")

# default values for the parameter.
# provide argument for the parameter in the function
print("******** DEFAULT VALUE **************")
def animal_pet(animal_name, animal_type="dog"): # order!
    '''Display info about the animal.'''
    print("Name of animal is {}.".format(animal_name))
    print("Type of the animal is {}.".format(animal_type))

animal_pet("kuku")
print("\n")
animal_pet("muku", "frog")
print("\n")
animal_pet(animal_type="horse", animal_name="polo")
print("\n")
animal_pet(animal_name="yuyu", animal_type="bunny")


# function with return value
def return_fullname(first_name, last_name):
    """return full name"""
    full_name = ("{} {}".format(first_name, last_name))
    return full_name.title() #Uppercase

full_name = return_fullname("kamran", "rashidov")
print(full_name)

# adding two numbers with function
def adding_function(num1, num2):
    return num1+num2

print(adding_function(23,34))

# MAKING AN ARGUMENT OPTIONAL = EMPTY
def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        print(first_name, middle_name, last_name)
    else:
        print(first_name, last_name)

get_formatted_name("Kamran", "Rashidov")
get_formatted_name("Kamran", "Rashidov", "Middle")





# RETURNING A DICTIONARY WITH OPTIONAL ARGUMENT
def get_dict_fullname(first_name, last_name, age = None):
    # none is a spaceholder

    if age:
        person = {"first name": first_name, "last name": last_name, "age":age}
    else:
        person = {"first name": first_name, "last name": last_name}

    return person

print(get_dict_fullname("Kamran", "Rashidov", 123))


# write a function with a while loop and input

def newFunction(first_name, last_name):
    name1 = "{} {}".format(first_name, last_name)
    return name1




"""
while True:
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    if name and surname:
        break

get_name = newFunction(name, surname)
print("Hello {}".format(get_name))

"""









# exercise
def city_country(city_name, country_name):
    city_country = ("{}, {}".format(city_name, country_name))
    return city_country

cn = city_country("Baku", "Azerbaijan")
print(cn)
print(city_country("Berlin", "Germany"))
print(city_country("Paris", "France"))
print(city_country("Barcelona", "Spain"))

"""
# exercise 
def makeAlbum(artist_name, album_title, number_of_tracks = None):

    if number_of_tracks:
        album = {"artist name": artist_name, "album title": album_title, "number_of_tracks": number_of_tracks}
    else:
        album = {"artist name": artist_name, "album title": album_title}
    return album

al = makeAlbum("Faiq", "Aldatdi meni", 132)
print(al)

while True:
    artist = input("Enter a name of artist")
    album = input("Enter a name of album")
    if artist and album:
        break
print(makeAlbum(artist, album))
"""

# Exercise: List with functions

my_names = ["Kamran", "Rashidov", "Mario", "Ivanov", "Orkhan"]
confirmation = [] # empty lsit

while my_names:
    confirmed = my_names.pop()
    print("Name {} is done!".format(confirmed))
    confirmation.append(confirmed)

print("Result: {} ".format(confirmation))

# copying the lists and proving it with append

list1 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []


list2 = list1[:] # copying the list1 to list2
print(list2)
list1.remove(1)
print(list1)
print(list2)

print("*****************")
# function to copy the lists from list1 into list2
def list_copy(list1, list2):
    while list1:
        element = list1.pop()
        list2.append(element)
    return list2

list3 = [23, 34, 56, 72, 15, 55, 62]
list4 = ["abc"]

# here we giving the copy of the list3 to the function. So we can protect the original list
list_copy(list3[:], list4)

def list_print(list5):
    for element in list5:
        print("Value is: {}".format(element))

#list_print(list3)
list_print(list4)
print(list3)

# Exercise: Passing an Arbitrary Number of Arguments

def cars(*brand):
    print(brand)

cars("Mercedes", "BMW", "Nissan", "Hyundai", "VolksWagen")
