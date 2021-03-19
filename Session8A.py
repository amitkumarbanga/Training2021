numbers = [10, 20, 30, 40, 50]
print("numbers:", numbers, hex(id(numbers)))

numbers = numbers + [60, 70]
print("numbers:", numbers, hex(id(numbers)))

print("Max", max(numbers))
print("Min", min(numbers))
print("Len", len(numbers))
print("Sum", sum(numbers))
