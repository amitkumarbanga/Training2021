employee = {
    "Eid": 1010,
    "Name": "Amit Kumar",
    "Section": "B2",
    "Roll_no": 1721104,
    "Technology": "IT"
}

print(employee)
print(type(employee))
print(min(employee))
print(max(employee))

# Update
employee["Roll_no"] = 1805578

# Deletion
del employee ["Technology"]

# Name
print(employee)
print(employee["Name"])

keys = list(employee.keys())
print(keys, type(keys))

values = list(employee.values())
print(values)

# employee.clear()
