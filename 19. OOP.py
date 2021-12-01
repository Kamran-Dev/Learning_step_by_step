# Kamran
# OOP
# 11.30.2021

class Employee:
    # class variables
    salary_increase = 0.1
    number_of_employee = 0

    def __init__(self, name="Empty", surname="Empty", age=""):
        self.name = name
        self.surname = surname
        self.age = age
        Employee.number_of_employee = Employee.number_of_employee + 1

    def show_info(self):
        print("Name: {}, Surname: {}, Age: {}".format(self.name, self.surname, self.age))
        print("Salary increase from self: {}".format(self.salary_increase))
        print("Salary increase from employee: {}".format(Employee.salary_increase))

    def return_info(self): # instance method
        return "Name: {}, Surname: {}".format(self.name, self.surname)

    # class method decorator
    @classmethod
    def return_amount_of_employee(cls): # cls - class
        return cls.number_of_employee

    @classmethod
    def creat_obj(cls, name_surname):
        name, surname = name_surname.split("_")
        return Employee(name, surname)

    # staticmethod does not require any parameters like self or cls
    @staticmethod
    def say_hello():
        print("Hello World!")

    # set age of object
    @staticmethod
    def set_age(self, age):
        self.age = age
        print("Age settled for {} to {}".format(self, age))



    # static method decorator #staticmethod
    # does not require any parameter like cls or self




employee1 = Employee("Raschadat", "Mirzoyev", 33)
employee2 = Employee(surname="Agadadash")
employee3 = Employee("Koko")
employee1.salary_increase = 100

employee1.show_info()
print(employee1.__dict__)
print(employee2.__dict__)
print(Employee.__dict__)
print(Employee.number_of_employee)
print(employee1.return_info())
print(employee2.return_info())
print(Employee.return_info(employee3))
print(Employee.return_amount_of_employee())


employee4 = Employee.creat_obj("Kamran_Rashidov")
print(employee4.__dict__)

Employee.say_hello()
employee2.say_hello()
employee3.say_hello()
employee4.say_hello()
Employee.set_age(employee4, 44)
print(employee4.__dict__)