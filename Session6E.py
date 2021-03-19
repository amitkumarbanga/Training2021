"""Recursion In Function"""

def printNumber(number):

    if number == 0:
        return
    else:
        printNumber(number-1)

    print("number is:", number)

def main():
    print("main started")
    printNumber(5)
    print("main finished")


if __name__ == '__main__':
 main()
