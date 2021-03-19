"""Value vs References"""

def square_of_number(number):
    print("number is:", number, hex(id(number)))
    number = number * number
    print("number is:", number, hex(id(number)))

def main():
    num = 11
    print("num is:", num, hex(id(num)))
    square_of_number(num)
    print("num is:", num, hex(id(num)))

if __name__ == '__main__':
    main()