# Dictionaries
# Author: Kamran Rashidov
# Date: 11.25.2021
# NO Duplication


employee  = {"Name": "Raschad", "Surname": "Mirzoyev", "Age": "30"}
print(employee.values())
print(employee.keys())
print(employee.get("Name"))
print(employee.items())
print(employee["Surname"])
employee["Surname"] = "Joe"
print(employee)
# update one or more key and values
employee.update({"Name": "Elvin"})
print(employee)
employee["hobby"] = "Electronics"
print(employee)
del employee["Name"]
del employee["Age"]
print(employee)

for elem in employee.items():
    print(elem)

print(employee.get("Name", "Not found")) # when there is no value. it does NOT return ERROR!