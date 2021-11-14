# Property Decorators - Getters, Setters, and Deleter

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        #self.email = first + "." + last + "@gmail.com"

    @property # by adding property we can call it as an attribute not a function
    def email(self):
        return self.first + "." + self.last + "@gmail.com"

    @property # access to the method as an attribute
    def fullname(self):
        return self.first + " " + self.last

    @fullname.setter
    def fullname_setter(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # deleter
    @fullname.deleter
    def fullname_deleter(self):
        self.first = None
        self.last = None
        print("Deleted")


emp1 = Employee("Tom", "Jerry")
emp1.first = "Michael"
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)

# currently we cannot set attribute fullname
# we have to make a setter for the fullname
emp1.fullname_setter = "Kamran Rashidov"
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.email)
del emp1.fullname_deleter
