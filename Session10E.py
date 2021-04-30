def get_max_number(data, length):

    if length == 1:
        return data[0]
    else:
        num = get_max_number(data, length-1)
    if num > data[length-1]:
        return num
    else:
        return data[length-1]

def main():
    data = [10, 20, 30]
    max_num = get_max_number(data, len(data))
    print("max number is:", max_num)

if __name__ == '__main__':
    main()

