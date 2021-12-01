# 06. If_elif_else
# Author: Kamran Rashidov
# Date: 11.25.2021

active = "Elvin"

if active == "Kamran":
    print("Hi Kamran")
elif active == "Elvin":
    print("Hi Elvin")
else:
    print("No one")

a = 2
b = 5

if a < b:
    print("B")
elif a == b:
    print("bb")
else:
    print("gggg")

# in
nums = [23, 54, 6, 65, 7, 9, 94, 56]
if 5 in nums:
    print("yes")
else:
    print("nooo")

# in with string
name = "Raschad"
letter = "c"

if letter in name:
    print("c in Raschad")
else:
    print("no there is no")

# or, and

# is

k = "Kamran"
n = "Kamran"
r = "Kamra"
r = r + "n"
l = r
n = n + "lola"

print(id(k))
print(id(r))
print(id(n))
print(id(l))
