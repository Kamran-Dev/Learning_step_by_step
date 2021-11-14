# Chapter 9 - Classes
# Author: Kamran Rashidov
# Date: 03.11.2021

# Creating classes and using instances of classes
# Create a dog class

class Dog(): # name of a class is Capitalized: Dog
    """A simple attemt a model of a dog.""" # docstring describing what this class does.

# A function that’s part of a class is a method.
    def __init__(self, name, age):
        """Inititalize name and age attribute"""
        # Any variable prefixed with self is available to every method in the class, and we’ll also be
        # able to access these variables through any instance created from the class .
        self.name = name
        self.age = age
# Variables that are accessible through instances like this are called attributes.

    # sitting method of all dogs
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + "rolled over.")


my_dog = Dog("Willie", 7)
print(my_dog.name)
print(my_dog.age)