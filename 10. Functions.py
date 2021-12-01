# Functions
# Kamran Rashidov
# 11.28.2021

def adding(num1, num2):
    print(num1 + num2)

def averageOfList(list):
    length = len(list)
    total = sum(list)
    av = total / length
    return av

adding(12, 24)

l = [2, 3, 4, 5, 6]
print(averageOfList(l))

def names(name1, name2 = "Kamran"):
    print("Firs name is: {} and {}".format(name1, name2))

names("Raschad")
names("Raschad", "Elvin")

