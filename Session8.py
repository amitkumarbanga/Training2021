students = ("amit", "divjot", "toypom", "nikhil", "guri")
print("students is:", students, type(students))

print()

# 1. Concetination
more_students = students + ("lucky", "leo", "gym")
print("students:", students, type(students))
print("more_students:", more_students, type(more_students))

print()

# 2. Repetition
repeated_students = students * 2
print("students:", students, type(students))
print("repeated_students:", repeated_students, type(repeated_students))

print()

# 3. Membership Testing(in or not on)
print("lucky" in students)
print("fionna" not in students)

print()

# 4. Indexing
print(students[0])
print(students[-2])

print()

# 5. Slicing
print(students[0:3])
sliced_students = students[3:]
print("sliced_students:", sliced_students, type(sliced_students))
print(students[:3])

print()

# Enhanced for loop
for i in range(len(students)):
    print(students[i], end="^^^^^")
