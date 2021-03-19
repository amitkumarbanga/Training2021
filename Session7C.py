"""inputs in function"""

def add(num1, num2):
    num1 += 10
    num2 += 20
    sum = num1 + num2

    print("sum of num1:{}, num2:{} is {}".format(num1, num2, sum))

add(num1 = 11, num2 = 21)
add(num1 = 22, num2 = 11)

def add_numbers(num1, num2):
    print("sum is:{}", (num1 + num2))
print(add_numbers)

def add_num(num1, num2, num3):
    print("sum is:{}", (num1 + num2 + num3))
print(add_num)