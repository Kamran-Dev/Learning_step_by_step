# Test from youtube
# 05.11.2021
# Kamran Rashidov

"""

class Employee:
    r_amount = 1.04
    number_emp = 0


    # constructor of Employee Class
    # we have here instance variables
    def __init__(self, first, last, pay): # arguments
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmbh.com"
        Employee.number_emp = Employee.number_emp + 1
        #self.email = first,last

    def full_name(self): # we are passing self as an argument. instance of class
        print("{} {}".format(self.first, self.last))

    def apply_raise(self):
        self.pay = self.pay * self.r_amount

# let's create objects from this class
# instances of class


emp1 = Employee("Bob", "Marley", 50000)
emp2 = Employee("Jonny", "Dep", 70000)

print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.email)
print("{},{}".format(emp1.first, emp1.last))
emp1.full_name()
emp2.full_name()

Employee.full_name(emp1) #we have to pass instance of class as an argument
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print("**********")
Employee.r_amount = 333
print(emp1.r_amount)
print(emp2.r_amount)
print(Employee.r_amount)
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

emp1.r_amount = 444 # it will change only for emp1! not for all
print(emp1.r_amount)
print(emp2.r_amount)
print(Employee.r_amount)

# number of employees # number of instances
print(Employee.number_emp)

"""







# class name Capital letter
class Employee:
    # Class variable
    raise_ = 1.04
    number = 0

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        Employee.number = Employee.number + 1

    def show_name(self):
        print(self.firstname)

    def get_salary(self):
        return self.pay

    def get_fullname(self):
        return self.firstname + "." + self.lastname

    def increase_salary(self):
        return self.pay * self.raise_

# creating instance of class
emp1 = Employee("Kamran", "Rashidov", 12345)
emp1.show_name()
Employee.show_name(emp1) # if we want to run the method through the class we have to give instance


# Class methods
