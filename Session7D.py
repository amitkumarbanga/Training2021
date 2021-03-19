

def add_numbers(*args):
    print(args)
    print(type(args))

    sum = 0
    for i in range(len(args)):
        sum += args[i]

    print("sum is:", sum)
    print()

add_numbers(10, 20, 30)
add_numbers(10, 20, 30, 40)
add_numbers(10, 20, 30, 40, 50)
add_numbers(10, 20, 30, 40, 50, 60)
