# Kamran
# For loop and While loop
# Date: 11.26.2021

num = range(0, 10)
print(num)
for n in num:
    print(n)

# while loop
k = 2
while k < 10:
    print(k)
    k += 2

# do while

# for loop with break

seasons = ["Summer", "Winter", "Autumn", "Spring"]
for ss in seasons:
    if ss == "Autumn":
        break
    else:
        print(ss)

# for loop with continue - skip

print("Exercise 04")
cars = ["Mercedes", "Kia", "Hyundai", "Ferrari", "BMW", "Honda"]

for c in cars:
    if c == "Kia":
        continue # skip bottom and go to the beginning
    elif c == "BMW":
        break
    else:
        print(c)

# print only 5, 10, 15

my_range = range(0,100)

for numm in my_range:
    if numm % 5 == 0:
        print(numm)