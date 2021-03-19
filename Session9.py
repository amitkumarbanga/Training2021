""" Sequences In Python  (Part II)"""

number1 = (10, 20, 30, 40, 50, 60, 70)
print(number1, type(number1), hex(id(number1)))

print()

number2 = list(number1)
print(number2, type(number2), hex(id(number2)))

print()

number3 = set(number2)
print(number3, type(number3), hex(id(number3)))

print()

number4 = tuple(number3)
print(number4, type(number4), hex(id(number4)))

print()

str_data = str(number4)
print(str_data)
print(str_data[0])

print(number1)
print(number1[::-1])