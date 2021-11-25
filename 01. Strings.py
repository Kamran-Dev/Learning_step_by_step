# Strings
# Author: Kamran Rashidov
# Date: 11.18.2021

name = "Kamran"
country = "Germany"
print(name)
print("My name is {}.".format(name))
print(f"I live in {country}.")
print(name * 4)
print(name + " " + country)
print(name.upper())
print(name.lower())
print(name.capitalize())

print(name[::-1])
print(name[0]) # index
print(name[-2])
print(name[0:4]) # start:stop:step
print("Hello \tWorld!")
print("Hello \nWorld")
print("""Hello My name is Kamran,
and yours?""")
print("My name is "
      "Kamran")
print(len(name))
print(len(country))
print(len(name + country))

print(name.startswith("Ka")) #True
print(name.endswith("lo")) #False