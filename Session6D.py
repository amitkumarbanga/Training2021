number = 10
"""def show():
  # local variable
    number = 20
    print("1. number is:", number)

show()
print("2. number is:", number)
"""
def show():
    global number
    number = 20
    print("1. number is:", number)

show()
print("2. number is:", number)

