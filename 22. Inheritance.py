# Inheritance
# Kamran Rashidov
# 12.01.2021

class Auto:

    def __init__(self, color, year):
        self.color = color
        self.year = year


mercedes = Auto("Green", 2000)
hyundai = Auto("Blue", 2010)

print(mercedes.color)
print(hyundai.year)

