# Operations on strings

name = " Amit Kumar"

print(name, type(name), hex(id(name)))

print(name)

another_name = "Rohan Chauchan"

print(another_name, type(name), hex(id(another_name)))

# indexing
print(another_name[0])
print(another_name[2])
print(another_name[len(name)-1])

# Slicing
print(name[1:5])
print(name[5:])

reverse_name = name[::-1]
print(reverse_name)

# Concetination
new_name = name + "Banga"
print(new_name)

# Repetition
repeate_name = name * 5
print(repeate_name)

# Membership Testing
Phone = input("Enter Your Phone Number:")
Email = input("Enter Your Email:")
print(Phone)
print(Email)

if len(Phone) < 10:
    print("Invalid Phone Number:", Phone)
else:
    print("Thank you for entering Phone_number")

if '@' in Email and '.' in Email:
    print("Thank You For Entering Email")
else:
    print("Invalid Email:")
