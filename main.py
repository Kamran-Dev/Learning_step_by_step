# Python course on Udemy
# 2021 Complete Python Bootcamp From Zero to Hero in Python
# Number

print(3 + 3);
print(3 - 4);
print(3 * 5);
print(15 / 3);
print(7 / 4);
print(7 % 4); # modulo or mod operation
print(50 % 10);
print(2 ** 3); # 2 power of 3 = 8
print(1/8);
print(0.3 + 0.33 + 0.333);

print(0.1+0.2-0.3);
print(1/2); # 1/2 = 0.5

# Dynamic typing in Python

age = "Hello";
age = 12;

print(type (age));
print(age);


weight = 79;
height = 177.5;
surname = "rashidov";
atHome = True;
fullname = "Kamran Rashidov";

print("My surname is " + surname + ".\nMy height is " + (str)(height) + " m.\nMy weight is " + (str)(weight));
print(type(surname))
print(surname.upper());
print(surname.lower());
print(surname.capitalize());
print(len(surname)); # length of the string, number of characters (rashidov = 8)
# String indexing
print(surname[0]); # indexing index 0 is r
print(surname[3]); # index 3 is h
print(surname[-2]);
print(surname[2:]) #start from 2nd index
print(surname[:2]) #print index 0 and 1. NOT include index 2
print(surname[2:5]) #print index 2,3,4
print(surname[::2]); # print from beginning to the end but with jumping 2 step size
print(surname[::-1]) #reverse the string

# strings are immutable, you cannot change them! unchangeable;
# surname = rashidov
tt = surname[1:]
print("K" + tt ); # string concatenation
print(surname*3) # print string 3 times in a row
print(tt.upper());

#splitting strings
word = "Hello my name is Kamran";
print(word.split()); #normal splitting #create a list out of string
print(word.split("i"));

word2 = "Apple, Kiwi, Pineapple, Cake, Banana";
print(word2);
print(word2.split(",", 2)); #split 2 out of the given string

#print formatting with string
w = "I live in Hamburg. I am {}"
age = 28;

print(w.format(age));
print(word + ". I am 28."); # java style string formatting
print("Hello {}".format(word));
print("{z} I am 28. {y}".format(y = "Thanks!", z = "I am at home."));
print("Hello.{0} {1} {0}".format("My surname is Rashidov.", "and what is yours?")) #with indexes
print(f"Hello {word2}"); #new style with Python3.6

result = 100/77;
print(result);
print("Result is: {:12.4f}".format(result))  #"{value:width.precision f}"


# # # # # # #
print("\n * * * * * * * * LISTS IN PYTHON! * * * * * * * * \n")
# # # # # # #

myList = [14, 21, 32, 42, 57]; #list with the same data type
difList = ["Hello", 3, 12.4, False]; #list with the different data type
charList = ["e", "q", "t", "b","y", "o", "l","a"];
print(myList[1]); #with index
print(myList[1:]) #slicing
print(len(myList)); #length of the list
print(difList[3]); #print with index
newList = myList + difList; #mergin the list
print("New List: {}".format(newList))
print(newList * 2) #printing multiple times
myList[1] = 123; #Links are mutable. Strings are immutable
print(myList)
myList[4] = myList[2] + myList[3];
print(myList)
myList.append(999) #add element to the end of list
print(myList)
print(myList.pop(4)) #remove and return the element by index #by default the last element will be removed
myList.sort() #sorting the index
print(myList)
print(charList)
newL = charList.sort()
print(charList)
print(type(newL))
nkList = [1, 3, 4, [23, 45, 67]] #nested list
print(nkList[3][1]) # third element is list, and first element of the nested list = 45




# # # # # # #
print("\n * * * * * * * * DICTIONARY * * * * * * * * \n")
# # # # # # #

# Dictionaries are mappings and do not retain order!
# If you do want the capabilities of a dictionary but you would like ordering as well,
# check out the ordereddict object lecture later on in the course!
# Dictionaries are mutable as like lists. Strings are immutable


#based on keys and values
myDict = {"a":"Hello", "b":"World", "CC":"Thanks"};
print(myDict["a"])
print(myDict["b"])
print(myDict["CC"])
intDict = {"a": 12, "b":234.456, "c":False}
print(intDict["c"])

Dict = {"d": ["a", "b", "c"]}
print(Dict["d"]);
dt = Dict["d"][2]
print(dt.upper())
print(Dict)
Dict["K3"] = 234; #assigning new value to the dictionary
print(Dict)
Dict["K3"] = 678 #overwrite
print(Dict)
print(Dict.keys()) #print keys
print(Dict.values()) #print values
print(Dict.items()) #


# # # # # # #
print("\n * * * * * * * * TUPLES * * * * * * * * \n")
# # # # # # #
# Tuples are immutable

tTuple = (147, 212, 398, "a", "b", "b", "c", "d"); #tuple
difTuple = ("Hi", 123, 3.5, False, [23, 12, 15])
tList = [1, 2, 3]; #list
print(type(tTuple),type(tList));
print(len(tTuple)) # length of tuple
print(tTuple)
print(tTuple[0],tTuple[1],tTuple[2])
print(tTuple[-1]) #the last element of tuple
print(tList[-1]) #the last element of list
print(tTuple.count("b"));  # how many times b is in the tuple
print(tTuple.index("a")) # print index of element "a"
#tTuple[0] = "NEW"    #CAN'T assign the element to tuple
#tuple is immutable
print(difTuple[4])






# # # # # # #
print("\n * * * * * * * * SETS * * * * * * * * \n")
# # # # # # #
# unordered collection of unique elements!!!
# NO DUPLICATION!
# No index!
mySet = set()
mySet.add("L")
mySet.add(2)
mySet.add(34)
mySet.add("K")
print(mySet)

myNewSet = {1, 434, 561, 7523}
strSet = {"Hello", "World", "How", "are", "you?"}
print(myNewSet)
print(len(strSet))
strSet.add("are") # NO DUPLICATION! CAN'T add the same element
print(strSet)

strList = ["op", "ol", "ol", "ol", "ol"]
print(set(strList)) #casting List to set, duplicated elements removed!
sekoSet = {"M", "i","s","s","i","s","s","i","p","p","i"}

print(set([1,2,3]))
print(sekoSet)







# # # # # # #
print("\n * * * * * * * * BOOLEANS * * * * * * * * \n")
# # # # # # #

print(9 > 4) #True
print(1 > 4)  #False
b = None # no any assignment. just use as a placeholder
print(type(b)) # Class NoneType