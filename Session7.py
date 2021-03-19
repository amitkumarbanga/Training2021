def show():
    print("Its AK")


def add(num1, num2):
    sum = num1 + num2
    return sum


print("show is:", show, id(show), hex(id(show)))
print("add is:", add)
show()

addition = add
display = show

print("addition is", addition)
print("display is:", display)

show()
display()

print("addition of 11 and 22", add(11, 22))
print("adding 29 and 39", addition(29, 39))

def display():
    print("its mk")
