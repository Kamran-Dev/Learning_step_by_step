# Integer, float - numeric data types
# Author: Kamran Rashidov
# Date: 11.19.2021

age = 29
weight = 75.5
print(type(age))
print(type(weight))
number = 2
print(2**3) # 3 power of 2
print(121**(1/2)) # square root of 9
print(17/5)
print(17//5)
print(17 % 5)
print(abs(-19)) # absolute value
print(round(99.445635, 3)) # round, three digit

print(5 == 5)# True
print(6 <= 3) # False
print(7 >= 4) # True
print(19 != 20) # True, they are not equal
print(1 < 3)
print(34 > 9)


# Casting
units = "1000"
apples = 1000
print(type(units))
print(units == apples)
print(int(units) == apples) #after casting
flight = int(7.2) #casting float to integer
print(flight)
print(type(flight))
flight = str(flight) # casting integer to string
print(type(flight))