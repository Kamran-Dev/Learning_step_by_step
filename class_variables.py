# Class variables

class Car:
    brand = "Mercedes"
    number_of_cars = 0

    def __init__(self, color, year):
        self.color = color
        self.year = year
        Car.number_of_cars += 1

    def show_color(self):
        print(self.color)

    def show_year(self):
        print(self.year)


car1 = Car("Black", 2010) # instance
car2 = Car("Green", 2020) # instance
car3 = Car("Yellow", 2012)


car1.show_color()
car1.show_year()

print(car1.brand) # Instance car1 shows brand through the class Car
print(car1.__dict__) # car1 is instance which has not class variable
print(car2.__dict__)
print(Car.__dict__) # brand is a class variable and it belongs to the class
car1.brand = "Kia"
print(car1.brand) # it print new assigned variable of car1 instance.
print(car2.brand) # it did not change, cause it prints variable through the class
print(Car.brand) # it did not change, cause it prints Class variable
print(Car.number_of_cars) # 3 instances created from the Car Class