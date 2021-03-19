"""
OPERATIONS:-
Create(read)
Update
Copy
Delete
"""
# CREATE OPERATION
amit_age = 20

print(amit_age, type(amit_age), id(amit_age))

print()

# UPDATE OPERATION
amit_age = 22

print(amit_age, type(amit_age), id(amit_age))

print()

# COPY OPERATION
divjot_age = 22

amit_age = divjot_age

print(divjot_age, type(divjot_age), id(divjot_age))

# DE:ETE OPERATION
del amit_age
# print(amit_age, type(amit_age), id(amit_age)) this will give an error
print(divjot_age, type(divjot_age), id(divjot_age))