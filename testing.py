class Human:
    salary = 42000
    current_year = 2021

    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
        now = 2021
        self.age = now - 1992

    def increaseSalary(self):
        Human.salary = Human.salary + 10000

    def setName(self, name):
        self.name = name


    def showAge(self):
        print(self.age)

    def getAge(self):
        return self.age

    def showName(self):
        print(self.name)

    def showYear(self):
        print(self.year)

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

# making instance of class Employee


human1 = Human("AAA", "A", 1)
human2 = Human("BBB", "B", 2)

list1 = [human1, human2]
set1 = {"u", "polo"}
tuple1 = ("Aba", "lolo", "koko", "gogo")
dict1 = {"name": "Rose", "age": 21}
print(type(tuple1))
print(type(list1))
print(type(set1))
print(type(dict1))
print(list1)
print(set1)
print(tuple1)
print(dict1)







