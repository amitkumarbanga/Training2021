"""Value vs References"""

def square_of_number(number):
    print("number is:", number, hex(id(number)))

    for i in range(0, len(number)):
        number[i] = number[i] * number[i]

    print("number is:", number, hex(id(number)))

def main():
    nums = [10, 20, 30, 40, 50]
    print("num is:", nums, hex(id(nums)))
    print("num is[0]:", nums[0], hex(id(nums[0])))
    square_of_number(nums)
    print("num is:", nums, hex(id(nums)))

if __name__ == '__main__':
    main()