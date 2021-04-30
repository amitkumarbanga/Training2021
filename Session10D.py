def get_max_number(*numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number

    return max

def main():
    print(get_max_number(10, 40, 80 ,50, 20, 90, 5))
    print(max(10, 40, 80 ,50, 20, 90, 5))

if __name__ == '__main__':
    main()

