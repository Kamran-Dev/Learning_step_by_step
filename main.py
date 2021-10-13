import math


# integer
age = 12;
print(age, type(age));

# str - String
name = "Kamran ";
print(name, type(name));

# multiple assignments
weight = height = size = 34;
print(weight);
print(height);

# String methods
fullName = "Kamran Rashidov";
surname = "Rashidov"
print(len(name));
print(len(surname));
print(len(name) + len(surname));
print(name.find("m")); #finds by index, returns integer
print(type(name.find("m")));
print(name.capitalize()); #capitalize only the first letter of first word
print(name.upper()); # make whole the word upper case
print(name.lower()); # make whole the word lower case
print(name.isdigit()); # checks is it digit or not, return false or true
print(name.isalpha()); # checks is string contains only alphabetical
print(fullName.count("a")); # count how many letters in the string
print(fullName.replace("a","o"));
print(name * 3); # display the string three times

# Type casting
x = 12; # int
y = 2.4; # float
z = "4567"; #str

y = (int)(y); # casting
print("x is: " + (str)(x)); #string concatination
print(y * 2);
print(z * 2);

# Python user input
#name = input("Hello, what is your name? ");
#print("Hello " + name + ". Nice to meet you");
#age = input("How old are you? ");
#print("You are " + age + " years old.");
#print(type(age));
#age = (int)(age);
#age = age + 1;
#print("After 1 year you will be " + (str)(age) + " years old!");

# Math Functions
print("Math Functions.")
pi = 3.14;
a = -3;
b = 121;
c = 1;
print(round(pi));
print(math.ceil(pi)); # rounding up
print(math.floor(pi)); # rounding down
print(abs(a)); # absolute value
print(pow(a,2)); #power of a
print(math.sqrt(b)); # square root of b
print(max(pi, a, b)); #find the maximum value
print(min(pi, a, b)); #find the minimum value
print(math.log10(c)); #logarithma

# String Slicing
print("String Slicing");

# if/else if statements

age = input("How old are you?: ");
aga = int(age);

if(int(age) > 18):
    print("You are adult")
elif (int(age) < 18):  #elif = else if
    print("Not adult!")
else:
    print("you are 18!")


# Logical operators