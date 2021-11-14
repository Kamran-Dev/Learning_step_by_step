# Chapter 6: Dictionaries
# Book: Python Crash Course
# Author: Kamran Rashidov
# Date: 26.10.2021
# Dictionaries work with key-values. No index, Key: Value, Changeable,


dict1 = {"name": "Kamran", "surname": "Rashidov", "age": "28"}
print(dict1) # print whole the dict
print(dict1["name"]) # print value
dict1["surname"] = "Mirzoyev"
print(dict1)
print(dict1.values())
print(dict1.keys())
print(dict1.items())
print(dict1.get("name"))
print(dict1)
print(dict1.pop("name"))
print(dict1)
# empty dictionary
alien_0 = {}
print(type(alien_0))
print(alien_0)
alien_0["color"] = "green"
alien_0["points"] = 5
alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["speed"] = "medium"
print(alien_0)

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print("X position of Alien is {}".format(alien_0["x_position"]))


# removing key value from dict
food = {"starter": "youghurt", "soup": "chicken", "main": "bbq"}
print(food.items())
del food["soup"]
print(food)





