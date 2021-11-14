# Chapter 7: User input and While loops
# Book: Python Crash Course
# Author: Kamran Rashidov
# Date: 27.10.2021

# USER INPUT


message = input("Tell me your name, please.")
print("Hello, {}".format(message))


prompt = ("Tell me who are you?")
message1 = input(prompt)
print("Hello Mr/Ms {}".format(message1))


# accept numerical input and casting it to int
prompt2 = ("Give your age, if you want to enter!")
message2 = input(prompt2)
print("Numerical input type is: ".format(type(message2)))
casted = int(message2)
print("After casting str to int, type is: {}".format(casted))
print(type(casted))

if (casted >= 18):
    print("You are Welcome!")
elif (casted < 18 and casted >= 16):
    print("Need ID card!")
else:
    print("Please, go home!")

print("End of the task!")


# check even or odd numbers

entered_Number = input("Please enter the number: ")
entered_Number = int(entered_Number)

if (entered_Number % 2 == 0): # if the modulo of number is zero (qaliq)
    print("Even number!")
else:
    print("Odd number!")


# Exercise: 7.1, 7.2, 7.3

message23 = input("Please enter the number")
message23 = int(message23)

if (10 % message23 == 0):
    print(" it is the multiple of 10")
else:
    print("no!")




# WHILE LOOPS

message123 = "" # empty string. cause Python should compare it in while loop with quit
while message123 != "quit":  # it compares empty string with "quit" it is not equal
    message123 = input("Say something") # take input to message

    if (message123 != "quit"): # check the input is quit or not
        print(message123)           # if not then print message

print("Task Parrot ended! {}")


# while loop with boolean and with break

active = True
while active:
    mess = input("Enter please:")

    if (mess == "quit"):
        break # break the while loop
    else:
        print(mess)


# using the break in the for loop

myList = ["toyota", "mercedes", "bwm", "kia", "ferrari"]

for car in myList:
    print("This is my lovely {}".format(car))

    if (car == "bwm"):
        break # breaking the loop with the break
print("end of the task")


# using continue in a while loop, print odd numbers
# continue - ignore the rest of the code start from beginning

num1 = 0
while num1 < 10:
    num1 = num1 + 1

    if num1 % 2 == 0:
        continue # ignore the rest, start from beginning
    print("Odd numbers: {}".format(num1))


# movie ticket pricing by age

movieTicket = input("Enter your age: ")
movieTicket = int(movieTicket)
if (movieTicket <= 3):
    print("Ticket is FREE")
elif (movieTicket > 3 and movieTicket <= 12):
    print("10 EUR")
elif (movieTicket > 12):
    print("15 EUR")

print("thanks")

# While loop with list
# Remove all instance of specific values from a list

pets = ["dog", "cat", "bunny", "frog", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)


# While loop with dictionary
# Filling dictionary with user inputs
responses = {}

case = True

while case:
    name = input("What is your name?")
    response = input("What is your car brand?")

    responses[name] = response

    repeat = input("Do you wanna continue?")
    if repeat == "no":
        break

print(responses)

# moving items from one list to another list
unconfirmed_users = ["Kamran", "Mamed", "Orkhan", "Mario", "Koko"]
confirmed_users = [] # empty list

print(unconfirmed_users)
print(confirmed_users)

while unconfirmed_users: #while it is full
    current = unconfirmed_users.pop() # pop from the last inserted
    print("Verified users: {}".format(current))
    confirmed_users.append(current)

print(unconfirmed_users)
print(confirmed_users)

# Exercise 7-8 and 7-9 - moving elements from one to another list

sandwich_orders = ["pastrami", "beef", "pork", "pastrami", "chicken", "salami", "vegan", "vegetarian", "pastrami"]
finished_sandwiches = []

print("Deli has run out of pastrami!")
print("Orders of sandwiches: {}".format(sandwich_orders))

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != "pastrami":
        print("I made for you {} sandwich".format(sandwich))
        finished_sandwiches.append(sandwich)
print("Finished: {}".format(finished_sandwiches))