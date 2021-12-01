# Errors and Exceptions
# try, except, else, finally, as
# Kamran Rashidov
# Date: 11.28.2021


a = 10
b = 0

try:
    a / b
except Exception:
    # except block whenever there is error in try block
    print("Here is error")
else:
    # else block whenever there is no error in try block
    print("result {}".format(a))
finally:
    # finally block it does not matter there is error or not in try block
    print("This is from finally block!")






try:
    num1 = int(input("Please enter number1: "))
    num2 = int(input("Please enter number2: "))
    num3 = num1 / num2

except ZeroDivisionError as e:
    print(e)
    print("Zero d error occured!")
except ValueError as e:
    print(e)
    print("Value")
except Exception as e:
    print(e)
    print("General error detector")
else:
    print(num3)
finally:
    print("Whatever happenes I am here!")