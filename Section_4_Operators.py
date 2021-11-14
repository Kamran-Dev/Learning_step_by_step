# Section 4: Python Operators
# Author: Kamran Rashidov
# Date: 22.10.2021


# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# Python Arithmetic Operators
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4) # division
print(3 % 4) # modulus
print(3 ** 4) # power
print(12 // 5) # floor division


# Assignment Operators
# Assignment operators are used to assign values to variables:

x = 5
x += 4 # x = x + 4
x -= 5 # x = x - 5





# Comparison Operators
print(1 < 2)
print(2 > 3)
print(2 <= 3) # 2 is small or equal to 3
print(2 >= 3)
print(1 == 2)
print(2 != 3)




# Logical Operators
# and, or, not


print(1 < 2 < 3) # chaining
print(1 < 2 and 2 < 3)
print(1 == 2 or 2 == 2) # true, one of the should be true
print(2 > 1, not (12 > 4 )) # not - reverse the resutl. if true then false


# Python Identity Operators
# Identity operators are used to compare the objects,
# not if they are equal, but if they are actually the same object,
# with the same memory location:

x = 10
y = 10
print(x is y) # Returns True if both variables are the same object
print(x is not y) # Returns True if both variables are not the same object




# Membership Operators
# Membership operators are used to test if
# a sequence is presented in an object:


list1 = [1, 2, 3, "ab", True]
el = 2
print(el in list1) # Returns True if a sequence with the specified value is
# present in the object
print(12 not in list1)  # Returns True if a sequence with the specified value
# is not present in the object


# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
# AND, OR, XOR, NOT, Zero fill left shift, Signed right shift
